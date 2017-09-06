"""Assignment: Car
Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

A sample output would be like this:"""
class Car(object):
  def __init__(self, price, speed, fuel, mileage):
    self.price = price
    self.speed = speed
    self.fuel = fuel
    self.mileage = mileage
  def display_all(self):
    if self.price > 10000:
      self.price = self.price - self.price * 0.15
    else:
      self.price = self.price - self.price * 0.12
    print "Price:",self.price, "\n Speed:", self.speed, "\n Mileage:", self.mileage, "\n Fuel:", self.fuel," \n"
car1 = Car(29567654, 35, 35, 35)
car2 = Car(2385, 300,2,12)
car3 = Car(346037262, 30, 198,70)
car4 = Car(4754, 1, 2, 3)
car5 = Car(90987654, 12347, 224, 4)
car6 = Car(264, 27, 18, 1845)
print "Car 1:\n"
car1.display_all()
print "Car 2:\n"
car2.display_all()
print "Car 3:\n"
car3.display_all()
print "Car 4:\n"
car4.display_all()
print "Car 5:\n"
car5.display_all()
print "Car 6:\n"
car6.display_all()
  