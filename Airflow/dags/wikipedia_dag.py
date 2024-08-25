from airflow import DAG 
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
import datetime
import pendulum
import etl

default_param = {
    "ownner":"dev_denzel",
    "start_date":pendulum.datetime(2024, 8, 18),
    "schedule_interval":"0 0 * * *",
    "catchup":False
}


with DAG('wikipedia_extraction', default_args=default_param) as dag:
    start = EmptyOperator(
        task_id = 'start'
    )

    extract = PythonOperator(
        task_id = 'extraction',
        python_callable= etl.get_data
    )

    end = EmptyOperator(
        task_id = 'end'
    )


start >> extract >> end
