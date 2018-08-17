
#i=0

#for i in range(11):
 #   print(i)

#y = 0

#for y in range(10, 20, 2):
 #       print(y)

#cat_names=["my","maja","anna"]

#for cat in (cat_names):
 #    print("If I get a cat, I will call it "+(cat))



#.joint

# counter= 30

# while counter > 0:
#     if counter % 4 == 0:
#         print(counter)
#     counter = counter - 1
# #counter= 5

#while counter > 0:
 #   print(counter)
  #  counter= counter- 1
#
# deci_amount=input("How many deciliter:")
#
# cup_amount=float(deci_amount)/2.37
#
# print("{} deciliter is equivalent to {}".format(deci_amount,cup_amount))


# list=[1,5,7,10]
# nummer=input("Vilket nummer letar du efter?")
#
# nummer_int=int(nummer)
#
# x=False
#
# for i in range(len(list)):
#     if list[i] == nummer_int:
#         x=True
#         print("The number is on position {}".format(i))
#
#
#
#
# if not x  #när vi kommer in i den här så är ju x false som vi definerade innan,
#     #  när vi sätter not framför så blir den true istället. Därför blir det
#     # if true och vi ska alltså printa ut texten. Om vi istället har ändrat värde
#     # så att den är true så ger ju not att det blir false och att det inte ska printas.
#
# # if x=False:
#     print("the number is not in the list")

#
# list=[2,6,3,0,4,13]
# order=[]
#
#
#  for i in range(len(list)):
#      x = min(list)
#      order.append(x)
#         list.remove(x)
# print(order)
#
# #list2=list.remove(x)
# #print(list2)
#
# for i in range(len(list2)):
#      y = min(list2)
#      order.append(y)
#      print(order)

#food=input("Vilka är dina två favoriträtter?")
#list=[]



# def test_recipe(food_1, food_2):
#         #list.append(food)
#     return "Jag vill ha " + food_1 + " med " + food_2
#
#
#
# food_1 = 'pasta'
# food_2 = 'köttbullar'
#
# output = test_recipe(food_1, food_2)
# print(output)









    # def second_smallest(numbers):
    #         m1, m2 = float('inf'), float('inf')
    #         for x in numbers:
    #             if x <= m1:
    #                 m1, m2 = x, m1
    #             elif x < m2:
    #                 m2 = x
    #         return m2


#Fibonacci- går alltid ner till minsta nämnaren (fib (0))


# def fib(n):
#     if n==0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# n=5
# print()
#num1=0
#num2=1

#def fib(num1,num2):


#Exercises day 3
# def infor(name,hometown,special_skill):
#     print("This is {} of {},undefeated in{}!".format(name, hometown, special_skill))
#
#
# what = 'linda'
# ist = 'lund'
# spe = 'skiing'
#
# infor(what,ist,spe)
# #infor("a","b","c")
# #output= infor(name,hometown,special_skill)
# #print(output)
# #

#price_meal=float(input("What is the price of a meal?"))

#price_meal = float(price_meal)

# def tip(price_meal):
#     if price_meal>100:
#         return "Du ska betala {}".format(price_meal+price_meal*0.05)
#     else:
#         return "Du ska betala {} ".format(price_meal+price_meal*0.1)
#
# sugg_price=tip(price_meal)
# print(sugg_price)
#     #return "Jag vill ha " + food_1 + " med " + food_2


#cookie=input("Choose your fortune cookie?")


# import random
# cookie=["Happiness awaits around the corner",
#         "A very lucky event is awaiting you",
#         "Your dream is about to come true","Love can be found where you least expect it"]
#
# number=(random.randrange(len(cookie)))
#
# print(cookie[number])


# #number=input("Give two different numbers:")
#
# def count(num_1,num_2):
#     for i in range(num_1,num_2+1):
#         print(i)
#     #return list(range(num_1,num_2+1))
#
# #a=1
# #b=5
# #hej=count(a,b)
# count(6,10)
# #print(hej)


#
test=input("Say a word")


def reverse(word):
    str=""
    for i in word:
        str = i + str
    return str
a = "letter"

print(reverse("a"))


# Python code to reverse a string
# using loop

# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str
#
#
# s = "Geeksforgeeks"
#
# print("The original string  is : ", end="")
# print(s)
#
# print("The reversed string(using loops) is : ", end="")
# print(reverse(s))
