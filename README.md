# 📊 UPI Pulse — India's Digital Payments Revolution, Visualised

> Six years of real NPCI data. One dashboard that tells the whole story.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red?style=flat-square&logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-5.20+-purple?style=flat-square&logo=plotly)
![Data Source](https://img.shields.io/badge/Data-NPCI%20Official-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 🇮🇳 What is this?

UPI Pulse is an interactive Streamlit dashboard that visualises India's Unified Payments Interface (UPI) growth from **FY2020 to FY2025** using **official NPCI statistics**.

From ₹1 lakh crore months in 2019 to ₹24.77 lakh crore in March 2025 — this dashboard tells the story of how **a billion people moved to instant digital payments** in under a decade.

---

## ✨ Features

- **Dual-axis trend line** — Monthly transaction volume & value on one canvas, with annotated milestones
- **Annual bar charts** — FY-wise volume and value comparison across 6 financial years
- **YoY growth chart** — Month-by-month year-on-year growth rates, green/red coded
- **Cumulative transactions** — The compounding story of 17,000+ crore total transactions
- **Seasonality heatmap** — Spot which months spike every year at a glance
- **Live KPI cards** — Latest month stats with YoY delta, always up top
- **Raw data table** — Expandable view of all monthly figures

---

## 📸 Preview

> *Dark-themed, premium UI — built to impress*

| Hero & KPIs | Trend Charts |
|---|---|
| Real-time KPI cards with YoY delta | Dual-axis volume + value trend |
| Milestone chips (all-time records) | YoY growth bar chart |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip

### Installation

```bash
# Clone the repo
git clone https://github.com/Bhoomika-404Error/UPI_Pulse.git
cd UPI_Pulse/UPI

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run upi_dashboard.py
```

The app will open at `http://localhost:8501` 🎉

---

## 📦 Dependencies

```
streamlit>=1.32.0
pandas>=2.0.0
plotly>=5.20.0
numpy>=1.26.0
```

---

## 📂 Project Structure

```
UPI_Pulse/
├── UPI/
│   ├── upi_dashboard.py      # Main Streamlit app
│   └── requirements.txt      # Python dependencies
└── README.md
```

---

## 📊 Data Source

All data is sourced from **NPCI (National Payments Corporation of India)** official UPI Ecosystem Statistics.

- 🔗 [NPCI UPI Statistics](https://www.npci.org.in/what-we-do/upi/upi-ecosystem-statistics)
- Coverage: **April 2019 – March 2025** (72 months)
- Metrics: Monthly transaction volume (Crore) & value (₹ Lakh Crore)

---

## 🏆 Key Insights from the Data

| Milestone | Value |
|---|---|
| All-time record value | ₹24.77 Lakh Cr (Mar 2025) |
| All-time record volume | 1,836 Crore txns (Mar 2025) |
| FY25 total value processed | ₹264 Lakh Crore (~$2.7 Trillion USD) |
| FY25 total transactions | 18.83 Billion |
| Growth FY21→FY22 | +85% YoY (post-COVID surge) |
| UPI's global rank | #1 real-time payments system on Earth |

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) — App framework
- [Plotly](https://plotly.com/python/) — Interactive charts
- [Pandas](https://pandas.pydata.org/) — Data processing
- [NPCI](https://www.npci.org.in/) — Official data source

---

## 👩‍💻 Author

**Bhoomika** — [@Bhoomika-404Error](https://github.com/Bhoomika-404Error)

*Built as part of a fintech data analytics portfolio project.*

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <sub>Made with ❤️ and real data · India's fintech story deserves to be visualised</sub>
</div>
