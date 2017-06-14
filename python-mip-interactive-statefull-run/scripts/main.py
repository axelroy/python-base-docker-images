import sys
import json
from collections import Counter
import database_connector

volume_folder = '/docker-volume/'

def train():
    """Does de average of the given data"""
    print("Train")

    input_file =  'input_training.json'
    output_file = 'training_result.txt'

    try:
        # Reading from the JSON input file
        with open(volume_folder + input_file) as data_file:
            data = json.load(data_file)

            type = data['type']

            if (type == "training"):
                numbers = data['values']
                numbers_sum = sum(numbers) / len(numbers)
                print(numbers_sum)

                # Output results
                with open(volume_folder + output_file, 'w') as outfile:
                    outfile.write(str(numbers_sum))
            else:
                print("Bad input format for ", input_file, "not set as training mode.")
    except:
        print("ERROR : Unable to open file ", input_file, ". Does it exists?")

    print("database tests : ")

    query = data['query']
    print(query)
    result = database_connector.fetch_data(query)
    print(result)

def test():
    """Does the modus of the datas given (for the tests)"""

    input_file =  'input_test.json'
    output_file = 'predicates.txt'

    print("Test")
    # try:
    with open(volume_folder + input_file) as data_file:
        data = json.load(data_file)

    type = data['type']

    if (type == "test"):
        print("read from file")
        numbers = data['values']
        data = Counter(numbers)
        mode = data.most_common(1)

        with open(volume_folder + output_file, 'w') as outfile:
            outfile.write(str(mode))

        print("Mode : ", mode)
    else:
        print("Bad input format for ", input_file, "not set as test mode.")
    # except:
    #     print("ERROR : Unable to open file ", input_file, ". Does it exists?")

def main(argv):
    """Documentation can be placed here, but not in the __name__ function"""
    if argv[0] == "train":
        train()
    elif argv[0] == "test":
        test()

if __name__ == "__main__":
    main(sys.argv[1:])
