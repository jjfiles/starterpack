### CONDITIONALS ###
# the if else statement lets us do certain actions only when a condition has been met
x = 100
# the following if statement will only print something if the condition is True
if x > 500:
    print("greater than")
    
if x < 500:
    print("!!!!")
    
# another way to write this would be with the else statement
if x > 500:
    print("wow huge number :)")
# here else is every condition that is not met by the above one
else:
    print("wow small number :(")

# you can also chain what are known as elif statements for more complex operations
if x > 500:
    print(":)")
# elif, just like if, needs some kind of condtional statement
# you can use this as many times as you'd like
elif x == 100:
    print("omg!")
else:
    print(":c")