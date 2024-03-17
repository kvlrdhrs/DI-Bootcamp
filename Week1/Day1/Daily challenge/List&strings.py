#Build Up A String, ex1
string =(input("write a string"))
out_str = ''
if len(string) < 10:
    out_str += "string not long enough"
elif len(string) > 10:
    out_str += "string too long"
elif len(string) == 10:
    out_str += "perfect string"
print(out_str)




#Build Up A String, ex2
print(string[0])
print(string[-1])




#Build Up A String, ex3
out_str = ''
for i in range(len(string)):
    out_str += string[i]
    print(out_str)




#Build Up A String, ex4
import random
list = list(string)
random.shuffle(list)
shuffled_string = ''.join(list)
print(shuffled_string)