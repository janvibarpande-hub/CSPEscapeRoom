print("Room 2")
import random
weight = random.uniform(10, 20)
basket_list = [["flower", 1.1], ["cookie", 1.5], ["Muffin", 2]]
print("There are 3 items in the basket: flowers, cookies, and muffins.")
print("The flowers weigh 1.1")
print("The cookies weigh 1.5")
print("The muffins weigh 2")
print("Calculate the number of each item that is needed for the basket to weigh {:.1dp}.".format(weight))
flower = int(input("How many flowers are needed? "))
cookie = int(input("How many cookies are needed? "))
muffin = int(input("How many muffins are needed? "))
num_list = []
num_list.append(flower)
num_list.append(cookie)
num_list.append(muffin)
print(num_list)
