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
    print self.price, self.speed, ",", self.mileage, ",", self.fuel
car1 = Car(29567654, 35, 35, 35)
car2 = Car(2385, 300,2,12)
car3 = Car(346037262, 30, 198,70)
car4 = Car(4754, 1, 2, 3)
car5 = Car(90987654, 12347, 224, 4)
car6 = Car(264, 27, 18, 1845)
car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()