import sys
import json
from collections import Counter
import database_connector

docker_volume = '/docker-volume/'

def train():
    """Does de average of the given data."""
    print("Train")

    input_file =  'input_training.json'
    output_file = 'training_result.txt'

    try:
        with open(docker_volume + input_file) as data_file:
            data = json.load(data_file)
            numbers = data['values']
            numbers_sum = sum(numbers) / len(numbers)
            print(numbers_sum)

            with open(output_file, 'w') as outfile:
                outfile.write(str(numbers_sum))

            print("database tests : ")

            query = data['query']
            results = database_connector.fetch_data(query)
            print(results)
    except:
        print("ERROR : Unable to open file ", input_file, ". Does it exists?")

def test():
    """Does the modus of the datas given (for the tests)."""
    print("Test")

    input_file =  'input_test.json'
    output_file = 'predicates.txt'

    try:
        with open(docker_volume + input_file) as data_file:
            data = json.load(data_file)

        print("read from file")
        numbers = data['values']
        data = Counter(numbers)
        mode = data.most_common(1)

        with open(output_file, 'w') as outfile:
            outfile.write(str(mode))
        print("Mode : ", mode)

    except:
        print("ERROR : Unable to open file ", input_file, ". Does it exists?")

def main(argv):
    """Documentation can be placed here, but not in the __name__ \"function\""""
    if argv[0] == "train":
        train()
    elif argv[0] == "test":
        test()

if __name__ == "__main__":
    main(sys.argv[1:])
