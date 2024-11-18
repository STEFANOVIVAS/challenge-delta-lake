from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession
from delta import *
from pyspark.sql.functions import col


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

# Create a Spark DataFrame

df = (spark
        .read
        .format("delta")
        .load("./delta/bronze/movies")
        
      )
df.columns
