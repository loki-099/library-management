from library import Library
from libraryitem import LibraryItem, Book, Magazine, DVD
from person import Patron, Staff

from os import system, name

def clear(): #* clearing terminals
  if name == 'nt': #* for windows
    _ = system('cls')
  else: # for mac and linux
    _ = system('clear')

def libraryInformation():
  lib1.getLibraryInformation()
  input("\nEnter any key to back: ")
  clear()
  main()

def seeItems(): #* take instance person as parameter
  Library.listItems(lib1.items)
  choice = input("\n1 - Borrow Item\n2 - Checkout Item\n3 - Return Item (Patron)\n4 - Return Item (Staff)\n5 - Check Item Details\n6 - Add Item\n7 - Remove Item\n0 - Back\n\nEnter your choice: ")
  if choice == "1": #* Borrow Item
    status = "Item is already borrowed!"
    while not status == "Successfully borrowed!":
      status = p1.borrowItem(lib1.items[int(input("Enter Item Number: ")) - 1])
      print(status) 
    clear()
    seeItems()
  elif choice == "2": #* Checkout Item
    status = "Invalid Item Number or Patron!"
    while not status == "Successfully Checkout!":
      status = s1.checkOutItem(input("Enter Patron Name: "), lib1.items[int(input("Enter Item Number: ")) - 1], lib1)
      print(status) 
    clear()
    seeItems()  
  elif choice == "3": #* Return Item (Patron)
    p1.returnItem(lib1.items[int(input("Enter Item Number: ")) - 1])
    clear()
    seeItems()
  elif choice == "4": #* Return Item (Staff)
    status = "Invalid Item Number or Patron!"
    while not status == "Successfully Returned!":
      status = s1.returnItem(input("Enter Patron Name: "), lib1.items[int(input("Enter Item Number: ")) - 1], lib1)
      print(status) 
    clear()
    seeItems()  
  elif choice == "5": #* Check Item Details
    itemIndex = int(input("Enter Item Number: ")) - 1
    clear()
    print(lib1.checkItem(itemIndex))
    input("\nEnter any key to back: ")
    clear()
    seeItems()
  elif choice == "6": #* Add Item
    itemType = LibraryItem.isValidItem(input("Enter Item Type (Book, Magazine, DVD): "))
    newItem = ""
    if itemType == "Book":
      newItem = Book(input("Enter Title: "), input("Enter Author Name: "))
      lib1.addItem(newItem)
    elif itemType == "Magazine":
      newItem = Magazine(input("Enter Title: "), input("Enter Issue Number: "))
      lib1.addItem(newItem)
    elif itemType == "DVD":
      newItem = DVD(input("Enter Title: "), input("Enter Duration: "))
      lib1.addItem(newItem)
    else:
      clear()
      print("Invalid Item Type")
      seeItems()    
    clear()
    seeItems() 
  elif choice == "7": #* Remove Item
    index = int(input("Enter Item Number: ")) - 1
    lib1.removeItem(index)
    clear()
    seeItems()
  elif choice == "0":
    clear()
    main()
  else:
    clear()
    print("Invalid option")
    seeItems()

def seePatrons(): 
  Library.listPatrons(lib1.patrons)
  choice = input("\n1 - Add Patron\n2 - Remove Patron\n0 - Back\n\nEnter your choice: ")
  if choice == "1": #* Add Patron
    newPatron = Patron(input("Enter Name: "), input("Enter Age: "), "Standard") 
    lib1.addPatron(newPatron)
    clear()
    seePatrons()
  elif choice == "2": #* Remove Patrons
    index = int(input("Enter Patron Number: ")) - 1
    lib1.removePatron(index)
    clear()
    seePatrons()
  elif choice == "0":
    clear()
    seePersons()

def seeStaffs(): 
  Library.listStaffs(lib1.staffs)
  choice = input("\n1 - Add Staff\n2 - Remove Staff\n0 - Back\n\nEnter your choice: ")
  if choice == "1": #* Add Staff
    newStaff = Staff(input("Enter Name: "), input("Enter Age: "), "15,000") 
    lib1.addStaff(newStaff)
    clear()
    seeStaffs()
  elif choice == "2": #* Remove Staff
    index = int(input("Enter Staff Number: ")) - 1
    lib1.removeStaff(index)
    clear()
    seeStaffs()
  elif choice == "0":
    clear()
    seePersons()

def seePersons():
  choice = input("\n1 - See Patrons\n2 - See Staffs\n0 - Back\n\nEnter your choice: ")
  if choice == "1": #* See Patrons
    clear()
    seePatrons()
  elif choice == "2": #* See Staffs
    clear()
    seeStaffs()
  elif choice == "0":
    clear()
    main()

def main():
  choice = input("\nLibrary Management System\n1 - Library Information\n2 - See Items\n3 - See Persons\n0 - Exit\n\nEnter choice: ")
  clear()

  if choice == "1": #* Library Information
    libraryInformation()
  elif choice == "2": #* See Items
    seeItems()
  elif choice == "3": #* See Persons
    clear()
    seePersons()
    
#* Instantiating Library Items, Patron, and Staff 
b1 = Book("Adventures of Tom Sawyer", "Mark Twain")
m2 = Magazine("Vogue Vol.1", 1236)
b2 = Book("Poject Loki", "Cris Ibarra")
p1 = Patron("Luis", 20, "VIP")
s1 = Staff("Mel", 21, "20,500")
lib1 = Library("KEPLRC", "USM", "0951848405")
lib1.addItem(b1)
lib1.addItem(m2)
lib1.addItem(b2)
lib1.addPatron(p1)
lib1.addStaff(s1)

main()





