def main() :
  s1 = input()
  s2 = input()
  
  if abs(len(s1) - len(s2)) > 1 :
    return False
  
  flag = False

  if len(s1) > len(s2) :
  
    for i in range(len(s2)) :
      if not (s1[i] == s2[i]) :
        return False

  elif len(s1) < len(s2) :
  
    for i in range(len(s1)) :
      if not (s1[i] == s2[i]) :
        return False
  
  else :

    for i in range(len(s1)) :
  
      if not (s1[i] == s2[i]) :
  
        if flag :
          return False
        flag = True

  return True

if __name__ == "__main__" :
    print(main())