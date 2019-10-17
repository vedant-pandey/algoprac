# To check if the string entered has all unique characters
from collections import defaultdict as d

def checkUnique() :
    s        : str  = input()
    chardict : d    = d(int)

    for char in s :
        if (chardict[char]) :
            return False
        chardict[char] = 1
    return True

if __name__ == "__main__":
    print(checkUnique())