#Exercise1:Hello World
for a in range (5):
    print("Hello world")





#Exercise 2 : Some Math
ex2=(99**3)*8
ex2





#Exercise 3 : What Is The Output ?
#print(5 < 3) #False
#print(3 == 3) #True
#print(3 == "3") #False
#print("3" > 3) #Error
#print("Hello" == "hello") #False




#Exercise 4 : Your Computer Brand
computer_brand='Lenovo'
print(f"I have a {computer_brand} computer")




#Exercise 5 : Your Information
name = 'Kanan'
age = '28'
shoe_size = '7.5 US'
info = f"Hi, my name is {name}, im {age} old, my shoe size is {shoe_size}"
info




#Exercise 6 : A & B
a = 10
b = 23
if a > b:
    print('Hello world')





#Exercise 7 : Odd Or Even
num = int(input("write a number"))
if num % 2 == 0:
    print("number is even")
else: 
    print("number is odd")





#Exercise 8 : What’s Your Name ?
name = str(input("write your name"))
out_str = ''
if name == 'Kanan':
    out_str += 'good job'
else:
    out_str += 'bad luck'
print(out_str)






#Exercise 9 : Tall Enough To Ride A Roller Coaster
height = int(input("write your height"))
out_str = ''
if height > 145:
    out_str += "U r tall enough to ride"
else:
    out_str += "U r need to grow some more to ride"
print(out_str)