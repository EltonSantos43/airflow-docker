from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 5),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'quarta_dag',
    default_args=default_args,
    description='Exemplo de DAG no Apache Airflow',
    schedule_interval=None
)

t1 = BashOperator(
    task_id='tarefa1',
    bash_command='echo "Executando a tarefa 1"',
    dag=dag
)

t2 = BashOperator(
    task_id='tarefa2',
    bash_command='echo "Executando a tarefa 2"',
    dag=dag
)

t3 = BashOperator(
    task_id='tarefa3',
    bash_command='echo "Executando a tarefa 3"',
    dag=dag
)

t1 >> t2 >> t3
