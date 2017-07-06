import sys
import json
import database_connector
import numpy as np
from tpot import TPOTRegressor
from deap import creator
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

volume_folder = '/docker-volume/'
input_training_file = 'input_training.json'
input_test_file =  'input_test.json'

def train():
    """Does de average of the given data"""
    try:
        print("Train")

        input_training_file =  'input_training.json'
        output_file = input_test_file

        try:
            # Reading from the JSON input file
            with open(volume_folder + input_training_file) as data_file:
                print("Opening succeed")
                data = json.load(data_file)
                print(data)
        except:
            print("ERROR while training, this might be because $HOME/docker-volume doesn't contain the input file as", input_file)

        # Query retrieving and DB query
        query_features = data['query_features']
        query_targets = data['query_targets']

        results_features = database_connector.fetch_data(query_features)
        results_target = database_connector.fetch_data(query_targets)

        print(type(results_target["data"]))

        # Converting to np arrays, for TPOT
        X = np.asarray(results_features["data"])
        y = np.ravel(np.asarray(results_target["data"]))

        X_train, X_test, y_train, y_test = train_test_split(X,y, random_state = 42)

        # print("len // X_train :", len(X_train), "Y_train:", len(y_train))
        # print("len // X_test :", len(X_test), "Y_test:", len(y_test))
        # print("===TRAIN===")
        # print("Features: ",X_test)
        # print("Targets: ", y_test)
        # print("===TEST===")
        # print("Features: ",X_test)
        # print("Targets: ", y_test)

        tpot = TPOTRegressor(generations=1, population_size=50, verbosity=2)

        tpot.fit(X_train, y_train)
        best_pipeline = tpot._optimized_pipeline
        pipeline_str = list(best_pipeline)[0]

        print(volume_folder + output_file)

        output = {"query_features" : query_features, "query_targets" : query_targets, "pipeline" : str(best_pipeline)}

        with open(volume_folder + output_file, 'w') as outfile:
            outfile.write(json.dumps(output, ensure_ascii=False))
    except:
        sys.exit(100)


def test():
    try:
        """Does the modus of the datas given (for the tests)"""
        # Output format still to choose
        output_file = 'predicates.txt'

        with open(volume_folder + input_test_file) as data_file:
            data = json.load(data_file)

        pipeline = data['pipeline']

        # This query assumes that the set is already split for test predicates
        query_features = data['query_features']
        query_targets = data['query_targets']

        print(query_features)
        print(query_targets)

        results_features = database_connector.fetch_data(query_features)
        results_targets = database_connector.fetch_data(query_targets)

        # Converting to np arrays, for TPOT
        X = np.asarray(results_features["data"])
        y = np.ravel(np.asarray(results_targets["data"]))

        X_train, X_test, y_train, y_test = train_test_split(X,y, random_state = 42)

        # print("len // X_train :", len(X_train), "Y_train:", len(y_train))
        # print("len // X_test :", len(X_test), "Y_test:", len(y_test))
        # print("===TRAIN===")
        # print("Features: ",X_test)
        # print("Targets: ", y_test)
        # print("===TEST===")
        # print("Features: ",X_test)
        # print("Targets: ", y_test)

        # convert pipeline string to scikit-learn pipeline object
        tpot = TPOTRegressor(generations=1, population_size=50, verbosity=2)
        optimized_pipeline = creator.Individual.from_string(pipeline, tpot._pset) # deap object
        pipeline = tpot._toolbox.compile(expr=optimized_pipeline)

        fitted_pipeline = pipeline.fit(X_train, y_train)

        # print scikit-learn pipeline objectP
        print("Chosen Pipeline :", fitted_pipeline, "\n")

        scores = fitted_pipeline.predict(X_test)

        print("scores : ", scores)

        with open(volume_folder + output_file, 'w') as outfile:
            outfile.write(str(scores))
    except:
        sys.exit(100)

def main(argv):
    """Documentation can be placed here, but not in the __name__ function"""
    if argv[0] == "train":
        train()
    elif argv[0] == "test":
        test()

if __name__ == "__main__":
    main(sys.argv[1:])
