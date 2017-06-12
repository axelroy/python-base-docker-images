import sys
import json
from collections import Counter
import database_connector

input_file = '/docker-volume/data.json'
output_file = '/docker-volume/out.json'

def train():
    """Does de average of the given data."""
    print("Train")

    try:
        with open(input_file) as data_file:
            data = json.load(data_file)
            numbers = data['values']
            numbers_sum = sum(numbers) / len(numbers)
    except:
        print("ERROR : Unable to open file ", input_file, ". Does it exists?")

    try:
        with open(output_file, 'w') as outfile:
            outfile.write(str(numbers_sum))
    except:
        print("ERROR : Unable to open file ", input_file, ". Does it exists?")

    print(numbers_sum)
    print("database tests : ")

    query = data['query']
    database_connector.fetch_data(query)

def test():
    """Does the modus of the datas given (for the tests)."""
    print("Test")
    with open('/docker-volume/data.json') as data_file:
        data = json.load(data_file)

    print("read from file")
    numbers = data['values']
    data = Counter(numbers)
    mode = data.most_common(1)

    with open(output_file, 'w') as outfile:
        outfile.write(str(mode))
    print("Mode : ", mode)

def main(argv):
    """Documentation can be placed here, but not in the __name__ function"""
    if argv[0] == "train":
        train()
    elif argv[0] == "test":
        test()

if __name__ == "__main__":
    main(sys.argv[1:])
