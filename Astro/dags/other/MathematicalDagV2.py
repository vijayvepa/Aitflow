from airflow import DAG
from airflow.decorators import task
from datetime import datetime

from airflow.example_dags.example_dynamic_task_mapping import added_values

with DAG(
    dag_id='MathSequenceV2',
    start_date=datetime(2023,1,1),
    schedule='@once',
    catchup=False
) as dag:

    @task
    def start_number():
        initial_value = 10
        print(f"Starting number: {initial_value}")
        return initial_value

    @task
    def add_five(number):
        new_value = number + 5
        print(f"Multiply by 2: {number} * 2 = {new_value}")
        return new_value

    @task
    def subtract_three(number):
        new_value = number - 3
        print(f"Subtract 3: {number} - 3  = {new_value}")
        return new_value

    start_value = start_number()
    added_value = add_five(start_value)
    subtracted_value = subtract_three(added_value)



