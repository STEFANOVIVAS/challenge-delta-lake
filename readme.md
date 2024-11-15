## Proposed solution for the Challenge.

### Clone this repository

    git clone....

### Build Delta docker image and give it delta_quickstart name.

    docker build . --no-cache -t delta_quickstart

### Run docker image with 3 volumes

    docker run --name delta_quickstart -d -v ./src:/opt/spark/work-dir/src -v ./storage:/opt/spark/work-dir/storage -v ./delta:/opt/spark/work-dir/delta  delta_quickstart
