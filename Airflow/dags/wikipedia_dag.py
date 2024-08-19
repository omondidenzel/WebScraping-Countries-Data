from airflow import DAG 
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
import datetime
import pendulum

default_param = {
    "ownner":"dev_denzel",
    "start_date":pendulum.datetime(2024, 8, 18),
    "schedule_interval":"0 0 * * *",
    "catchup":False
}

with DAG('wikipedia_extraction', default_args=default_param) as dag:
    start = DummyOperator(
        task_id = 'start'
    )

    extract = BashOperator(
        task_id = 'extraction',
        bash_command='echo "Working" '
    )

    end = DummyOperator(
        task_id = 'end'
    )


start >> extract >> end
