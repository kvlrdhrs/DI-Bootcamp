#Exercise 1 : Hello World-I Love Python
for i in range(4):
    print("Hello world")
for k in range(4):
    print("I love python") 




#Exercise 2 : What Is The Season ?
month = int(input("input a month (1 to 12)"))
if 2 < month <=5:
    print('Spring'),
elif 6 <= month <= 8:
    print('Summer'),
elif 9 <= month <= 11:
    print('Autumn'),
elif month in [1,2,12]:
    print('Winter')