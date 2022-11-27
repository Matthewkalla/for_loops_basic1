#1. Print all integers from 0 to 150
for int in range(0, 151):
    print(int)

#2. Multiples of 5
for int in range(5, 1001, 5):
    print(int)

"""
3. Print integers 1 to 100.
If dvisible by 5, print "Coding" instead.
If divisible by 10, print "Coding Dojo".
"""
for int in range(1, 101):
    if(int % 5 != 0):
        print(int)
    elif(int % 10 == 0):
        print("Coding Dojo")
    elif(int % 5 == 0):
        print("Coding")

#4. Add odd integers from 0 to 500,000, and print the final sum
sum = 0
int = 0
while int <= 500000:
    int += 1
    if(int % 2 != 0):
        sum += int
else:
    print("The total sum of odd integers between 1 and 500,000 is:", str(sum))

#5. Countdown by Fours:
for i in range(2018, -1, -4):
    print(i)


#6. Flexible Counter

def flexibleCount(lowNum, highNum, mult):
    for i in range(lowNum, (highNum + 1)):
        if(i % mult == 0):
            print(i)

flexibleCount(3, 21, 4)
