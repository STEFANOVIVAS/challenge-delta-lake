from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession
from delta import *



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
data = spark.range(0, 5)


(data
  .write
  .format("delta")
  .save("./delta")
)


# df = (spark
#         .read
#         .format("delta")
#         .load("./storage/delta-table")
        
#       )

# df.show()


# Write to a Delta Lake table
# (data
#    .write
#    .format("delta")
#    .save("./delta/delta-table")
# )

# Read from the Delta Lake table
# df = (spark
#         .read
#         .format("delta")
#         .load("./storage/delta-table")
        
#       )

# Show the Delta Lake table
# df.show()