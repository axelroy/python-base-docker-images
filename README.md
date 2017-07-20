# Python Base Docker Images

## What is it ?

This is a collection of Docker images for Python.

## Images

* python-base : Python 3 (includes Conda)
* python-mip : python-base + psycopg2 + custom library to access MIP databases
* python-mip-interactive : python-mip + statefull container, which can be interacted after running (still under development)


### Build

Run: `./build.sh`

### Integrate a new algorithm

1. Add `import database_connector` in your Python script;
2. Call `database_connector.fetch_data()` to get the input data;
3. Call `database_connector.save_results(pfa, error, shape)` to store the results.

For more information, have a look at the library documentation.

## Usage for the python-mip-interactive

This version works by doing two `docker run` commands. The method called is passed by `entrypoint`,
but the work to do is :

`docker run \
--rm \
--name python-mip-interactive-statefull-run \
-v ${HOME}/docker-volume/:/docker-volume \
--env IN_JDBC_URL="jdbc:postgresql://172.17.0.1:65432/postgres" \
--env IN_JDBC_USER="postgres" \
--env IN_JDBC_PASSWORD="test" \
--env OUT_JDBC_URL="jdbc:postgresql://172.17.0.1:5432/postgres" \
--env  OUT_JDBC_USER="postgres" \
--env  OUT_JDBC_PASSWORD="test" \
--env PARAM_meta="{}" \
hbpmip/python-mip-interactive \
train`

or

`docker run \
--rm \
--name python-mip-interactive-statefull-run \
-v ${HOME}/docker-volume/:/docker-volume \
--env IN_JDBC_URL="jdbc:postgresql://172.17.0.1:65432/postgres" \
--env IN_JDBC_USER="postgres" \
--env IN_JDBC_PASSWORD="test" \
--env OUT_JDBC_URL="jdbc:postgresql://172.17.0.1:5432/postgres" \
--env  OUT_JDBC_USER="postgres" \
--env  OUT_JDBC_PASSWORD="test" \
--env PARAM_meta="{}" \
hbpmip/python-mip-interactive \
test`


HARD-CODE IP docker0's interface is evil, to be fixed when integrated into Woken.

## interactive inputs

example of input file format at the moment.

### Training inputs :

filename - input_training.json

Content :

`{
  "query_features": "SELECT score_test1, stress_before_test1  from linreg_sample;",
  "query_targets": "SELECT score_math_course1 from linreg_sample;"
}`

### Test inputs :

This file is automaticaly generated in the Docker Volume passed in arguments when launched in training mode.

filename - input_test.jsons

Content :

`{
  "query_features": "SELECT score_test1, stress_before_test1  from linreg_sample;",
  "query_targets": "SELECT score_math_course1 from linreg_sample;"
  "pipeline": "KNeighborsRegressor(input_matrix, KNeighborsRegressor__n_neighbors=89, KNeighborsRegressor__p=DEFAULT, KNeighborsRegressor__weights=uniform)",
}`
