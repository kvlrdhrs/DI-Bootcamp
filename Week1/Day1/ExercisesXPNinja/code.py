#Exercise 3 : Outputs

# >>> 3 <= 3 < 9    True
#     >>> 3 == 3 == 3   True
#     >>> bool(0)   True
#     >>> bool(5 == "5")    False
#     >>> bool(4 == 4) == bool("4" == "4")  True
#     >>> bool(bool(None))  False

#     x = (1 == True)   
#     y = (1 == False)
#     a = True + 4
#     b = False + 10
#     print("x is", x)  x is true
#     print("y is", y)  y is false
#     print("a:", a)    a: 5
#     print("b:", b)    b: 10




#Exercise 4 : How Many Characters In A Sentence ?
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, \nsed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \nUt enim ad minim veniam, quis nostrud exercitation ullamco \nlaboris nisi ut aliquip ex ea commodo consequat.\nDuis aute irure dolor in reprehenderit in voluptate velit\nesse cillum dolore eu fugiat nulla pariatur.\nExcepteur sint occaecat cupidatat non proident, \nsunt in culpa qui officia deserunt mollit anim id est laborum."
print(my_text)
print(len(my_text))




#Exercise 5: Longest Word Without A Specific Character (not completed)
longest_word = ''
user_input = input("write the longest word without the character 'A'")
if 'A' not in user_input:
    print("u wrote sentence without the character 'A'")
if len(user_input) > len (longest_sentence) and 'A' not in user_input:
    out_str += "and its longest sentence without 'A'"
    longest_sentence = user_input
print(out_str)