# # import re
# import json
#
#
# def iter_json(json_str):
#     for majorkey, subdict in json_str.items():
#         print(majorkey)
#         for subkey, value in subdict.items():
#             print(subkey, value)
#
# total_sum = 0
#
# with open('input12.txt', 'r') as f:
#
#     '''for line in f:
#         nums = re.compile(r"[+-]?\d+(?:\.\d+)?")
#         for n in nums.findall(line):
#             total_sum += int(n)'''
#
# # print(total_sum)
#     for line in f:
#         iter_json(json.loads(line))
#
#

import re
import json

# TODO Needs refactoring ([generator](https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/))
# [Interesting article to read](http://compiletoi.net/garcon-theres-a-catamorphism-in-my-python.html)
def get_obj(obj, value=None, lst=[]):
    """ Returns a list with all the objects with value
    """

    if isinstance(obj, dict):
        if value not in obj.values():
            for v in obj.values():
                if isinstance(v, dict) or isinstance(v, list):
                    get_obj(v, value = value, lst = lst)
        else:
            lst.append(obj)
    elif isinstance(obj, list):
        for v in obj:
            if isinstance(v, dict) or isinstance(v, list):
                get_obj(v, value = value, lst = lst)


    return lst


if __name__ == "__main__":

    with open("input12.txt") as f:

        lines = f.readlines()

        for i, line in enumerate(lines):

            ln = line.strip('\n')

            if not ln:
                continue

            # Find all numbers in the format -12.345
            l = re.findall("-?\d+(?:\.\d+)?", ln)

            # Convert to int
            l = [int(i) for i in l]

            print('1. What is the sum of all numbers in the document? %d' % sum(l))

            # Load json in python data structures
            j = json.loads(ln)

            # Find all the objects with value red
            ln_red = get_obj(j, value='red', lst=[])

            #print ln_red, len(ln_red)
            ln_red = json.dumps(ln_red)

            l_red = re.findall("-?\d+(?:\.\d+)?", ln_red)

            l_red = [int(i) for i in l_red]

            print('2. Find the sum ignoring any object (and all of its children) which has any property with the value "red": %d' % (sum(l) - sum(l_red)))