import pyspark
from delta import *

builder = pyspark.sql.SparkSession.builder.appName("init-dt") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

# show configured parameters
print(SparkConf().getAll())

# set log level
spark.sparkContext.setLogLevel("INFO")