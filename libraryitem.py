from abc import ABC, abstractmethod

class LibraryItem(ABC):
  _totalBooks = 0
  _totalMagazines = 0
  _totalDVDs = 0

  @classmethod
  def increaseBooks(cls):
    cls._totalBooks += 1

  @classmethod
  def increaseMagazines(cls):
    cls._totalMagazines += 1

  @classmethod
  def increaseDVDs(cls):
    cls._totalDVDs += 1

  @classmethod
  def getTotalItems(cls):
    _totalItems = cls._totalBooks + cls._totalMagazines + cls._totalDVDs
    return _totalItems

  def __init__(self, title, itemType):
    self._title = title #* Protected
    self.itemType = itemType #* Public
    self.isBorrowed = False
    self.borrowedBy = "None"

  @abstractmethod
  def getItemDetails(self):
    pass

  @staticmethod
  def isValidItem(itemType):
    validItems = ["Book", "Magazine", "DVD"]
    return itemType if itemType in validItems else False
  
class Book(LibraryItem):
  def __init__(self, title, author):
    self.__bookId = f"book{LibraryItem._totalBooks + 1}" #* Private
    super().__init__(title, "Book")
    LibraryItem.increaseBooks()
    self.author = author

  def getItemDetails(self):
    return f"ID: {self.__bookId} | Book Title: {self._title} | Author: {self.author} | Borrowed By: {self.borrowedBy}"
  
class Magazine(LibraryItem):
  def __init__(self, title, issueNumber):
    self.__magazineId = f"mag{LibraryItem._totalMagazines + 1}"
    super().__init__(title, "Magazine")
    LibraryItem.increaseMagazines()
    self.issueNumber = issueNumber

  def getItemDetails(self):
    return f"ID: {self.__magazineId} | Magazine Title: {self._title} | Issue Number: {self.issueNumber} | Borrowed By: {self.borrowedBy}"
  
class DVD(LibraryItem):
  def __init__(self, title, duration):
    self.__dvdId = f"dvd{LibraryItem._totalDVDs + 1}"
    super().__init__(title, "DVD")
    LibraryItem.increaseDVDs()
    self.duration = duration

  def getItemDetails(self):
    return f"ID: {self.__dvdId} | DVD Title: {self._title} | Duration: {self.duration} | Borrowed By: {self.borrowedBy}"
  