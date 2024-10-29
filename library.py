from tabulate import tabulate

class Library:
  _totalPatrons = 0
  _totalStaffs = 0

  @classmethod
  def getTotalPatrons(cls):
    return cls._totalPatrons
  @classmethod
  def getTotalStaffs(cls):
    return cls._totalStaffs
  @classmethod
  def getTotalPeople(cls):
    return cls._totalPatrons + cls._totalStaffs

  @staticmethod
  def listItems(items): #* will take an array of item
    headers = ["Item No.", "Title", "Item Type", "Status"]
    listOfItems = []
    itemNo = 1
    for item in items:
      curItem = []
      curItem.append(itemNo)
      itemNo += 1
      curItem.append(item._title)
      curItem.append(item.itemType)
      curItem.append("Not Available" if item.isBorrowed else "Available")
      listOfItems.append(curItem)
    print(tabulate(listOfItems, headers , tablefmt="grid"))

  @staticmethod
  def listPatrons(patrons):
    headers = ["Patron No.","Name", "Age", "Tier", "Items Borrowed"]
    listOfPatrons = []
    patronNo = 1
    for patron in patrons:
      curPatron = []
      curPatron.append(patronNo)
      patronNo += 1
      curPatron.append(patron.name)
      curPatron.append(patron.age)
      curPatron.append(patron.tier)
      curPatron.append(patron.totalBorrowedItems)
      listOfPatrons.append(curPatron)
    print(tabulate(listOfPatrons, headers, tablefmt="grid"))

  @staticmethod
  def listStaffs(staffs):
    headers = ["Staff No.","Name", "Age", "Salary"]
    staffNo = 1
    listOfStaffs = []
    for staff in staffs:
      curStaff = []
      curStaff.append(staffNo)
      staffNo += 1
      curStaff.append(staff.name)
      curStaff.append(staff.age)
      curStaff.append(staff.salary)
      listOfStaffs.append(curStaff)
    print(tabulate(listOfStaffs, headers, tablefmt="grid")) 

  @staticmethod
  def getAllItemsTotal(items):
    return len(items)

  def __init__(self, libName, libAddr, libContact):
    self.libName = libName
    self.libAddr = libAddr
    self.libContact = libContact
    self.items = []
    self.patrons = []
    self.staffs = []

  def addItem(self, item):
    self.items.append(item)

  def addPatron(self, patron):
    self.patrons.append(patron)
    Library._totalPatrons += 1

  def addStaff(self, staff):
    self.staffs.append(staff)
    Library._totalStaffs += 1

  def removeItem(self, itemIndex):
    try:
      self.items.pop(itemIndex)
    except:
      pass

  def removePatron(self, patronIndex):
    try:
      self.patrons.pop(patronIndex)
      Library._totalPatrons -= 1
    except:
      pass

  def removeStaff(self, staffIndex):
    try:
      self.staffs.pop(staffIndex)
      Library._totalStaffs -= 1
    except:
      pass

  def getLibraryInformation(self):
    print(f"\nLIBRARY INFORMATION:\nLibrary Name: {self.libName}\nLibrary Address: {self.libAddr}\nTotal Patron: {self.getTotalPatrons()}\nTotal Staff: {self.getTotalStaffs()}\nTotal People: {self.getTotalPeople()}\nTotal Library Items: {Library.getAllItemsTotal(self.items)}\nContact: {self.libContact}")

  def checkItem(self, itemIndex):
    return self.items[itemIndex].getItemDetails()
