from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(dag_id = "dag_with_statement") as dag:
    task_1 = EmptyOperator(
        task_id = "task_ke_1",
    )

    task_1