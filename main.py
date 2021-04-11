# ----------imports go here----------


# ----------variables go here----------
valid = str("")


# ----------functions go here----------

#funtion for name input


def not_blank(question, error_message):
  valid = False

  while not valid:
    response = input(question)
    
    if response != "":
      return response

    else: 
      print("sorry this cant be blank")


#----------main routine----------
name = not_blank("name: ",
                "Sorry  -  this cant be blank, "
                "please enter your name")





# set up dictionaries/ lists needed to hold data

# ask user if they have used the program before & show instructions if necessary

# loop to get ticket details
# initialise loop so that it runs at leaset once  
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count <MAX_TICKETS:
  print ("you have {} seats "
  "left".format(MAX_TICKETS - count))
  

  # get details
  name = input("name: ")
  count += 1
  print()

if count == MAX_TICKETS:
  print("You have sold all the avalible tickets!")
else:
  print("you have sold {} tickets. \n"
        "there are {} places still avalible"
        .format(count, MAX_TICKETS - count))

  #get name (cant be blank)
  #get age (between 12 and 130)
  #caluculate ticket price
  #loop to ask for snacks
  #caluate snack price
  #ask for payment mmethod(and apply surcharge if nessiary)

#calculate total sales and profit

#output data to text file

print("end of program")