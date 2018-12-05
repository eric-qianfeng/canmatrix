import sys
import shlex
import csv

def quote_aware_space_split(inLine):
    if sys.version_info >= (3, 0):  # is there a clean way to to it?
        return shlex.split(inLine.strip())
    else:
        tempArray = shlex.split(inLine.strip().encode('utf-8'))
        newArray = []
        for item in tempArray:
            newArray.append(item.decode('utf-8'))
        return newArray


def quote_aware_comma_split(string):
    if sys.version_info >= (3, 0):  # is there a clean way to to it?
        temp = list(csv.reader([string], skipinitialspace=True))
    else:
        temp = list(csv.reader([string.encode("utf8")], skipinitialspace=True))
    return temp[0]
