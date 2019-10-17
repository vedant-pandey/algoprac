from collections import defaultdict

def main():
    s = input().replace(' ','')
    checkPalDict = defaultdict(int)
    flag = False
    for c in s :
        checkPalDict[c] +=1
    for k,v in checkPalDict.items():
        if (not (v % 2 == 0)) and (flag):
            return False
        if (not (v % 2 == 0)) and (not flag):
            flag = True
    return True

if __name__ == "__main__":
    print(main())