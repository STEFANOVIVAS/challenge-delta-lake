## Proposed solution for the Challenge.

### Clone this repository

    git clone....

### Build Delta docker image and give it delta_quickstart name.

    docker build . --no-cache -t delta_quickstart

### Run docker image with 3 volumes

    docker run --name delta_quickstart -d -v ./src:/opt/spark/work-dir/src -v ./storage:/opt/spark/work-dir/storage -v ./delta:/opt/spark/work-dir/delta  delta_quickstart

### Changing permissions in the local folder ./delta so we can write files there.

    sudo chmod a+rwx ./delta
    

#### This command gives full permissions for everyone to respective folder. Probably not the safer solution but a think that for a testing project it's ok.
### Quickstart.py test file

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
      .save("./delta/test")
    )
    
    
    df = (spark
            .read
            .format("delta")
            .load("./delta/test")
            
          )
    
    df.show()

### Testing the infrastructure

      docker exec -it delta_quickstart /opt/spark/bin/spark-submit \
      --packages io.delta:delta-spark_2.12:3.0.0
      --master local \
      --deploy-mode client \
      /opt/spark/work-dir/src/quickstart.py

### Test Result

    24/11/15 19:34:20 INFO DAGScheduler: Job 6 is finished. Cancelling potential speculative or zombie tasks for this job
    24/11/15 19:34:20 INFO TaskSchedulerImpl: Killing all running tasks in stage 10: Stage finished
    24/11/15 19:34:20 INFO DAGScheduler: Job 6 finished: showString at <unknown>:0, took 0.146657 s
    24/11/15 19:34:20 INFO CodeGenerator: Code generated in 5.509727 ms
    +---+
    | id|
    +---+
    |  0|
    |  1|
    |  2|
    |  3|
    |  4|
    +---+
    
    24/11/15 19:34:21 INFO SparkContext: Invoking stop() from shutdown hook
    24/11/15 19:34:21 INFO SparkContext: SparkContext is stopping with exitCode 0.
    24/11/15 19:34:21 INFO SparkUI: Stopped Spark web UI at http://68c4d03d5a70:4040
    24/11/15 19:34:21 INFO MapOutputTrackerMasterEndpoint: MapOutputTrackerMasterEndpoint stopped!
    24/11/15 19:34:21 INFO MemoryStore: MemoryStore cleared
