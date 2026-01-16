from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def preprocess_data():
    print("Preprocessing data..")

def train_model():
    print("Training model")

def evaluate_model():
    print("Evaluate model")

with DAG(
    'ml_pipeline',
    start_date=datetime(2026,1,14),
    schedule='@weekly'
) as dag:

    preprocess = PythonOperator(task_id='preprocess', python_callable=preprocess_data)
    train = PythonOperator(task_id='train', python_callable=train_model)
    evaluate = PythonOperator(task_id='evaluate', python_callable=evaluate_model)

    preprocess >> train >> evaluate
