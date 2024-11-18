from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession
from delta import *
from pyspark.sql.functions import col,current_timestamp,expr,lit


builder = (
        SparkSession.builder
        .appName("pytest-pyspark-local-testing")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
)

spark = configure_spark_with_delta_pip(builder).getOrCreate()

sources=['movies','subscription','ratings','user']

def ingestion_bronze(source_name):
    df = (spark
        .read
        .format("json")
        .load(f"./storage/files/landing/{source_name}/*.json")
        
      )
    df_metadata=df.withColumn("ingestion_timestamp",current_timestamp()).withColumn("source",lit(f"{source_name}"))
    df_metadata.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(f"./delta/bronze/{source_name}")
    df_metadata.show()

for source_name in sources:
    ingestion_bronze(source_name)