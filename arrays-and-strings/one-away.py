def main():
  s1 = input()
  s2 = input()
  if abs(len(s1) - len(s2)) > 1 :
    return False
  flag = False
  if len(s1) > len(s2) :
    for c in s1 :
      if (c not in s2) :
        if flag :
          return False
        else :
          flag = True
    return True
  else :
    for c in s2 :
      if (c not in s1) :
        if flag :
          return False
        else :
          flag = True
    return True

if __name__ == "__main__":
    print(main())