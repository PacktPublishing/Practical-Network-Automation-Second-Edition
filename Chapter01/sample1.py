#ask for input of user's name and prints it with a message
x=input("What is your name:")
print ("how are you"+x)
y="how are you"+x

#validates and prints message if 'test1' AND 'test2' exists in input
if ("test1" in y) and ("test2" in y):
    print ("cool")

#splits the sentence stored in variable x with blank spaces    
x=y.split(" ")
print (x)
#adds the string "awesome" to the third word in the sentence and stores it in x
x=x[2]+"awesome"

#validates if word "are" is in x and prints the message accordingly
if ("are" in x):
    print ("not cool")

    

    
