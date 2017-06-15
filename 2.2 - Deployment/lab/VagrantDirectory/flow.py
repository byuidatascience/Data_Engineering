# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
from airflow.operators import EmailOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2017, 3, 29),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    'end_date': datetime(2016, 3, 31)
}

    dag = DAG(
        'once_hour', default_args=default_args, schedule_interval="0 * * * *"
    )
    # the schedule interval for the dag here is one day

    t1 = EmailOperator(
        to='2check91@gmail.com',
        subject='Generic Subject')
