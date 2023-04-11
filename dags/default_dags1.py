from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 10),
    'email': ['elton.c.s1979@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10)
}

dag = DAG(
    'defaultargs',
    description="Default arguments",
    default_args=default_args,
    schedule_interval='@hourly',
    start_date=datetime(2023, 4, 10),
    catchup=False,
    default_view='graph',
    tags=['process', 'tags', 'pipeline']
)


task1 = BashOperator(
    task_id="tks1", bash_command="sleep 5", dag=dag, retries=3
)
task2 = BashOperator(task_id="tks2", bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id="tks3", bash_command="sleep 5", dag=dag)

task1 >> task2 >> task3
