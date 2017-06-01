import sys
import json
from collections import Counter

array = '{"values": [12, 13, 14, 14]}'

def train():
    """Does de average of the given data"""
    print("Train")
    data  = json.loads(array)
    numbers = data['values']
    numbers_sum = sum(numbers) / len(numbers)
    print(numbers_sum)

def test():
    """Does the modus of the datas given (for the tests)"""
    print("Test")
    data  = json.loads(array)
    numbers = data['values']
    data = Counter(numbers)
    mode = data.most_common(1)
    print("Mode : ", mode)

def main(argv):
    """Documentation can be placed here, but not in the __name__ function"""
    if argv[0] == "train":
        train()
    elif argv[0] == "test":
        test()

if __name__ == "__main__":
    main(sys.argv[1:])
