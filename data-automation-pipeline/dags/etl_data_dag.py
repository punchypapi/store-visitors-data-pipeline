#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Example DAG demonstrating the usage of the BashOperator."""

from __future__ import annotations

import datetime

import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

# Create the DAG
with DAG(
    dag_id="etl_data",
    schedule_interval="32 11 * * *",
    start_date=pendulum.datetime(2024, 7, 21, tz="Europe/Paris"),
    catchup=True,
    dagrun_timeout=datetime.timedelta(minutes=120),
    tags=["example", "example2"],
    params={"example_key": "example_value"},
) as dag:

    extract_data_api = BashOperator(
        task_id="extract_data_api",
        bash_command="python /opt/airflow/dags/scripts/script_generate_data.py",
    )

    transform_data = BashOperator(
        task_id="transform_data",
        bash_command="python /opt/airflow/dags/scripts/transform_data.py",
    )

    create_database = BashOperator(
        task_id="create_database",
        bash_command="python /opt/airflow/dags/scripts/init_db.py",
    )

    extract_data_api >> transform_data >> create_database


if __name__ == "__main__":
    dag.test()
