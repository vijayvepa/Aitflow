from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import  datetime
from math import pow

# Define function for each task

def start_number(**context):
    context["ti"].xcom_push(key='current_value', value=10)
    print("Starting number 10")

def add_five(**context):
    current_value = context['ti'].xcom_pull(key='current_value', task_ids='start_number_task')
    new_value = current_value + 5;
    context["ti"].xcom_push(key='current_value', value=new_value)
    print(f"Add {current_value} + 5 = {new_value}")

def multiply_by_2(**context):
    current_value = context['ti'].xcom_pull(key='current_value', task_ids='add_five_task')
    new_value = current_value * 2;
    context["ti"].xcom_push(key='current_value', value=new_value)
    print(f"Multiply {current_value} by 2 = {new_value}")

def subtract_3_from(**context):
    current_value = context['ti'].xcom_pull(key='current_value', task_ids='multiply_by_2_task')
    new_value = current_value - 3;
    context["ti"].xcom_push(key='current_value', value=new_value)
    print(f"Subtract {current_value} by 2 = {new_value}")


def square_number(**context):
    current_value = context['ti'].xcom_pull(key='current_value', task_ids='subtract_3_from_task')
    new_value = pow(current_value, 2);
    context["ti"].xcom_push(key='current_value', value=new_value)
    print(f"Square {current_value} ^ 2 = {new_value}")

with DAG(
    dag_id = 'math_sequence_dag',
    start_date=datetime(2023,1,1),
    schedule='@once',
    catchup=False
) as dag:
    start_number_task = PythonOperator(task_id='start_number_task', python_callable=start_number)
    add_five_task = PythonOperator(task_id='add_five_task', python_callable=add_five)
    multiply_by_2_task = PythonOperator(task_id='multiply_by_2_task', python_callable=multiply_by_2)
    subtract_3_from_task = PythonOperator(task_id='subtract_3_from_task', python_callable=subtract_3_from)
    square_number_task = PythonOperator(task_id='square_number_task', python_callable=square_number)

    start_number_task >> add_five_task >> multiply_by_2_task >> subtract_3_from_task >> square_number_task




