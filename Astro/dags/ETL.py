from airflow import DAG
from airflow.providers.http.operators.http import HttpOperator
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils import timezone
from datetime import timedelta
## create table if not exists
## extract NASA api data - Astronomy Picture of Day
## transform the data
## load data into postgres
## verify with DBViewer
## Define task deps

with DAG(
    dag_id='NASA-Astronomy-Picture-of-Day',
    start_date=timezone.utcnow() - timedelta(days=7),
    schedule='@daily',
    catchup=False
) as dag:
    @task
    def create_table():
        postgres_hook = PostgresHook(postgres_conn_id="my_postgres_connection")
        create_table_query = """
            CREATE TABLE IF NOT EXISTS apod_data(
                id SERIAL PRIMARY KEY,
                title VARCHAR(255),
                explanation TEXT, 
                url TEXT,
                date DATE,
                media_type VARCHAR(50)
            );
        """
        postgres_hook.run(create_table_query)

    extract_apod = HttpOperator(
        task_id='extract_apod',
        http_conn_id='nasa_api', #connection id for nasa api
        endpoint='planetary/apod',
        method='GET',
        data={"api_key":"{{ conn.nasa_api.extra_dejson.api_key }}"}, # use api key from conn
        response_filter=lambda response:response.json(), # convert response to json
    )

    @task
    def transform_apod_data(response):
        apod_data = {
            'title': response.get('title', ''),
            'explanation': response.get('explanation', ''),
            'url': response.get('url', ''),
            'date': response.get('date', ''),
            'media_type': response.get('media_type', '')
        }
        return apod_data

    @task
    def load_into_postgres(apod_data):
        postgres_hook = PostgresHook(postgres_conn_id="my_postgres_connection")
        sql_insert_query="""
            INSERT INTO apod_data(title, explanation, url, date, media_type)
            VALUES (%s, %s, %s, %s, %s);
        """
        postgres_hook.run(sql_insert_query, parameters=(
            apod_data['title'],
            apod_data['explanation'],
            apod_data['url'],
            apod_data['date'],
            apod_data['media_type']
        ))

    ## DAG flow
    create_table() >> extract_apod
    api_response = extract_apod.output
    transformed_data = transform_apod_data(api_response)
    load_into_postgres(transformed_data)

