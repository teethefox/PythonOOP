
class Patient(object):
  def __init__(self, id, name, allergies):
    self.id=id
    self.name=name
    self.allergies=allergies
    self.bed=None
patient1= Patient("1", "Tif", "Nah")

class Hospital(object):
  def __init__(self,patient):
    self.patients=[]
    self.name="Foxpital"
    self.capacity=10
  def admit(self, patient):
    i=len(self.patients)+1
    patient.bed=i
    self.patients.append([patient.id, patient.name,patient.allergies,patient.bed])
    print self.patients
    return self
  def discharge(self, patient):

    patient.bed=None
    self.patients.append([patient.id, patient.name,patient.allergies,patient.bed])
    self.patients.remove(self.patients[0])
    print self.patients
    return self
add=Hospital(patient1)
add.admit(patient1)
add.discharge(patient1)

    