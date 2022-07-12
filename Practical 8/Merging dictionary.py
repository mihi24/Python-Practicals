combined_dict = {}

keys = ["apple","guava","mango"]
values = ["red","green","yellow"]

for k,v in zip(keys,values):
    combined_dict[k] = v

print(combined_dict)