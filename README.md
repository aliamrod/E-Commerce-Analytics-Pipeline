# E-Commerce-Analytics-Pipeline


## Objective
The objective of this project is to build a data pipeline that automates the extraction, transformation, and loading (ETL) of e-commerce data to generate meaningful analytics. This pipeline simulates a real-world data engineering scenario, transforming raw data into insights such as top-performing products, customer trends, and order analysis.

---

## Data Source
The data for this project is provided in CSV files located in the `data/` directory:
- **orders.csv**: Contains order details such as order IDs, customer IDs, product IDs, and order status.
- **products.csv**: Includes product details such as product IDs, names, categories, and prices.
- **customers.csv**: Contains customer information such as customer IDs, names, and locations.

---

## Pipeline Overview
The pipeline processes the raw data in the following stages:

1. **Data Extraction**:  
   - Python scripts read the raw CSV files from the `data/` directory and load them into a staging database.

2. **Data Transformation**:  
   - Using dbt, the raw data is transformed into analytics-ready tables.  
   - Key transformations include:
     - Filtering out cancelled or incomplete orders.
     - Joining customer, order, and product data for analysis.
     - Aggregating metrics such as total revenue and product popularity.

3. **Analytics and Reporting**:  
   - Transformed data is queried to generate insights and dashboards.
   - Example metrics include top customers, most popular product categories, and order trends.

---

## Tech Stack

### 1. Apache Airflow  
- Automates and schedules the pipeline tasks.  
- Orchestrates the execution of Python scripts and dbt models.

### 2. Python  
- Used for the extraction of raw data from CSV files into the staging database.  
- Libraries like `pandas` and `sqlalchemy` are utilized for data manipulation and database interaction.

### 3. dbt (Data Build Tool)  
- Handles data transformations in SQL.  
- Enables version control and modular transformations for clean and reusable models.

### 4. PostgreSQL (or SQLite)  
- Serves as the staging and analytics database.  
- Stores raw and transformed data for querying and reporting.

---

## Directory Structure

```plaintext
ecommerce-analytics-pipeline/
│
├── airflow/
│   ├── dags/
│   │   ├── ecommerce_data_pipeline.py  # Airflow DAG definition
│
├── dbt/
│   ├── models/
│   │   ├── staging/
│   │   │   ├── staging_orders.sql
│   │   │   ├── staging_products.sql
│   │   │   ├── staging_customers.sql
│   │   ├── marts/
│   │       ├── orders_transformed.sql
│
├── data/
│   ├── orders.csv  # Raw order data
│   ├── products.csv  # Raw product data
│   ├── customers.csv  # Raw customer data
│
├── scripts/
│   ├── load_data.py  # Python script for data extraction
│
└── README.md
