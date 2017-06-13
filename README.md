# Python Base Docker Images

## What is it ?

This is a collection of Docker images for Python.

## Images

* python-base : Python 3 (includes Conda)
* python-mip : python-base + psycopg2 + custom library to access MIP databases
* python-mip-interactive : python-mip + statefull container, which can be interacted after running (still under development)

## Usage for the interactive version


Functionnalities :

Allows to start a Docker container, which can be run without doing any job, and stay listening to the next exec commands the user do.

Input & output not documented yet, will be done in the fully fonctionnal version.

Basic usage for demo.

launch :

TODO : Clean when the good option will be determined.
`docker run --rm --init --name python-mip-interactive -v  /home/utilisateur/docker-volume/:/docker-volume --env IN_JDBC_URL="jdbc:postgresql://"${HOST}":5432/postgres" --env --env --env IN_JDBC_USER="postgres" --env IN_JDBC_PASSWORD="test" --env OUT_JDBC_URL="jdbc:postgresql://"${HOST}":5432/postgres" --env  OUT_JDBC_USER="postgres" --env  OUT_JDBC_PASSWORD="test" --env PARAM_meta="{}" hbpmip/python-mip-interactive-statefull-run train`


ENV
ENV
ENV

ENV
ENV
ENV



And in another command line :

`docker exec python-mip-interactive python /main.py train`

or

`docker exec python-mip-interactive python /main.py test`


and to stop :
`docker stop python-mip-interactive`

### Build

Run: `./build.sh`

### Integrate a new algorithm

1. Add `import database_connector` in your Python script;
2. Call `database_connector.fetch_data()` to get the input data;
3. Call `database_connector.save_results(pfa, error, shape)` to store the results.

For more information, have a look at the library documentation.
