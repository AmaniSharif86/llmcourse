# first pro
course='llms python course'# string variabul
is_puplished=True # boolean variabul 
price=180.5  #float variabul
version=5 # intiger variabul
print (price) # printe value of variabul  #output --> 180.5

print (type(price)) # print type of variabul #output --> <class 'float'>
###### strings #####
print(course[0]) #return first character  #output --> l
print(course[-1]) #return first character from the end  #output--> e
print(course[-2]) #return second character from the end #output--> s
### slice a string
print(course[:5]) #  #output will be first five characters
print(course[2:5]) #  #output will be from index  to 5 characters including 5 index
# formated print
ftext=f'this coure is ==> {course}'
print (ftext)
### lists
lnum=[1,2,3,4,5]
print(lnum)
lnum.append(6) # غضافة الرقم 6 في نهاية الليست
print(lnum)
lnum.remove(6)#حذف الرقم  6 من الليست
print(lnum)
lnum.pop() #حذف آخر عنصر
print(lnum)
lnum.clear() #حذف كل العناصر
print(lnum)
lnum=[1,2,3,4,5]
lnum.insert(0,6)#إضافة 6 في الاندكس 0
print(lnum)
tuple1=(1,2,3,4,5) # مثل الليست ولكن لا يتم تغيير القيم
