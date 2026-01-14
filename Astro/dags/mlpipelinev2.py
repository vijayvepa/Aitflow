
from airflow.sdk import Asset, dag, task
from pendulum import datetime
import requests


dag(dag_id='ml_pipeline_v2' ,start_date=datetime(2026,1,14),schedule='@weekly')
def ml_pipeline_v2():

    @task(outlets=[])
    def preprocess():
        print('preprocessing data')

    @task(outlets=[])
    def load():
        print('loading data')

ml_pipeline_v2()