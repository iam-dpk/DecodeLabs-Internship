import io
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Sales Insight Studio", page_icon="📊", layout="wide")
DATA_PATH = Path(__file__).parent / "data" / "sales_data.csv"

st.markdown("""
<style>
.stApp { background: #f6f8fc; }
.block-container { padding-top: 1.7rem; max-width: 1450px; }
[data-testid="stMetric"] { background: white; padding: 18px; border-radius: 14px; border: 1px solid #e6eaf2; }
h1, h2, h3 { letter-spacing: -0.025em; }
</style>
""", unsafe_allow_html=True)

st.title("📊 Sales Insight Studio")
st.caption("Project 4 · Data Visualization | Turn raw sales data into decision-ready insights")
st.info("This portfolio demo uses a **synthetic sample dataset**. Replace it with verified business data before drawing real-world conclusions.")

@st.cache_data
def load_default():
    return pd.read_csv(DATA_PATH)

uploaded = st.sidebar.file_uploader("Upload your own CSV (optional)", type=["csv"])
try:
    raw = pd.read_csv(uploaded) if uploaded else load_default()
except Exception as e:
    st.error(f"Could not read the CSV: {e}")
    st.stop()

required = {"month", "region", "category", "units_sold", "revenue_inr"}
missing = required - set(raw.columns)
if missing:
    st.error("CSV is missing required columns: " + ", ".join(sorted(missing)))
    st.markdown("Required: `month`, `region`, `category`, `units_sold`, `revenue_inr`. Optional: `avg_unit_price_inr`, `return_rate`.")
    st.stop()

raw["month"] = pd.to_datetime(raw["month"], errors="coerce")
for col in ["units_sold", "revenue_inr", "avg_unit_price_inr", "return_rate"]:
    if col in raw.columns:
        raw[col] = pd.to_numeric(raw[col], errors="coerce")
raw = raw.dropna(subset=["month", "region", "category", "units_sold", "revenue_inr"])
if raw.empty:
    st.warning("No valid rows found in the uploaded file.")
    st.stop()

st.sidebar.header("Filter the story")
regions = sorted(raw["region"].astype(str).unique())
categories = sorted(raw["category"].astype(str).unique())
selected_regions = st.sidebar.multiselect("Regions", regions, default=regions)
selected_categories = st.sidebar.multiselect("Categories", categories, default=categories)
min_date, max_date = raw["month"].min().date(), raw["month"].max().date()
date_range = st.sidebar.date_input("Month range", value=(min_date, max_date), min_value=min_date, max_value=max_date)

filtered = raw[raw["region"].astype(str).isin(selected_regions) & raw["category"].astype(str).isin(selected_categories)].copy()
if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    start, end = pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1]) + pd.offsets.MonthEnd(0)
    filtered = filtered[(filtered["month"] >= start) & (filtered["month"] <= end)]
if filtered.empty:
    st.warning("No rows match those filters. Change your selection in the sidebar.")
    st.stop()

revenue = filtered["revenue_inr"].sum()
units = filtered["units_sold"].sum()
n_regions = filtered["region"].nunique()
avg_return = filtered["return_rate"].mean() if "return_rate" in filtered.columns else None
m1, m2, m3, m4 = st.columns(4)
m1.metric("Total revenue", f"₹{revenue:,.0f}")
m2.metric("Units sold", f"{units:,.0f}")
m3.metric("Regions", f"{n_regions}")
m4.metric("Average return rate", f"{avg_return:.1%}" if pd.notna(avg_return) else "Not provided")

monthly = filtered.groupby("month", as_index=False).agg(revenue_inr=("revenue_inr","sum"), units_sold=("units_sold","sum")).sort_values("month")
by_region = filtered.groupby("region", as_index=False).agg(revenue_inr=("revenue_inr","sum"), units_sold=("units_sold","sum")).sort_values("revenue_inr", ascending=False)
by_category = filtered.groupby("category", as_index=False).agg(revenue_inr=("revenue_inr","sum"), units_sold=("units_sold","sum")).sort_values("revenue_inr", ascending=False)

tab1, tab2, tab3, tab4 = st.tabs(["Executive overview", "Explore patterns", "Data quality", "Export"])
with tab1:
    st.subheader("The story behind the numbers")
    if len(monthly) >= 2:
        first, last = monthly.iloc[0]["revenue_inr"], monthly.iloc[-1]["revenue_inr"]
        change = ((last - first) / first * 100) if first else 0
        best_region = by_region.iloc[0]["region"] if not by_region.empty else "—"
        best_category = by_category.iloc[0]["category"] if not by_category.empty else "—"
        st.markdown(f"**Headline:** Revenue changed by **{change:+.1f}%** between the first and last selected months. **{best_region}** leads regional revenue, while **{best_category}** is the top category in the current selection.")
    else:
        st.markdown("**Headline:** Select at least two months to compare revenue over time.")
    left, right = st.columns(2)
    with left:
        fig = px.line(monthly, x="month", y="revenue_inr", markers=True, title="Revenue trend over time", labels={"month":"Month","revenue_inr":"Revenue (₹)"})
        fig.update_layout(margin=dict(l=10,r=10,t=55,b=10), plot_bgcolor="white", paper_bgcolor="white")
        st.plotly_chart(fig, use_container_width=True)
    with right:
        fig = px.bar(by_region, x="region", y="revenue_inr", text_auto=".2s", title="Revenue by region", labels={"region":"Region","revenue_inr":"Revenue (₹)"})
        fig.update_layout(margin=dict(l=10,r=10,t=55,b=10), plot_bgcolor="white", paper_bgcolor="white")
        st.plotly_chart(fig, use_container_width=True)
    fig = px.bar(by_category, x="category", y="revenue_inr", color="category", text_auto=".2s", title="Category contribution", labels={"category":"Category","revenue_inr":"Revenue (₹)"})
    fig.update_layout(showlegend=False, margin=dict(l=10,r=10,t=55,b=10), plot_bgcolor="white", paper_bgcolor="white")
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Interpretation tip: describe what changed, quantify the difference, then state the business action that the evidence supports.")
with tab2:
    st.subheader("Explore relationships")
    c1, c2 = st.columns(2)
    with c1:
        x_options = [c for c in ["units_sold","avg_unit_price_inr","return_rate","revenue_inr"] if c in filtered.columns]
        x = st.selectbox("X-axis", x_options, index=0)
        y = st.selectbox("Y-axis", x_options, index=min(1, len(x_options)-1))
        fig = px.scatter(filtered, x=x, y=y, color="region", size="revenue_inr", hover_data=["month","category"], title="Relationship explorer")
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        if "return_rate" in filtered.columns:
            fig = px.box(filtered, x="category", y="return_rate", color="category", title="Return-rate spread by category")
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Add a `return_rate` column to explore returns.")
    st.subheader("Ranked results")
    st.dataframe(by_region, use_container_width=True, hide_index=True)
with tab3:
    st.subheader("Check the data before telling the story")
    quality = pd.DataFrame({
        "Check": ["Rows loaded", "Duplicate rows", "Missing values", "Negative revenue rows", "Negative unit rows"],
        "Result": [len(raw), int(raw.duplicated().sum()), int(raw.isna().sum().sum()), int((raw["revenue_inr"] < 0).sum()), int((raw["units_sold"] < 0).sum())]
    })
    st.dataframe(quality, use_container_width=True, hide_index=True)
    st.markdown("**Chart integrity checklist**")
    st.markdown("- Start bar charts at zero when comparing magnitudes.\n- Label units and time periods clearly.\n- Use color to emphasize meaning, not decoration.\n- Prefer direct labels and a small number of categories.\n- Separate observed facts from explanations or assumptions.")
    st.caption("This dashboard flags basic issues; it does not certify that a dataset is accurate or complete.")
with tab4:
    st.subheader("Download the filtered view")
    st.download_button("Download filtered CSV", filtered.to_csv(index=False).encode("utf-8"), file_name="filtered_sales_data.csv", mime="text/csv")
    report = io.StringIO()
    report.write("SALES INSIGHT STUDIO — SUMMARY\n")
    report.write(f"Rows included: {len(filtered)}\nTotal revenue (INR): {revenue:.2f}\nUnits sold: {units:.0f}\n")
    if not by_region.empty:
        report.write(f"Top region by revenue: {by_region.iloc[0]['region']}\n")
    if not by_category.empty:
        report.write(f"Top category by revenue: {by_category.iloc[0]['category']}\n")
    st.download_button("Download text summary", report.getvalue(), file_name="sales_summary.txt", mime="text/plain")
    st.dataframe(filtered, use_container_width=True, hide_index=True)

st.divider()
st.caption("Project 4 · Data Visualization | Built with Python, Pandas, Streamlit and Plotly")
