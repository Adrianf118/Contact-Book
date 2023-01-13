# Adrian Figueredo
# Final Project
# April. 2022
# 1250 1:00pm lab

# This program is a contact book that allows the user
# to add, edit, or delete a contact

# Contact Book Program

# program welcome statement

def welcome():

   print("This program is a contact book that allows the user")
   print("to add, edit, or delete a contact.")

   print()

# prints options for user

def menu(): 
    
   print("COMMAND MENU")
   print()
   print("L - List all contacts")
   print("A - Add a contact")
   print("D - Delete a contact")
   print("E - Edit a contact")
   print("H - Help, see options")
   print("S - Stop program")
   print()

# function to bring up options for help

def help_menu(menu):

   menu()
   
# function to print contacts list

def list_menu(contacts):

   print("Here are your contacts:")
   
   print("-----------------------------")
    
   for i in range(len(contacts)):
      
      print("Name :", contacts[i][0])
      
      print("Email:", contacts[i][1])
      
      print("Phone:", contacts[i][2])
      
      print("-----------------------------")
      
      print()

# funtion to add a new contact to list
  
def add_menu(contacts):
   
   # takes name, email, phone
   
   name = input("Name: ")

   print()
   
   email = input("Email: ")

   print()
   
   phone = input("Phone: ")

   print()
   
   add = [] 
   
   add.append(name) 
   
   add.append(email)
   
   add.append(phone)
   
   contacts.append(add) 
   
   print(name, "was added")

   print()

# function to delete a contact
 
def del_menu(contacts):

   # prints list of contacts
   
   print("Contacts:")
   
   print("-----------------------------")
    
   for i in range(len(contacts)):
      
      print("Name :", contacts[i][0])
      
      print("Email:", contacts[i][1])
      
      print("Phone:", contacts[i][2])
      
      print("-----------------------------")
      
      print()
   
   print("Please choose the corresponding contact you would like to delete: ")

   print()

   # user input for which contact to delete 
    
   print("Details:\nN - to delete by name\nM - to delete by email\nP - to delete by phone number")

   print()
   
   detail = input("Enter which property to edit: ")

   detail = detail.upper()

   print()

   # error check

   while detail != "N" and detail != "M" and detail != "P":

      detail = input("Error, please enter a valid option: ")

      detail = detail.upper()

      print()

   # user input to delete contact by name, email, and phone number
    
   if detail == "N":

      check_list = []

      name = input("Please enter name: ")

      for i in contacts:

         check_list.append(i[0])

      while name not in check_list:

         print()

         name = input("Error, please enter name correctly: ")

         print()

      for i in range(len(contacts)):
           
         if contacts[i][0] == name:
               
            del contacts[i]
                
            break
                  
   elif detail == "M":

      check_list = []

      email = input("please enter email: ")

      for i in contacts:

         check_list.append(i[1])

      while email not in check_list:
         
         print()

         email = input("error, input a valid email: ")

         print()
         
      for i in range(len(contacts)):
           
         if contacts[i][1] == email:
               
            del contacts[i]
                
            break         
         
   elif detail == "P":

      check_list = []

      phone = input("Please enter phone number: ")

      for i in contacts:

         check_list.append(i[2])

      while phone not in check_list:
         
         print()

         phone = input("Error, enter a valid phone number: ")

         print()

      for i in range(len(contacts)):
           
         if contacts[i][2] == phone:
               
            del contacts[i]
                
            break        
        
   print("Contact deleted")

   print()

   return contacts

# edit a contact

def edit_contact(contacts):

   print("Please choose the corresponding contact you would like to edit: ")

   print()

   # prints list of contacts

   print("Contacts:")
   
   print("-----------------------------")
    
   for i in range(len(contacts)):
      
      print("Name :", contacts[i][0])
      
      print("Email:", contacts[i][1])
      
      print("Phone:", contacts[i][2])
      
      print("-----------------------------")
      
      print()

   # user input to edit contact by name, email, and phone number
    
   print("Details:\nN - to edit the name\nM - to edit email\nP - to edit phone number")

   print()
   
   detail = input("Which property to edit : ")

   detail = detail.upper()

   print()

   # error check

   while detail != "N" and detail != "M" and detail != "P":

      detail = input("Error, please enter a valid option: ")

      detail = detail.upper()

      print()

   # user input to edit contact by name, email, and phone number
    
   if detail == "N":

      check_list = []

      name = input("please enter name: ")

      for i in contacts:

         check_list.append(i[0])

      while name not in check_list:
         
         print()

         name = input("error, input a valid name: ")

         print()
         
      for i in contacts:
         
         if name == i[0]:

            edit = input("enter new name: ")

            i[0] = edit
            
   elif detail == "M":

      check_list = []

      email = input("please enter email: ")

      for i in contacts:

         check_list.append(i[1])

      while email not in check_list:
         
         print()

         email = input("error, input a valid email: ")

         print()
         
      for i in contacts:
         
         if email == i[1]:

            edit = input("Enter new email: ")

            i[1] = edit
         
   elif detail == "P":

      check_list = []

      phone = input("Please enter phone number: ")

      for i in contacts:

         check_list.append(i[2])

      while phone not in check_list:
         
         print()

         phone = input("Error, enter a valid phone number: ")

         print()
         
      for i in contacts:
         
         if phone == i[2]:

            edit = input("Enter new phone number: ")

            i[2] = edit
        
   print("Updated")

   print()

   return contacts
#---------------------------Main-----------------------------#

print("Contact Manager: ")

print()

welcome()

# list of contacts
  
contacts = [["Daniel Alverez", "daniel@aol.com", "909-445-3322"], ["Eric Mattes", "eric@mattes.com", "909-437-7999"], ["Jason Blake", "jason@aol.com", "909-555-4444"]]
  
# calls menu function
   
menu()

# program loop 
while True:

   # user input for command
       
   command = input("\ncommand: ")

   command = command.upper()

   print()
       
   if command == "L":

      list_menu(contacts)
           
   elif command == "A":
           
      add_menu(contacts)
           
   elif command == "D":
           
      del_menu(contacts)
      
   elif command == "E":

      edit_contact(contacts)

   elif command == "H":

      help_menu(menu)
  
   elif command == "S":
           
      break
        
   else:
      
      print("Enter valid command: ")


print('Have a great day!!!')
           

   

