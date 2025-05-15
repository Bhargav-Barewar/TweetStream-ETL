from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta
from airflow.utils.dates import days_ago
from datetime import datetime
from etl_function import etl_process

default_args = {
    'owner': 'airflow',
    'depends_on_post': False,
    'start_date': datetime(2025,1,1),
    'email': ['airflow@emample.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args = default_args,
    description = 'My first etl code',
    schedule_interval='@daily',
    catchup=False

)

run_etl = PythonOperator(
    task_id = 'complete_twitter_etl',
    python_callable = etl_process,
    dag = dag
)

run_etl