import sys
import json
from collections import Counter

input_file = '/docker-volume/data.json'
output_file = '/docker-volume/out.json'

def train():
    """Does de average of the given data"""
    print("Train")
    # data  = json.loads(array)
    with open(input_file) as data_file:
        data = json.load(data_file)

    print("read from file")

    numbers = data['values']
    numbers_sum = sum(numbers) / len(numbers)

    with open(output_file, 'w') as outfile:
        outfile.write(str(numbers_sum))

    print(numbers_sum)

def test():
    """Does the modus of the datas given (for the tests)"""
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
