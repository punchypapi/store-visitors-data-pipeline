# Data Quality Pipeline for Store Visitors

## Overview

This project focuses on the end-to-end process of generating, retrieving, transforming, and visualizing store visitor data. The core objective is to simulate realistic visitor count data for multiple stores, expose this data through a GET API, and create a comprehensive dashboard for insights using Streamlit. The pipeline automation is managed using Apache Airflow and all components run in Docker containers.
## Features

* **Data Generation:** Simulate realistic visitor count data for multiple stores.
* **API Exposure:** Retrieve the data through a GET API and save it to a CSV file.
* **Data Transformation:** Use PySpark for data transformation and save the results in parquet format.
* **Database:** Load the parquet file into DuckDB.
* **Visualization:** Develop an interactive dashboard with Streamlit, including data quality checks.
* **Pipeline Automation:** Automate the entire data pipeline using Apache Airflow.
## Project Structure
```
├── README.md
├── .gitignore
├── .github
│   ├── workflows
│       ├── code_quality.yaml
│       └── unit_tests.yaml
├── data-automation-pipeline
│   ├── dags
│   │   ├── etl_data_dag.py
│   │   └── scripts
│   │       ├── init_db.py
│   │       ├── script_generate_data.py
│   │       └── transform_data.py
├── src
│   ├── api
│   │   └── get_number_visitors_api.py
│   ├── app
│   │   └── app.py
│   └── utils
│       ├── __init__.py
│       └── sensor.py
├── tests
│   ├── test_db.py
│   ├── test_sensor_api.py
│   └── test_sensor_method.py
├── requirements.txt
├── .dockerignore
├── Dockerfile
├── server-api.dockerfile
├── app.dockerfile
├── docker-compose.yaml
```

## Tickets and Workflow

### Ticket 1: Generate Visitor Data

* **Description:** Develop a script to simulate realistic visitor count data for multiple stores.
* **Files:** `src/utils/`

### Ticket 2: Set Up API

* **Description:** Create a FastAPI app to expose the generated data through a GET API.
* **File:** `src/api/get_number_visitors_api.py`

### Ticket 3: Retrieve Data from API

* **Description:** Use a Python script to retrieve data from the API and save it to a CSV file in subdirectory `data/raw`
* **File:** `data-automation-pipeline/dags/sripts/script_generate_data.py`

### Ticket 4: Data Transformation with PySpark

* **Description:** Clean and transform the data using PySpark, and save the transformed data in Parquet format in subdirectory `data/processed`
* **File:** `data-automation-pipeline/dags/sripts/transform_data.py`

### Ticket 5: Load Data into DuckDB

* **Description:** Load the Parquet file into DuckDB for efficient querying. The database in saved in subfolder in subdirectory `data/database`
* **File:** `data-automation-pipeline/dags/sripts/init_db.py`

### Ticket 6: Develop Streamlit Dashboard for Data Quality Checks

* **Description:** Create an interactive dashboard using Streamlit to visualize the data and perform quality checks.
* **File:** `src/app/app.py`

### Ticket 7: Create DAG with Airflow

* **Description:** Define and manage a Directed Acyclic Graph (DAG) using Apache Airflow to orchestrate the data pipeline. The DAG automates the extraction, transformation, and loading (ETL) of data using Docker containers for execution.
* **File:** `data-automation-pipeline/dags/etl_data_dag.py`

## Setup and Installation

### Prerequisites

Ensure you have Docker and Docker Compose installed on your machine.

1. Clone the repository using SSH key:

```bash
git clone git@github.com:punchypapi/store-visitors-data-pipeline.git
```

2. Navigate to the project directory:

```bash
cd store-visitors-data-pipeline
```
3. Create necessary directories for storing data:

```bash
mkdir -p data/raw data/processed data/database
```
### Initializing Airflow Environment

4. Create necessary directories:

```bash
mkdir -p ./data-automation-pipeline/logs ./data-automation-pipeline/plugins ./data-automation-pipeline/config
```

5. Create an `.env` file to store necessary environment variables :

```bash
echo -e "AIRFLOW_VERSION=2.9.3\nAIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
```
6. Build images and run containers :

```bash
docker-compose up --build
```

7. Track running containers :

```bash
docker-compose ps
```


## Usage 

1. Start the FastAPI server container (if not already running):

```bash
docker-compose up fastapi-server
```
The API server will be available at http://localhost:8000

2. Access the Airflow web server at http://localhost:8080 and trigger the DAG named `etl_data`. 
This will automate the extraction of API data, transform it into Parquet format, and load it into DuckDB.


3. Start the Streamlit app container (if not already running):

```bash
docker-compose up streamlit-app
```
The Streamlit dashboard will be available at http://localhost:8501




   









