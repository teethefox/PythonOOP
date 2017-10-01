class Call(object):
  def __init__(self, id, num, name, number, time, reason):
    self.id=id
    self.num = num
    self.name = name
    self.number = number
    self.time = time
    self.reason = reason
  def display(self):
    print self.name
    print self.number 
    print self.time 
    print self.reason
call1 = Call("1","21", "lester", "1234566", "2:30", "sad")
call2 =Call("1","21", "lester", "1234566", "2:30", "sad")
class CallCenter(object):
 
  def __init__(self,call):
    self.queue=[]
    
  def add(self, call):
    self.queue.append(["Call id: " + call.id+', Call num: ' +call.num+", Caller Name: "+call.name+", Phone Number: "+call.number+", Call Time: "+call.time+", Reason: "+call.reason])
    return self
  def remove(self, call):
    self.queue[0]=None
  def info(self, call):
    print self.queue, "List length =", len(self.queue)


callcenter=CallCenter(call1)
callcenter.add(call1)
callcenter.add(call2)
callcenter.info(call1)