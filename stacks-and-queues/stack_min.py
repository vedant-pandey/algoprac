class StackWithMin:
  
  def __init__(self) :
    self.stack = []
  
  def push(self, value) :
    if not len(self.stack):
      self.stack.append([value,value])
    curmin = self.stack[len(self.stack) - 1][1]
    newmin = value if curmin > value else curmin
    self.stack.append([value, newmin])
    return value
  
  def pop(self) :
    lastval = self.stack[len(self.stack) - 1][0]
    self.stack.pop()
    return lastval
  
  def get_min(self) :
    return self.stack[len(self.stack) - 1][1]

if __name__ == "__main__":
  swm = StackWithMin()
  print(swm.push(9))
  print(swm.push(2))
  print(swm.push(6))
  print(swm.push(4))
  print(swm.push(3))
  print(swm.push(1))
  print(swm.push(100))
  print(swm.get_min())
  swm.pop()
  swm.pop()
  print(swm.get_min())