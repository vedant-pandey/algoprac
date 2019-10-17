class ComplexQueue :

  """A queue containing two inner queues"""

  queue_dog : list
  queue_cat : list
  cur_queue : list

  def __init__(self) :
    self.queue_dog = []
    self.queue_cat = []
    self.cur_queue = None
  
  def enqueue(self, ani_name, ani_type) :
    if ani_type == 0 :
      self.queue_dog.append(ani_name)
      self.cur_queue.append(0)
    else :
      self.queue_cat.append(ani_name)
      self.cur_queue.append(1)

  def dequeue_any(self) :
    if self.cur_queue[-1] == 0 :
      self.cur_queue.pop()
      return self.queue_dog.pop()
    else :
      self.cur_queue.pop()
      return self.queue_dog.pop()

  def dequeue_dog(self) :
    
    self.cur_queue.reverse()
    try :
      self.cur_queue.remove(0)
    except :
      pass
    self.cur_queue.reverse()

    return self.queue_dog.pop()


  def dequeue_cat(self) :

    self.cur_queue.reverse()
    try :
      self.cur_queue.remove(1)
    except :
      pass
    self.cur_queue.reverse()

    return self.queue_cat.pop()