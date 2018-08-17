#6. Create a program that asks the user to input some new hobbies (one at a time)
# and saves it to a list using list.append(). If the user enters “stop”, the program should stop and print all hobbies.
#For example:
#What do you like to do?:
#What do you like to do?:
#What do you like to do?:
#Okay. Hobbies are swimming, painting.


list1=[]




answer = input("What do you like to do?")
while answer != "stop":
    list1.append(answer)
    answer = input("What do you like to do?")



print(list1)