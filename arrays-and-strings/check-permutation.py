from collections import defaultdict

def main() :
    s1 = input()
    s2 = input()

    checkDict = defaultdict(int)

    if not (len(s1) == len(s2)):
        return False

    for char in s1:
        checkDict[char] += 1
    
    for char in s2:
        checkDict[char] -= 1
        if (checkDict[char] < 0):
            return False
    return True

if __name__ == "__main__":
    print(main())