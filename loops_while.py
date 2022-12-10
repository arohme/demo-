#print("meow")
# i=1
# while i<=3:
#     print("aroh singh")
#     i=i+1

# count=0
# while count<1:
#     print("programming is a fun")
#     count= count+1

#while loop excutes statements repeatdely as long as acondition remains true.
# sum=0
# i=1
# while i<=10:
#     sum=sum+i
#     i=i+1
# print(sum)

#Repeadsubstraction quiz
import random
#1 generate two random single digit number
number1=random.randint(0,9)
number2=random.randint(0,9)
# if number<number2 swap number1 with number2
if number1<number2:
    number1,number2=number2,number1
#prompt the student to answer "what is number1 -number2?"
answer=int(input("What is"+str(number1)+"-"+str(number2)+"?"))
#repeatdly ask the question until answer is correct
while number1-number2 != answer:
    answer=eval(input("wrong aswer,try agin. what is"+str(number1)+"-"+str(number2)+"?"))
print("you got it!")