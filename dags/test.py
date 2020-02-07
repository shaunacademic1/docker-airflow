from airflow import DAG
import datetime
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from dags.variables import START_DATE

import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

first_brace = '{'
second_brace = '}'

test_date = f"'{first_brace}{first_brace}macros.ds_add({START_DATE}, 0){second_brace}{second_brace}'"

def log_info():
    log.info(test_date)
    return

my_dag = DAG(
    'my-dag',
    description="Nighly ETL From Production Database",
    schedule_interval='05 * * * *', 
    start_date=datetime.datetime(2019, 11, 13),
    catchup=False,
)

my_task = PythonOperator(task_id='my_task', dag=my_dag)
