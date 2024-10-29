class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Patron(Person):
  def __init__(self, name, age, tier):
    super().__init__(name, age)
    self.totalBorrowedItems = 0
    self.tier = tier

  def borrowItem(self, item):
    #* takes item as instance object
    if not item.isBorrowed:
      item.isBorrowed = True
      item.borrowedBy = self.name
      self.totalBorrowedItems += 1
      return "Successfully borrowed!"
    else:
      return "Item is already borrowed!"

  def returnItem(self, item):
    if item.isBorrowed and item.borrowedBy == self.name:
      item.isBorrowed = False
      item.borrowedBy = "None"
      self.totalBorrowedItems -= 1
      print("Successfully returned!")
    else:
      print("Item is already returned!")

class Staff(Person):
  @staticmethod
  def checkPatron(patronName, library):
    patronToBorrow = Patron("None", 0, "None")
    for patron in library.patrons:
      if patron.name == patronName:
        patronToBorrow = patron
    return patronToBorrow

  def __init__(self, name, age, salary):
    super().__init__(name, age)
    self.salary = salary

  def checkOutItem(self, patronName, item, library):
    patron = Staff.checkPatron(patronName, library)
    if not item.isBorrowed and patron.name == patronName:
      item.borrowedBy = patronName
      item.isBorrowed = True
      patron.totalBorrowedItems += 1
      return "Successfully Checkout!"
    else:
      return "Invalid Item Number or Patron!"
    
  def returnItem(self, patronName, item, library):
    patron = Staff.checkPatron(patronName, library)
    if not ((not item.isBorrowed) and patron.name == patronName) and item.borrowedBy == patronName:
      item.isBorrowed = False
      item.borrowedBy = "None"
      patron.totalBorrowedItems -= 1
      return "Successfully Returned!"
    else:
      return "Invalid Item Number or Patron!"




      