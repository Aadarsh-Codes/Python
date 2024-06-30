"""
@file :-Dictionarie_Methods.py
@brief :- Demonstration of Dictionarie Methods
@author :- Aadarsh Nanaware(nanawareaadarsh333@gmail.com)
"""

#1 Creating A Dictionarie
dict = {
    
     "Key1" : "value1",
     "Key2" : "value2",
     "KeyN" : "valueN"
     
     
}

#2 Accesing  Dictionarie
print(dict["Key1"])     # Output: value1

#3 Adding Key value pair 
dict["key3"] = "value3" 

#4 Updating Dictionarie
dict["Key2"] = "valueX"

#5 Removing Key value pair
del dict["KeyN"]  

#6 Getting all keys
keys = dict.keys()
print(keys)     # Output: dict_keys(['key1', 'key2', 'key3'])


#7 Getting  all values
Values = dict.values()

#8 Merging two dictionaries
dict1 = {
     "name" : "aadarsh",
     "Number" : "989243---"
}

dict2 = {
     "country" : "India",
     "city"    : "Mumbai"
     
}

dict2.update(dict1) #  Output: {'name':aadarsh, 'Number':989243---, 'country':India, 'city': Mumbai}

#9 Setting default value 
value = dict.setdefault('key1', 'default_value')
print(value)

#10 getting default value
value1 = dict.get('key2', 'Demo')
print(value1)    # Output: Demo