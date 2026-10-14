# Project 4 — Data Visualization: Sales Insight Studio

A runnable interactive analytics dashboard based on the themes in the provided *Data Analytics Project 4* guide: choose charts for the business question, keep axes honest, reduce chart clutter, label directly, write action-oriented headlines, and structure a concise executive story.

## Features
- Executive KPI cards for revenue, units, regions, and average return rate
- Monthly revenue trend and region/category comparisons
- Interactive filters for date range, region, and category
- Relationship explorer and return-rate distribution (when data supports it)
- Basic data-quality checks
- Upload your own CSV and download filtered data plus a summary
- Responsive layout via Streamlit

## Tech stack
- Python — application logic
- Pandas — data loading, cleaning, grouping, and metrics
- Plotly Express — interactive charts
- Streamlit — dashboard UI and controls

## Run on Windows
1. Install Python 3.10 or newer from https://www.python.org/downloads/
2. Extract this ZIP.
3. Open PowerShell in the extracted `Data-Visualization-Project-4` folder.
4. Run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

Your browser should open the dashboard. If PowerShell blocks activation, use `.venv\Scripts\python.exe -m pip install -r requirements.txt` then `.venv\Scripts\python.exe -m streamlit run app.py`.

## CSV format for your own data
Required columns: `month`, `region`, `category`, `units_sold`, `revenue_inr`
Optional columns: `avg_unit_price_inr`, `return_rate`

Example:
```csv
month,region,category,units_sold,revenue_inr
2025-01,North,Electronics,120,18000
```

`month` should be parseable as a date. `revenue_inr` is treated as Indian rupees. The bundled dataset is synthetic demo data, not actual company performance.

## Suggested portfolio description
**Sales Insight Studio — Data Visualization Dashboard**  
Built an interactive sales analytics dashboard using Python, Pandas, Streamlit, and Plotly. Visualized revenue trends, regional and category performance, explored variable relationships, added data-quality checks, and enabled CSV/summary exports. Focused on clear chart selection, truthful axes, concise executive headlines, and actionable storytelling.

## Important
- Replace synthetic data with a dataset you have permission to use before making factual business claims.
- The PDF guide is primarily a data-visualization/storytelling playbook, not a specified business dataset. This implementation uses a synthetic sales dataset as a practical, runnable starting point.

<img width="1158" height="861" alt="Screenshot 2026-10-14 093739" src="https://github.com/user-attachments/assets/5476f7c2-089e-484d-bd30-c1b83ba2e779" />

<img width="762" height="858" alt="Screenshot 2026-10-14 093805" src="https://github.com/user-attachments/assets/5a7a8215-60ab-4785-b986-1eb6dcbb120c" />
