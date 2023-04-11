from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from datetime import datetime

dag = DAG(
    'dagrundag1',
    description="Dag run dag",
    schedule_interval=None,
    start_date=datetime(2023, 4, 5),
    catchup=False,
)

task1 = BashOperator(task_id="tks1", bash_command="sleep 5", dag=dag)
task2 = TriggerDagRunOperator(
    task_id="tks2", trigger_dag_id="dagrundag2", dag=dag)

task1 >> task2
