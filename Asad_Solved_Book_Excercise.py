#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 2-1. Simple Message: Store a message in a variable, and then print that
# message.
# 2-2. Simple Messages: Store a message in a variable, and print that message.
# Then change the value of your variable to a new message, and print the new
# message.


# In[2]:


#2-1
a="this is python"
print(a)
a="this is python 3.0"
print(a)


# In[3]:



# code
name="Asad"
print(name.upper())
print(name.lower())
print(name.title())
print(name.strip())
print(name.endswith('l'))
print(name.find("a"))
print(name.startswith('n'))
print(name.split(','))


# In[4]:


# to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”
# 2-4. Name Cases: Store a person’s name in a variable, and then print that person’s
# name in lowercase, uppercase, and titlecase.
# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# # following, including the quotation marks:
# 2-7. Stripping Names: Store a person’s name, and include some whitespace
# characters at the beginning and end of the name. Make sure you use each
# character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().


# In[5]:


#2-3
name="Asad"
print(name+" "+"write this code")
#2-4
print(name.upper()+" "+"write this code")
print(name.lower()+" "+"write this code")
print(name.title()+" "+"write this code")
#2-5,2-6
print(name+" "+"says  \"Always Ecpect Unexpectd\" ")
#2-7
name=" nabeel  "
print(name.strip())# reomve the extra spaces


# In[6]:


#2-8. Number Eight: Write addition, subtraction, multiplication, and division
# operations that each result in the number 8. Be sure to enclose your operations
# in print statements to see the results. You should create four lines that look
# like this:
print(2+6)
print(10-2)
print(4*2)
print(2**3) #power
print(16//2)
print(16/2)


# In[7]:


#2-9. Favorite Number: Store your favorite number in a variable. Then, using
# that variable, create a message that reveals your favorite number. Print that
# message.
age=13
print("your age is "+str(age))


# In[8]:


# chaper#03 list

# 3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time.
# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message
# should be the same, but each message should be personalized with the
# person’s name.
# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”


# In[9]:



#3-1
my_friend_list=["Asad","Ali","Naveed"]
print(my_friend_list[0])
print(my_friend_list[1])
print(my_friend_list[2])
#3-2
print(my_friend_list[0]+" My great friend")
print(my_friend_list[1]+" My great friend")
print(my_friend_list[2]+" My great friend")
#3-3
fvt_car_color=["White","Blue",'Black']
print("My Most Favourite Car Color Is "+fvt_car_color[1])


# In[10]:


# list funtions
# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.
# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# in your list.
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list


# In[ ]:


#3-4
invited_persons=["ali","babar","khan"]
print(invited_persons[0]+"you are invided")
print(invited_persons[1]+"you are invided")
print(invited_persons[2]+"you are invided")
#3-5
print(invited_persons[2]+"i am not avialabe sorry")
invited_persons[1]="amir"
print(invited_persons[0]+"you are invided")
print(invited_persons[1]+"you are invided")
print(invited_persons[2]+"you are invided")
#3-6
invited_persons.insert(0,"sameer")
invited_persons.insert(2,"sad")
invited_persons.append("kabeer")
print(invited_persons[0]+"you are invided")
print(invited_persons[1]+"you are invided")
print(invited_persons[2]+"you are invided")
print(invited_persons[3]+"you are invided")
print(invited_persons[4]+"you are invided")
print(invited_persons[5]+"you are invided")


# In[ ]:


# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.


# In[ ]:


print("you can invite only 2 person your current list is")
print(invited_persons)
print(invited_persons.pop()+" sorry you can’t invite them to dinner")
print(invited_persons.pop()+" sorry you can’t invite them to dinner")
print(invited_persons.pop()+" sorry you can’t invite them to dinner")
print(invited_persons.pop()+" sorry you can’t invite them to dinner")
print(invited_persons[0]+" you are still invided")
print(invited_persons[1]+" you are still invited")
del invited_persons[1]
del invited_persons[0]
print(invited_persons)


# In[ ]:


# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse alphabetical order without changing
# the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
# • Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the
list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse alphabetical order.
Print the list to show that its order has changed.


# In[ ]:


my_places=["Pakistan","China","UAE","US","Africa"]
print(my_places)

sorted(my_places)
print(my_places)

sorted(my_places,reverse=True)
print(my_places)

my_places.sort()
print(my_places)


# In[ ]:


# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 46), use len() to print a message indicating the number
# of people you are inviting to dinner.

print("Total place is "+ str(len(my_places)))


# In[ ]:


# chapter #04 working with list


# In[ ]:


my_fvt_color=["Black","Grey","Red","SkyBlue"]
for color in my_fvt_color:
    print(color)


# In[ ]:


# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.
# • Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!
# 4-2. Animals: Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.
# • Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
# • Add a line at the end of your program stating what these animals have in
# common. You could


# In[ ]:


#4-1
my_fvt_pizza=["BBQ","Fagita","Maliboti"]
for pizza in my_fvt_pizza:
    print(pizza)
for pizza in my_fvt_pizza:
    print(pizza+" is my fvt pizza") 
print("I realy love pizza")


# In[ ]:


#4-2
my_fvt_animal=["Dog","Cat","Cow"]
for animal in my_fvt_animal:
    print(animal)
for animal in my_fvt_animal:
    print(animal+" is my fvt animal")
print("All of there are my fvt aminal")


# In[ ]:



# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.
for number in range(1,31):
    print(number)


# In[ ]:


# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)
# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.


# In[ ]:


#4-4
number_list=[]
for number in range(1,21):
    number_list.append(number)
print(min(number_list))
print(max(number_list))
print(sum(number_list))


# In[ ]:


# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.
for odd in range(0,21,2):
    print(odd)
for even in range(1,21,2):
    print(even)


# In[ ]:


# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.
for num in range(1,11):
    print(3*num)
for cube in range(1,11):
    print(cube**3)


# In[ ]:


# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.
print([cube**3 for cube in range(1,11)])


# In[ ]:


# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# • Print the message, The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# • Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.
# • Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.


# In[ ]:


my_number=[1,2,3,4,5,6,7]
print("my list "+ str(my_number))
print("The first three items in the list are")
print(my_number[:3])
print("Three items from the middle of the list are")
print(my_number[2:5])
print("The last three items in the list are")
print(my_number[4:7])


# In[ ]:


# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the second
# list. Make sure each new pizza is stored in the appropriate list.


# In[ ]:


my_fvt_pizza=["BBQ","Fagita","Maliboti"]
my_friend_fvt_pizza=["ChezPizaa","OlivePizza","SpicyPizza"]
my_fvt_pizza.append("RedHot")
print("My Fvt pizza list")
for pizza in my_fvt_pizza:
    print(pizza)
my_friend_fvt_pizza.append("BBQ")    
print("My friend pizza list")
for pizza in my_friend_fvt_pizza:
    print(pizza)
# same fvt pizza between me and my friend
print("Comparing fvt pizza between me and my friend")
for same_pizza in my_fvt_pizza:
    if same_pizza in my_friend_fvt_pizza:
        print(same_pizza)


# In[ ]:


# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the
# change.


# In[ ]:


resturent_manu=("BBQ","Biryani","ZingerBurger")
for item in resturent_manu:
    print("manue is........ "+ item)
print("After update new manu is")    
resturent_manu=("FriedRice","Soop","Haleem")
for item in resturent_manu:
    print("manue is........ "+ item)


# In[ ]:


# chapter 5


# In[ ]:



# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')


# In[ ]:


# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to 10. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() function
# • Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list


# In[ ]:


number=99
if number>100:
    print("number is greater then 100")
elif(number<100):
    print("number is less then 100")
else:
    print("number is equal to 1000")

print("a">"b")
print("a"<"b")
print("a"=="a")
print("a"=="b".upper())
num=99
if num in [12,20,99]:
    print("Number Found")
if num not in [12,20,999]:
    print("Number Not Found")


# In[ ]:


# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# • Write an if statement to test whether the alien’s color is green. If it is, print
# a message that the player just earned 5 points.
# • Write one version of this program that passes the if test and another that
# fails. (The version that fails will have no output.)


# In[ ]:


#5-3
alien_color=["green","yellow","red"]

if "green" in alien_color:
    print("player got 5 points") 
else:
    print("player got 0 point")


# In[ ]:


# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
# write an if-else chain.
# • If the alien’s color is green, print a statement that the player just earned
# 5 points for shooting the alien.
# • If the alien’s color isn’t green, print a statement that the player just earned
# 10 points.
# • Write one version of this program that runs the if block and another that
# runs the else block.


# In[ ]:


#5-4
alien_color=["green","yellow","red"]

if "green" in alien_color:
    print("player got 5 points") 
else:
    print("player got 10 point")


# In[ ]:


# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse
# chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed
# for the appropriate color alien


# In[ ]:


#5-5
color="red"
if color=="green" :
    print("player got 5 points") 
elif (color=="yellow"):
    print("player got 10 point")
elif (color=='red'):
    print("player got 15 point")
else:
    print("player got 0 point")


# In[ ]:


# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
# stage of life. Set a value for the variable age, and then:
# • If the person is less than 2 years old, print a message that the person is
# a baby.
# • If the person is at least 2 years old but less than 4, print a message that
# the person is a toddler.
# • If the person is at least 4 years old but less than 13, print a message that
# the person is a kid.
# • If the person is at least 13 years old but less than 20, print a message that
# the person is a teenager.
# • If the person is at least 20 years old but less than 65, print a message that
# the person is an adult.
# • If the person is age 65 or older, print a message that the person is an
# elder.


# In[ ]:


age=10
if age<2:
    print("the person is a baby")
elif age >= 2 and age<=4:
    print("the person is a toddler.")   
elif age>=4 and age<=13:
    print("the person is a kid.")  
elif age>=13 and age<=20:
    print("the person is a teenager.")
elif age>=20 and age<=65:
    print("the person is an adult.")
else:
    print("the person is an elder")


# In[ ]:


# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
# independent if statements that check for certain fruits in your list.
# • Make a list of your three favorite fruits and call it favorite_fruits.
# • Write five if statements. Each should check whether a certain kind of fruit
# is in your list. If the fruit is in your list, the if block should print a statement,
# such as You really like bananas!
#5-7
fruite_list=["apple","mango","orange","banan"]
if "banana" in fruite_list:
    print("banana in my list")
if "graps" in fruite_list:
    print("graps in my list") 
if "apple" in fruite_list:
    print("apple in my list")
if "mango" in fruite_list:
    print("mango in my list") 
if "redgraps" in fruite_list:
    print("redgraps in my list")


# In[ ]:


# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user:
# • If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Eric, thank you for logging
# in again.


# In[ ]:


#5-8
user_logs=["amir","admin","ali","khan","admin"]
for user in user_logs:
    if user=="admin":
        print("HELLOW---Admin")
    else:
        print(f"Hi {user} thanks for login")


# In[ ]:


# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct
# message is printed.


# In[ ]:


user_logs=[]
if len(user_logs):
    for user in user_logs:
        if user=="admin":
            print("HELLOW---Admin")
        else:
            print(f"Hi {user} thanks for login")
else:
    print("we need to add some user logs")


# In[ ]:


# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted.

#5-10
current_user=["nabeel","amir","owasi","anas","ali"]
new_user=["hassan","qasim","amir","anas","nabeel"]
for user in current_user:
    if user in new_user:
        print("this name already use change your name")
    else:
        print("this is new user")


# In[ ]:


# as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# • Store the numbers 1 through 9 in a list.
# • Loop through the list.
# • Use an if-elif-else chain inside the loop to print the proper ordinal ending
# for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
# 7th 8th 9th", and each result should be on a separate line.


number_list=[x for x in range(1,10)]
for number in number_list:
    if number==1:
        print(str(number)+"st")
    elif number==2:
        print(str(number)+"nd")
    elif number==3:
        print(str(number)+"rd")
    else:
        print(str(number)+"th")


# In[ ]:


# chapeter=06
# Dictionary



dic={"key":'value'}
print(dic['key'])
dic['key']=5
print(dic)
print(dic["key"])
dic["key2"]="value2"
print(dic)
del dic['key2']
print(dic)


# In[ ]:


# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.

person_dic={"FirstName":"Nabeel","LastName":"Anwar","Age":22,"City":"Karachi"}
fullname=person_dic["FirstName"]+" "+person_dic["LastName"]
print(f"Hi i am {fullname} my age is {person_dic['Age']} and my current city is {person_dic['City']}" )


      


# In[ ]:


# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.
      
Favourite_Number={"Ali":7,"Amir":10,"Nabeel":2,"Anus":7,"Kabeel":9}
for key,value in Favourite_Number.items():
    print(f"Friend name is {key} and there lucky number is {value}")


# In[ ]:


# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

#6-3
python_methods={"str":"Its use to conver int to string","split":"Its use to split the string","len":"Its return the lengh of the giving input"}
for key,value in python_methods.items():
    print(key+":-\n"+value+"\n")


# In[ ]:


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
            print(" Hi " + name.title() + ", I see your favorite language is " +favorite_languages[name].title() + "!")
    if 'erin' not in favorite_languages.keys():
        
        print("Erin, please take our poll!")


# In[ ]:


favorite_languages = {'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for only_key in favorite_languages.keys():
    print(only_key)
print(".............")
for only_value in favorite_languages.values():
    print(only_value)


# In[ ]:


# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.


python_methods={"str":"Its use to conver int to string","split":"Its use to split the string","len":"Its return the lengh of the giving input","count":"Its use to count the word or anything in your given input"}
for data in python_methods.items():
    print(data)


# In[ ]:


# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.


#6-5
River_Dic={"Rever_A":"Country_A","Rever_B":"Country_B","Rever_C":"Country_C"}
for River,Country in River_Dic.items():
    print(River +" run through in "+Country)
for River in River_Dic.keys():
    print("Rivers Name ...... " +River)
for Country in River_Dic.values():
    print("Country Name....."+Country)


# In[ ]:


# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.


# list in dictionayr
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],}
# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +"with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)


# In[ ]:


favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


# In[ ]:


# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.


#6-7
person_dic1={"FirstName":"Nabeel","LastName":"Anwar","Age":22,"City":"Karachi"}
person_dic2={"FirstName":"Ali","LastName":"Xyz","Age":20,"City":"Karachi"}
person_dic3={"FirstName":"Khan","LastName":"Abc","Age":23,"City":"Karachi"}
peoples=[person_dic1,person_dic2,person_dic3]
for people in peoples:
    print("Person Detail")
    for key, value in people.items():
        print(key+"......"+str(value))
    print(" ")


# In[ ]:


# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

#6-10
fvt_num={"Amir":[1,3,4],"Asad":[4,6,7]}
for key,value in fvt_num.items():
    print(key+" "+ str(value))


# In[ ]:


# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.


#6-11
cities={"khi":{"Population":2000,"Place":"SeaView"},"Isl":{"Population":1500,"Place":"Mosq"},"Kpk":{"Population":1000,"Place":"Hills"}}
for name,detail in cities.items():
    print("City Name is "+name)
    for key, value in detail.items():
        print(key+" "+str(value))


# In[ ]:


#chapter #07
#user input and while loop

# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”

car_choise=input("Enter Your rental car name")
print(f"We can Found this {car_choise} car for you on rental base")


# In[ ]:


# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.
seat_requide=int(input("How many seat you want to reserved?"))
if seat_requide >8:
    print("You will be wait for a table")
else:
    print("Your table is ready enjoy your food")


# In[ ]:


# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.
number=int(input("Enter a number"))
if number%10 ==0:
    print("this is the multiple of 10")
else:
    print("this is not the multiple of 10")


# In[ ]:


# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.


#7-4
condition=True
Topping=[]
while condition:
    user_input=input("Enter pizza topping detail or write quite for exit")
    if user_input == "quite":
        condition= False
    else:
        Topping.append(user_input)

for toping in Topping:
    print(f"You will add {toping} in your pizza")


# In[ ]:


# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

#7-5
condition=True
while condition:
    age=int(input("Enter your age to get the ticket price"))
    if age==0:
        condition=False

    if age<=3:
        print("Your ticket is free")
    elif age>3 and age<=12:
        print("Your ticket is $10")
    else:
        print("Your ticket price is $15")


# In[ ]:


# that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.
In [12]:
condition=5
while condition:
    age=int(input("Enter your age to get the ticket price"))
    if age ==-1:
        break
    condition=condition-1
    if age==0:
        condition=0


    if age<=3:
        print("Your ticket is free")
    elif age>3 and age<=12:
        print("Your ticket is $10")
    else:
        print("Your ticket price is $15")


# In[12]:


# sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.

sandwitch_list=["chickensandwitch","Beefsandwitch","Eggsandwitch","cheezsandwitch"]
finished_sanwitch=[]
for sandwitch in sandwitch_list:
    print(f"I made your {sandwitch} sandwitch")
    finished_sanwitch.append(sandwitch)
print(str(finished_sanwitch)+" "+"All are made for you")


# In[14]:


# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwitch_list=["chickensandwitch","pastrami","Beefsandwitch","Eggsandwitch","pastrami","cheezsandwitch","pastrami"]
print("Deal ha outof pastrami sandwitch")
for x in range(len(sandwitch_list)):

    # print(sandwitch_list[x])
    if sandwitch_list[x] == 'pastrami':
        sandwitch_list[x]=''
        
print("Avialable Sanwitch list "+str(sandwitch_list))


# In[16]:


# vacation. Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.

#7-10
condition=1
while condition:
    
    Dream_vications=input("Enter you dream vication place")
    print("Your Drem location is "+str(Dream_vications))
    if Dream_vications=='q':
        condition=0


# In[18]:


#chapter#08 Funtions

# 8-1. Message: Write a function called display_message() that prints one sentence
# telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.
# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.

#8-1
def mydetail():
    print("My name is nabeel and i am SMIT stidens")
#8-2    
def Fvt_Book(title):
    print("my Fvt book is "+title.title())
mydetail()
Fvt_Book("python")


# In[20]:


# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

#8-3
def make_shirt(text,size=0):
   print(text+" "+str(size))
make_shirt("My short size is",size=29)


# In[23]:


# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(text,size=0):
    if text =="i love python":
       print("Your short is to large")
    else:
       print(text+" "+str(size)) 
make_shirt("My short size is",size=29)
make_shirt("i love python",size=29)


# In[24]:


def description_city(city,country=' .....'):
    print(city+" present in "+country)
description_city("Karachi","Pakistan")
description_city("Abc")


# In[25]:


def city_country(city,country):
    print(" \"{0}, {1}\"".format(city,country))
city_country("khi","Pak")


# In[26]:


#8-7

albulm_list=[]
def make_album(artistname,title,track=0):
    album_dic={}
    album_dic[artistname]=title
    album_dic[track]=number_of_track(track)
    albulm_list.append(album_dic)
    return album_dic
def number_of_track(num=0):
    if num !=0:
        return num
    else:
        return "no track found"    

    

print(make_album("Atif","Wo lamhay"))    
print(make_album("Alizafar","Bhai hazir hay")) 
print(make_album("Argeet","tum ho",2)) 
print(albulm_list)


# In[ ]:


def make_album(artistname,title,track=0):
    album_dic={}
    album_dic[artistname]=title
    album_dic[track]=number_of_track(track)
    albulm_list.append(album_dic)
    return album_dic
def number_of_track(num=0):
    if num !=0:
        return num
    else:
        return "no track found"
condition=True
while condition:
    ArtistName=input("Enter Artist Name or Q to exit")
    if  ArtistName !="q" :

        TItle=input("Enter title name")
        Track=input("Enter track")
        result=make_album(ArtistName,TItle,Track)
    else:
        condition=False    
    print(result)


# In[ ]:





# In[ ]:




