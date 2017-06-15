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

There's two version of the interactive container at the moment, the statefull run stops between each `docker run`
command, but the input files shared with the `docker-volume` and the entrypoints make the functionnalities differ.

The activewait version is runned, stays alive and then wait for an `docker exec`command to do training or test function.
We have both version because we don't know what we will be able to use with our scala/AKKA backend. 

First will be explored the interaction with Marathon, but it might be possible to create a Scala to docker direct communication. 

TODO : Clean when the good option will be determined.

### For the python-mip-interactive-statefull-run container :

This version works by doing two `docker run` commands. The method called is passed by entrypoint,
but the work to do is 

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

### For the python-mip-interactive-activewait Container :

Allows to start a Docker container, which can be run without doing any job, and stay listening to the next exec commands the user do.

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
