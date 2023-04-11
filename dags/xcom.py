from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

dag = DAG(
    'dagxcom',
    description='Dag Xcom',
    schedule_interval=None,
    start_date=datetime(2023, 4, 10),
    catchup=False
)


def task_write(**kwarg):
    kwarg['ti'].xcom_push(key='valorxcom1', value="Hello, word!")


task1 = PythonOperator(task_id='tks1', python_callable=task_write, dag=dag)


def task_read(**kwarg):
    valor = kwarg['ti'].xcom_pull(key='valorxcom1')
    print(f"Valor recuperado: {valor}")


task2 = PythonOperator(task_id='tks2', python_callable=task_read, dag=dag)

task1 >> task2
