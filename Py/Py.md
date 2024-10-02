##### why?
- ready to use libs
- rapid app dev - batteries included
- it's interpreted, fast and obj oriented
- huge userbase/community 
- dyncamically typed and easy to learn


 - py used indentation for block of code.
 - any no. of spaces.
 

 ##### Datatype
 nan
 number int, float/decimal, complex(a+bj), int(a=0B1010 binary 0XFF hex 0o  octal
        int(<float/string>), float(<string>), bin(dec_num)
 bool(True/False)
 sequence str, bytes, bytearrary, list, tuple, range
 string
type(var)
None - null obj


#####
magic functions
__init__

##### sequence type/collections
List
set
dictionary
- "hello"*3 => repetition
###### string
 - multiline string '''/"""
 - index s[i:j:k] substring from i through j(not including j)
       - k is step value
 - s*3 # no. of times
 - len(s)
 - s[-5:] # last 5 chars
 - s[:-5] # except last 5 chars
 - s[::-1] # reverse a string
 - s.strip(), s.lstrip(), s.rstrip(),  # strip spaces
 - s.find("substr"[,start_index, len]) # index of substring
 - s.count("substr") # num of occurences of str
 - s.replace("strtoreplc", "replace")
 - s.lower(), s.upper(), s.tittle()
 

###### list
lst= [10, 20, "Bharatha", -19.56]
- non-homegeneous lists
- lst*4 # list repeated 4times
- len(lst)
- lst.append(), lst.remove(-19.56)/del lst[1], lst.insert(index, val)
- lst.clear() # clear all ele
- max(lst), min(lst), lst.sort(reverse=True)
- not a key in dict

###### tuple
tpl = (10, 20)
tpl = (10,) # if no ',', int
- immutable, insertion order, heterogenous list, () optional
- tuple(list) # list to tuple
- as key in dict

###### set
s = {10, 20, "str"}
- no dups
- s.update([88, 99]) # add ele
- no indexing no s[i]
- s*3 # no repeatition
- s.remove(30) # rem ele
- f = frozenset(s)
       - f.update([88]) # fail, no attr update()/remove()


###### pass by references
- list,tuple,set, dict are pass by ref.

###### range
r = range(5) # 0-4
for i in r:
  print(i) #0-4

###### byte arr
lst = [10, 20, 30]
b=bytes(lst) # int list to bytes
b[0] #err
b=bytearray(lst)
b[0]=65 #no err

- byte/bytearray doesn't change the lst
- 
###### dictionary
dict ={'name': 'name1', 'name': 'name2'}
 - d.keys() list of keys
 - d.values() # list of values
 - d.items() # list of items
 - for in d: # key
 - del dict['name']

###### Immutable
- if same obj is assigned to multiple vars, vars references the same mem location.
- a=20, b=20 if a is b => True and id(a) = id(b)
- all primitive types and obj type're immutable
- in java, only string is immutable

###### Sequence types
 - None
 - def fun(): return None by default
 - Escape chars :
 - constants : final(java) PI (upper case)
 - del : delete obj
       a=10
       del a
       # dealloc's a and obj go ooscope


###### operators
 - arithmatic +,-, *, /, %, **(exp), //(int div quotiant/floor division)
 - a,b=10,5
 - +=, -=, => assigment ope
 - <, >, <=, >=, ==, != => comparision operators
 - logical operators => and, or, not
 - bitwise operators => 


###### input/output
- join => print(10, 11, sep=",")
- format specifiers %s, %f, %.2f
- print("name is %s, marks are %.2f"%(name, marks))
- "name is {}, Marks are {}".format(name, marks)
- "name is {0}, Marks are {1}".format(name, marks)
- input => r=input("optional str: "), ret as string






