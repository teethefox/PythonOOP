class Store(object):
  def __init__(self, product, owner, location):
    self.product=product
    self.owner=owner
    self.location=location
  def add_product(self):
    product=[]
    product.append(product1.product)
    product.append(product2.product)
    print product

    
    
  def remove_product(self,product):
    
    product1.product=None
    
    print [product]
  def inventory(self,product):
    print 'product:',self.product, 'owner:', self.owner, 'location:',self.location
      

product1=Store("shirt","Me","here")
product2=Store('pants', "me", 'here')
product1.add_product()
product2.add_product()
product1.remove_product(product1.product)
product2.inventory(product2)

