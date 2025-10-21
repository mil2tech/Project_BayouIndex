# Project Bayou Index

### Purpose
This project automates the retrieval and analysis of key **economic indicators** for the **Houston–The Woodlands–Sugar Land metropolitan area**, using the **U.S. Bureau of Labor Statistics (BLS) Public Data API (v2)**.  

The project focuses on building a clean and reusable data pipeline capable of collecting time-series data such as the Consumer Price Index (CPI), average prices for goods and services, wages, and employment statistics.  
By automating this process, the project eliminates the need for manual data downloads, ensuring that local economic datasets remain accurate, current, and easily reproducible for future analysis and visualization.

The long-term goal is to establish a foundation for advanced analytics, forecasting, and dashboard development — enabling consistent monitoring of Houston’s economic trends over time.

---

### Project Evolution
This project builds on the foundation of the [**original Houston CPI Time Series Forecasting Project**](https://github.com/mil2tech/individiual-project), which focused exclusively on predicting **Consumer Price Index (CPI)** trends (2009–2021) using manually downloaded datasets and Holt’s linear trend model.  

The current project modernizes that effort by:
- Automating data acquisition using the **BLS API (v2)**
- Integrating **secure API key management** via a `.env` file
- Maintaining **data reproducibility and integrity**
- Expanding the dataset to include multiple local economic indicators


---

### Expanded Scope
While the original project analyzed only CPI trends, this new version broadens the analysis to include a variety of economic variables specific to the **Houston metro area**, including:

| Category | Description | Example Series |
|-----------|--------------|----------------|
| **Consumer Price Index (CPI)** | Overall inflation trends and cost of living | `CUURS37ASA0` – CPI for All Urban Consumers, Houston area |
| **Average Prices** | Prices of goods and services such as gasoline, groceries, and utilities | `APUS37B74714` – Gasoline, unleaded regular, per gallon |
| **Employment & Unemployment** | Labor market indicators and jobless rates | LAUS (Local Area Unemployment Statistics) series |


Each dataset provides insight into different dimensions of Houston’s economy, enabling a holistic view of economic health and cost-of-living dynamics in the region.

---

### Environment Configuration

1. **BLS API Key**
   - Successfully registered and approved with the **Bureau of Labor Statistics Developer Program**. Click [here](https://data.bls.gov/registrationEngine/)
   - The API key is stored securely in a local `.env` file:
     ```bash
     BLS_API_KEY=your_actual_bls_api_key_here
     ```

2. **Git Ignore**
   - The `.gitignore` file protects sensitive information from being tracked:
     ```bash
     .env
     ```
   - Ensures API credentials remain private and the repository stays clean.

---

### Technical Highlights
- **Data Source:** U.S. Bureau of Labor Statistics (BLS) Public Data API (v2)
- **Region of Focus:** Houston–The Woodlands–Sugar Land, TX Metropolitan Area
- **Primary Objective:** Automated retrieval of CPI, price, and employment data
- **Core Stack:** Python, Pandas, Requests, JSON
- **API Key Security:** Implemented environment-based key management using `.env` (ignored via `.gitignore`)
- **Error Handling:** Added validation for response codes and API-level status messages
- **Metadata Extraction:** Pulls series title, area, and item information alongside data values
- **Output Format:** Structured JSON responses and CSV export for local validation
- **Coding Standards:** Follows NASA-style clarity and explicitness for data safety and reliability  

---

### Relation to Previous Work
This project directly extends the **Houston CPI Forecasting Project**, transforming it from a single-variable model into a **multi-dimensional economic data pipeline**.  
Where the prior version focused on CPI forecasting from static Excel files, this project:
- Automates the retrieval of local economic data
- Enables continuous updates as new BLS releases are published
- Establishes a foundation for live analysis and future forecasting integrations

---

### Project Roadmap

The following sections outline the current progress, short-term development steps, and long-term goals for this project.  
Each stage builds upon the previous one — evolving the system from basic data acquisition into a scalable, automated data engineering and analytics platform for the **Houston–The Woodlands–Sugar Land metropolitan area**.

---

## Current Stage
The project is currently in the **data acquisition and validation phase**.  
The focus at this stage is to establish a reliable process for collecting and organizing data from the **Bureau of Labor Statistics (BLS) Public Data API (v2)** specific to the Houston metropolitan area.  

Work in progress includes:
- Developing Python scripts to connect to the BLS API and fetch time-series data for CPI, prices, employment, and wages.  
- Verifying API responses, structure, and consistency for each series.  
- Implementing error handling for incomplete or missing data.  
- Capturing metadata (series titles, areas, and items) for each dataset.  
- Logging API calls and saving raw JSON responses for reproducibility.  

This foundational stage ensures that future phases of the project are built on **accurate, validated, and well-structured data sources**.  

---

### Next Steps
The next stages of development will expand upon the data acquisition foundation, introducing structured transformation, storage, and long-term automation.  

Planned next steps:
1. **Data Structuring and Transformation**  
   - Convert raw BLS JSON data into standardized Pandas DataFrames.  
   - Merge multiple datasets (CPI, unemployment, prices, and wages) into a unified Houston dataset.  
   - Handle missing values and ensure time-series consistency.  
   - Export transformed datasets to CSV for preliminary analysis.  

2. **Data Engineering Foundations**  
   - Develop an **ETL (Extract–Transform–Load)** pipeline to automate data ingestion and transformation.  
   - Implement local database storage using SQLite or PostgreSQL.  
   - Add validation layers for schema consistency and data quality.  
   - Introduce scheduling for regular updates using Prefect or cron.  

3. **Data Analysis and Visualization**  
   - Conduct exploratory analysis to identify economic trends.  
   - Visualize changes in CPI, prices, employment, and wages across time.  
   - Build prototype dashboards for local economic indicators.  

4. **Cloud and Automation Expansion (Future)**  
   - Deploy ETL processes to cloud infrastructure (AWS Lambda or GCP Functions).  
   - Integrate cloud storage for long-term historical data.  
   - Automate monthly updates aligned with new BLS data releases.  

These steps will evolve the project from a **manual data retrieval script** into a **full-fledged data engineering and analytics pipeline** for the Houston metropolitan economy.  

---

### Future Development Goals
These goals will follow the successful completion of the **Next Steps** phase and focus on scaling the system for broader functionality and automation.  

- 📊 **Interactive Dashboards:** Develop live dashboards (Tableau, Power BI, or Streamlit) to visualize CPI, prices, and unemployment trends.  
- 🔄 **Automated Updates:** Schedule periodic API pulls for new BLS data releases.  
- 🧮 **Forecasting Models:** Extend existing CPI models to include multiple economic variables for multi-factor predictions.  
- 🗄️ **Database Integration:** Store historical BLS data in SQL or cloud databases for trend tracking.  
- 🧠 **Regional Comparisons (Long-Term):** Benchmark Houston against other major Texas metro areas.  

---

> **Author’s Note:**  
> This project represents the next evolution of the original Houston CPI analysis—transforming it into a dynamic, API-powered data pipeline that captures the broader economic picture of Houston through local prices, wages, and employment trends.
