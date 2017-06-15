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


## Usage for the interactive version


Functionnalities :

Allows to start a Docker container, which can be run without doing any job, and stay listening to the next exec commands the user do.

Input & output not documented yet, will be done in the fully fonctionnal version.

Basic usage for demo.

launch :

TODO : Clean when the good option will be determined.

For the python-mip-interactive-statefull-run container :

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
hbpmip/python-mip-interactive-statefull-run \
train`


HARD-CODE IP docker0's interface is evil, to be fixed when integrated with Woken.

For the python-mip-interactive-activewait Container :
=============================

`docker run \
--init  \
--name python-mip-interactive-activewait \
-v ${HOME}/docker-volume/:/docker-volume \
--env IN_JDBC_URL="jdbc:postgresql://172.17.0.1:65432/postgres" \
--env IN_JDBC_USER="postgres" \
--env IN_JDBC_PASSWORD="test" \
--env OUT_JDBC_URL="jdbc:postgresql://172.17.0.1:5432/postgres" \
--env  OUT_JDBC_USER="postgres" \
--env  OUT_JDBC_PASSWORD="test" \
--env PARAM_meta="{}" \
hbpmip/python-mip-interactive-activewait \
init`

And in another command line :

`docker exec python-mip-interactive-activewait python /main.py train`
or
`docker exec python-mip-interactive-activewait python /main.py test`

and to stop :
`docker stop python-mip-interactive-activewait`
`docker rm python-mip-interactive-activewait`


### interactive inputs

example of input file format at the moment. It's not the final version!

`{
"type" : "training",
"values": [12, 13, 14, 14],
"query" : "SELECT score_test1 from linreg_sample;"
}`
