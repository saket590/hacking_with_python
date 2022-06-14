from itertools import permutations
from itertools import combinations
import argparse

parser = argparse.ArgumentParser(
        description='This Programme try to create a list of password from entered word.')
parser.add_argument('--minLength', help='minimum length of password', default=3)
parser.add_argument('--maxLength', help='Maximum length of password', default=16)
parser.add_argument('--initList', help='Path to the initial word list', default="")
args = parser.parse_args()


input_words = []
output_words = []


if args.initList != "":
    f = open(args.initList, "r")
    for x in f:
        x = x.rstrip()
        input_words.append(x)
else:
    print("input your words and then for finishing enter @finish@")
    while 1:
        inp = input()
        if inp.__eq__("@finish@"):
            break
        else:
            input_words.append(inp)

for i in range(0, input_words.__len__()):
    comb = combinations(input_words, i + 1)
    for wordSet in list(comb):
        passLength = 0
        for j in wordSet:
            passLength += len(j)
        if args.minLength <= passLength <= args.maxLength:
            perm = permutations(wordSet)
        for j in list(perm):
            result = ""
            for k in range(0, j.__len__()):
                result += j[k]
            output_words.append(result)

with open("output.txt", "w") as txt_file:
    for line in output_words:
        txt_file.write("".join(line) + "\n")

print("total " + str(len(output_words)) + " password generated!!!")
