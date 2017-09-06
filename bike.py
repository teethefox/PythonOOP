"""Assignment: Bike
Create a new class called Bike with the following properties/attributes:

price
max_speed
miles
Create 3 instances of the Bike class.

Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.

Add the following functions to this class:

displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().

What would you do to prevent the instance from having negative miles?

Which methods can return self in order to allow chaining methods?"""
class Bike:
  
  def __init__(self, price, max_speed):
    self.price = price
    self.max_speed = max_speed
    self.miles = 0
  def riding(self):
    for x in range(3):
      bike1.miles += 10
    for x in range(1):
      bike2.miles += 10
    print "Riding...", self.miles,"miles"
  def reverse(self):
    for x in range(0):
      bike2.miles -= 5
    for x in range(0,1):
      bike1.miles -= 5
    for x in range(1):
      bike3.miles -=5
    if self.miles < 0:
      self.miles = 0
    print "Reversing...", self.miles,"miles"
  def displayInfo(self):
    print "Info:", self.max_speed, "," ,self.price, ",", self.miles, "miles"
  
  
bike1= Bike(200, "25mph")
bike2= Bike(2000, "500mph")
bike3= Bike(2, "10mph")

print "Bike 1:"
bike1.riding(),bike1.reverse(),bike1.displayInfo()
print "Bike 2:"
bike1.riding(),bike1.reverse(),bike2.displayInfo()
print "Bike 3:"
bike3.riding(),bike3.reverse(),bike3.displayInfo()
# set any amount of miles that is less than zero, equal to zero to avoid negative miles


