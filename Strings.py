# Strings
"ABC" #is a string
'ABC' #is a string
"@435465 3242 231&3#$%^#@!" #is a string
print('fefqf12$@#%')

#Indexing
#"Michael" me M is 0, i is 1 and so forth
# l is also -1, e is -2
Name="Michael"
print(Name[0]) #m
print(Name[-1]) #l

#Slicing, we can also get a part of our string by saying [XX:YY]
print(Name[0:4]) #Mich

#Striding, we can get every second letter too. by saying ::2
print(Name[::2]) #Mcal

#we can join 2 string
Fullname = Name + " Jackson"
Fullname
# \n means new line, \t means tab
# r will tell python that string will be display as raw string
print(Fullname+" is \n very good and \t smart")
print(Fullname+r" is \n very good and \t smart")
print(Fullname+r" is \n very good and \ smart")

#String operations for making things upper case
A = "Thriller is the sixth studio album"
print("before upper:", A)
B = A.upper()
print("After upper:", B)

# Replace the old substring with the new target substring is the segment has been found in the string
A = "Michael Jackson is the best"
B = A.replace('Michael', 'Janet')
B

# Find the substring in the string. Only the index of the first elment of substring in string will be the output
Name = "Michael Jackson"
Name.find('el')

# If cannot find the substring in the string it will say -1
Name.find('Jasdfasdasdf')