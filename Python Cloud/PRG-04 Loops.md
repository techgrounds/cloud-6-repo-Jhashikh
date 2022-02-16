# Loop
## Introduction:

You can use loops when you want to run a block of code multiple times. For example, you might want to do an operation on every item in a (large) list, or you want to write an algorithm that follows the same set of instructions for multiple iterations.
There are two types of loops in Python: the while loop and the for loop.
With the while loop we can execute a set of statements as long as a condition is true. They can run indefinitely if that condition never changes. If your code is stuck in an infinite loop, just press ctrl-c (or command-c on MacOS) to force quit the running code.
The for loop runs for a predetermined number of iterations. This number can be hard coded using the range() function, or dynamically assigned (using a variable, the size of a list, or the number of lines in a document). It is also possible to accidentally create an infinite for-loop. You can use the same command (ctrl/cmd+c) to exit your program.

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

## Key-terms
* The break Statement for while loop :-With the break statement we can stop the loop even if the while condition is true.

* The continue Statement for while loop :-
With the continue statement we can stop the current iteration, and continue with the next.

* The else Statement for while loop :-
With the else statement we can run a block of code once when the condition no longer is true.

* The range() Function:- 
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

* Else in For Loop :-
The else keyword in a for loop specifies a block of code to be executed when the loop is finished

## Opdracht
Py 04.1
Create a new script.
Create a variable x and give it the value 0.
Use a while loop to print the value of x in every iteration of the loop. After printing, the value of x should increase by 1. The loop should run as long as x is smaller than or equal to 10.

Py 04.2:
Create a new script.
Copy the code below into your script.
for i in range(10):
    # do something here
Print the value of i in the for loop. You did not manually assign a value to i. Figure out how its value is determined.
Add a variable x with value 5 at the top of your script.
Using the for loop, print the value of x multiplied by the value of i, for up to 50 iterations.

Py 04.3:
Create a new script.
Copy the array below into your script.
arr = ["Coen", "Casper", "Joshua", "Abdessamad", "Saskia"]
Use a for loop to loop over the array. Print every name individually.


Example output:
### Gebruikte bronnen
https://www.codecademy.com/catalog/language/python

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
[Omschrijf hoe je weet dat je opdracht gelukt is (gebruik screenshots waar nodig).]
