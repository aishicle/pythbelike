While Loops

-continue to execute code WHILE some condition remains TRUE eg) while my pool isnt full, keep adding water

o smtg diff
#Syntax: while some_boolean_condition: do something
#can also include
​
else: #do smtg diff
x=0

while x < 5: #only runs while this condition is true
    print(f'the current value of x is {x}')
    x=x+1
x=0
​
while x < 5: #only runs while this condition is true
    print(f'the current value of x is {x}')
    x=x+1
the current value of x is 0
the current value of x is 1
the current value of x is 2
the current value of x is 3
the current value of x is 4
else:
    print("X IS NOT LESS THAN 5")
x=0
​
while x < 5: #only runs while this condition is true
    print(f'the current value of x is {x}')
    x=x+1
    # x+=1 same line just more compact lol java
else:
    print("X IS NOT LESS THAN 5")
the current value of x is 0
the current value of x is 1
the current value of x is 2
the current value of x is 3
the current value of x is 4
X IS NOT LESS THAN 5
# Lets do this for example
​
x=50
​
while x < 5: #only runs while this condition is true
    print(f'the current value of x is {x}')
    x+=1
else:
print("X IS NOT LESS THAN 5")
​
#will only execute the else bc the while statement wont execute at all bc it'll never be true
  File "<ipython-input-9-1c645c7e6b90>", line 9
    print("X IS NOT LESS THAN 5")
        ^
IndentationError: expected an indented block


USEFUL KEYWORDS (which u probs wont use all the time) break, continue, pass

break: breaks out of current closest enclosing loop

continue: goes to the TOP of the closest enclosing loop

pass: does nothing at all

#pass keyword
#pass keyword
x=[1,2,3]
​
for item in x:
    # if you just put a comment here bc you dont know what to do, you get an error
    # solution:
    pass
continue 
#continue 
mystring = 'Sammy'
​
for letter in mystring: 
    print(letter)
S
a
m
m
y
my_string='aischwauriya'

for letter in my_string:
    if letter == 'a':
        continue #so you go back to the top of the code 
    
    print(letter)
#lets say i didnt want it to print letter 'a'
my_string='aischwauriya'
​
for letter in my_string:
    if letter == 'a':
        continue #so you go back to the top of the code 
    
    print(letter)
i
s
c
h
w
u
r
i
y
#break
my_string='shaischwauriya'
​
for letter in my_string:
    if letter == 'a':
        break #so mow you dont go back to the top, it stops here
    
    print(letter)
s
h
#break is useful in while loops

#example:
x=0

while x<5:
    if x==2:
        break
    print(x)
    x+=1
#break is useful in while loops
​
#example:
x=0
​
while x<5:
    if x==2:
        break
    print(x)
    x+=1
0
1
