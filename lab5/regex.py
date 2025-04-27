#1
import re
text=["ab","acc","abbbb","abc","acb","adb","abcd"]
pattern=r'ab*'
for x in text:
    if re.fullmatch(pattern, x):
        print(x)
 

 #2
import re
text=["abb","acc","abbb","abbbbbc","acb","adb","abcd"]
pattern=r"ab{2,3}$"
for x in text:
    if re.fullmatch(pattern,x):
        print(x)



#3
import re
pattern=r"[a-z]+_[a-z]+"
text=["hi_ww","hi_ss","hisgc","hi_Hskd","hi_sssw"]
for x in text:
    if re.fullmatch(pattern,x):
        print(x)



#4
import re
pattern=r"[A-Z][a-z]+"
text=["hiII","Hiii","HIIii","World","Python"]
for x in text:
    if re.fullmatch(pattern,x):
        print(x)




#5
import re
pattern=r"^a.*b$"
text=["apple","appldb","pppcdf","adhb","honr"]
for x in text:
    if re.fullmatch(pattern,x):
        print(x)



#6
import re
text="hello,,how..are,you."
new_text=re.sub(r"[ ,.]","：",text)
print(new_text)


#7
import re
def snake_to_camel(snake_str):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_str)
print(snake_to_camel("hello_world"))         
print(snake_to_camel("convert_snake_case")) 
print(snake_to_camel("this_is_a_test"))



#8
import re
def uppercase_words(s):
    return re.findall(r'[A-Z][a-z]*', s)
print(uppercase_words("HelloWorld")) 
print(uppercase_words("MyNameIs")) 
print(uppercase_words("HaaHssHdd"))  


#9
import re
pattern=r"([a-z])([A-Z])"
text="HelloEveryOneMyNameIsAnna"
new_text=re.sub(pattern,r"\1 \2",text)
print(new_text)



#10
import re
def camel_to_snake(camel_str):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str).lower()
print(camel_to_snake("camelCaseString")) 
print(camel_to_snake("ConvertToSnakeCase")) 
print(camel_to_snake("thisIsATest")) 