# Data Quality Pipeline for Store Visitors

## Overview

This project focuses on the end-to-end process of generating, retrieving, transforming, and visualizing store visitor data. The core objective is to simulate realistic visitor count data for multiple stores, expose this data through a GET API, and create a comprehensive dashboard for insights using Streamlit.

## Features

* **Data Generation:** Simulate realistic visitor count data for multiple stores.
* **API Exposure:** Retrieve the data through a GET API and save it to a CSV file.
* **Data Transformation:** Use PySpark for data transformation and save the results in parquet format.
* **Database:** Load the parquet file into DuckDB.
* **Visualization:** Develop an interactive dashboard with Streamlit, including data quality checks.

## Project Structure

├── README.md
├── .gitignore
├── requirements.txt
├── .github
│   ├── workflows
│       ├── code_quality.yaml
│       └── unit_tests.yaml
├── src
│   ├── app
│   │   └── app.py
│   ├── data
│   │   ├── init_db.py
│   │   ├── script_generate_data.py
│   │   └── transform_data.py
│   └── utils
│       ├── __init__.py
│       └── sensor.py
├── get_number_visitors_api.py
├── tests
│   ├── __init__.py
│   ├── test_db.py
│   ├── test_sensor_api.py
│   └── test_sensor_method.py




* **src/utils/**: Scripts for simulating store visitor data.
* **tests/test_sensor_method.py**: Unit tests for different methods used to generate data.
* **get_number_visitors_api.py**: Scripts for creating API method GET.
* **src/data/**: Scripts for retriving data from API and transforming the data using PySpark.
* * **data/**: Different repositories where data is written and saved.
* **src/app/app.py**: Streamlit app for data visualization and quality checks.

## Tickets and Workflow

### Ticket 1: Generate Visitor Data

* **Description:** Develop a script to simulate realistic visitor count data for multiple stores.
* **Files:** `src/utils/`

### Ticket 2: Set Up API

* **Description:** Create a Flask app to expose the generated data through a GET API.
* **File:** `get_number_visitors_api.py`

### Ticket 3: Retrieve Data from API

* **Description:** Use a Python script to retrieve data from the API and save it to a CSV file.
* **File:** `src/data/`

### Ticket 4: Data Transformation with PySpark

* **Description:** Clean and transform the data using PySpark, and save the transformed data in Parquet format.
* **File:** `transformation/transform_pyspark.py`

### Ticket 5: Load Data into DuckDB

* **Description:** Load the Parquet file into DuckDB for efficient querying.
* **File:** `transformation/load_duckdb.py`

### Ticket 6: Data Quality Checks

* **Description:** Implement data quality checks and visualize the data using a Streamlit dashboard.
* **File:** `dashboard/data_quality_checks.py`

### Ticket 7: Develop Streamlit Dashboard

* **Description:** Create an interactive dashboard using Streamlit to visualize the data and perform quality checks.
* **File:** `dashboard/app.py`

### Ticket 8: Create Local DAG with Airflow (Optional)

* **Description:** Define and manage a local Directed Acyclic Graph (DAG) using Apache Airflow to orchestrate the data pipeline.
* **File:** `airflow/dags/store_visitors_dag.py`

## Setup and Installation

1. Clone the repository:

```bash
git clone [https://github.com/yourusername/store-visitors-data-pipeline.git](https://github.com/yourusername/store-visitors-data-pipeline.git)
```

2. Navigate to the project directory:

```bash
cd store-visitors-data-pipeline
```

3. Set up a virtual environment :

```bash
python3 -m venv venv 
```
   
4.Install the required dependencies:

```bash
pip install -r requirements.txt
```

5.Set the `PYTHONPATH` environment variable:

```bash
export PYTHONPATH=$(pwd)
```

## Usage 

### Data Generation

1. Run the data generation script to simulate visitor data:

```bash
python src/utils/__init__.py
```

2. Run the unit tests for `Sensor` class methods :

```bash
python -m unittest tests/test_sensor_method.py
```

### API

1. Start the FastAPI API:

```bash
python get_number_visitors_api.py
```

2. Retrieve data from API and save it in a CSV file in `data/raw`:

```bash
python src/data/script_generate_data.py
```

**Note:** you can shutdown the FastAPI Server once the CSV file is created

### Data Transformation and Loading 

1. Transform the data using PySpark and save it in a Parquet file in `data/processed` :

```bash
python src/data/transform_data.py
```

2. Load the transformed data into DuckDB and create a Duckdb database in `data/database` :

```bash
python src/data/transform_data.py
```

### Visualization 

Start the Streamlit dashboard :

```bash
streamlit run src/app/app.py
```
   









