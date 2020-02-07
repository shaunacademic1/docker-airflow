from airflow.models import Variable

START_DATE = Variable.get('SECRET__START_DATE')
