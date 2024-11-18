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

df_subscription = (spark
        .read
        .format("json")
        .load("./storage/files/landing/subscription/*.json")
        
      )

df_subscription_column_renamed=df_subscription.withColumnRenamed("id","subscription_id")\
.withColumnRenamed("payment_method","subscription_payment_method")\
.withColumnRenamed("payment_term","subscription_payment_term")\
.withColumnRenamed("plan","subscription_plan")\
.withColumnRenamed("status","subscription_status")\


df_subscription_column_renamed.select(col("subscription_id"),col("uid"),col("user_id"),\
                                      col("subscription_plan"),col("subscription_status"),\
                                      col("subscription_payment_method"),col("subscription_payment_term"),\
                                      col("dt_current_timestamp")).show()