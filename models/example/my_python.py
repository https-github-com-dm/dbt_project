import sys
from pyspark.sql import SparkSession


def model(dbt, session):
        dbt.config(
            #submission_method="cluster",
            #dataproc_cluster_name="dbt-cluster",
            #gcs_bucket="bkt-dmgcp-del-ce-temp",
            #dataproc_region="us-central1",
            materialized = 'table',
            packages = ['pandas', 'bigquery']
        )
        
        my_sql_model_df = dbt.ref("my_first_dbt_model")
        
        return my_sql_model_df
