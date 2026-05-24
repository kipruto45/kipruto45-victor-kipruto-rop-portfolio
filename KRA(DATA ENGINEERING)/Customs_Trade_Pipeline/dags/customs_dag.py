from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'kra_customs_trade_pipeline',
    default_args=default_args,
    description='KRA Customs & Trade Intelligence ETL',
    schedule_interval='30 10 * * *',
    catchup=False,
) as dag:

    generate_data = BashOperator(
        task_id='generate_customs_data',
        bash_command='python3 /opt/airflow/projects/kra/Customs_Trade_Pipeline/ingestion/generate_customs_data.py',
    )

    load_data = BashOperator(
        task_id='load_customs_to_postgres',
        bash_command='python3 /opt/airflow/projects/kra/Customs_Trade_Pipeline/ingestion/load_customs_data.py',
    )

    dbt_run = BashOperator(
        task_id='dbt_run_customs',
        bash_command='cd /opt/airflow/projects/kra/Customs_Trade_Pipeline/dbt && dbt run --profiles-dir .',
    )

    generate_data >> load_data >> dbt_run
