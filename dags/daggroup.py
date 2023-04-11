from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime


dag = DAG(
    'dag_group', description="TaskGroup",
    schedule_interval=None, start_date=datetime(2023, 4, 5),
    catchup=False
)

task1 = BashOperator(task_id="tks1", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="tks2", bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id="tks3", bash_command="sleep 5", dag=dag)
task4 = BashOperator(task_id="tks4", bash_command="sleep 5", dag=dag)
task5 = BashOperator(task_id="tks5", bash_command="sleep 5", dag=dag)
task6 = BashOperator(task_id="tks6", bash_command="sleep 5", dag=dag)

tks_group = TaskGroup("tks_group", dag=dag)

task7 = BashOperator(task_id="tks7", bash_command="sleep 5",
                    dag=dag, task_group=tks_group)
task8 = BashOperator(task_id="tks8", bash_command="sleep 5",
                    dag=dag, task_group=tks_group)
task9 = BashOperator(
    task_id="tks9", bash_command="sleep 5", dag=dag, task_group=tks_group
)


task1 >> task2
task3 >> task4
[task2, task4] >> task5 >> task6
task6 >> [tks_group]
