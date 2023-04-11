from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


dag = DAG(
    'terceira_dag',
    description="Nossa terceira DAG",
    schedule_interval=None,
    start_date=datetime(2023, 4, 5),
    catchup=False,
)

task1 = BashOperator(task_id="tks1", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="tks2", bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id="tks3", bash_command="sleep 5", dag=dag)

[task1, task2] >> task3
