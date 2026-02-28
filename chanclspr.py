class Person:
  lastname = ""
  def __init__(self, name):
    self.name = name
p1 = Person("bharathi")
p2 = Person("indu")
Person.lastname = "laveti"
print(p1.lastname)
print(p2.lastname)