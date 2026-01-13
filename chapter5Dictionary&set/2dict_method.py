marks={
    "ankit":100,
    "anisha":65,
    "rohan":23
}
#items()-represent all the dict  item
print(marks.items())
#key()-show all the key of dict
print(marks.keys())
#update()-use to edit dictionary by edit existing onr and adding new to original dic cause its a mutable type
marks.update({"ankit":99,"renu":100})
print(marks)
#get()-help in getting value of the given  key if not exist return none 
print(marks.get("ankit"))  