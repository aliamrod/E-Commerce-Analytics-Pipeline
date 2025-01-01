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
```

---

### Directions

#### Install SQLite

SQLite is bundled with Python. To check:

```bash
sqlite3 --version
```

--- 
## Exploratory Analysis and Statistics

At this point, we have walked through the process of setting up a data pipeline that integrates raw data files into a SQLite database for analysis. We started by importing and cleaning data from CSV files into pandas DataFrames, then loaded this data into SQLite tables using Python's SQLite3 library. Once the data was successfully stored in the database, we utilized SQL queries to retrieve the data into pandas for further analysis. The dataset contained information about customer orders, including their status (Completed, Pending, Cancelled), which laid the foundation for exploring patterns in order processing.

We then conducted exploratory data analysis (EDA) to better understand the distribution of order statuses and gain insights into trends. Using Python's pandas and matplotlib, we visualized the frequency of each order status to identify any potential imbalances. To dive deeper into the relationships between the status categories, we applied a Chi-Square Test of Independence to assess whether the order status distribution differed significantly from a uniform distribution. The test returned a p-value of 0.257, suggesting that the observed distribution of statuses (Completed, Pending, Cancelled) does not significantly differ from what would be expected by chance, implying that the differences in order statuses may be attributed to random variation. This statistical analysis provides a better understanding of how orders are distributed and whether external factors might be influencing the data.
