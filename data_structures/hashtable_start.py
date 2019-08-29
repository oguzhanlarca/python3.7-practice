# demonstrate hashtable usage
# how hashtables are use understanding
# key to value mappings are uniqe
# hash tables are typically very fast
# for small datasets, arrays are usually more efficent
# hashtables dont order entries in a predictable way

# TODO: create a hashtable all at once
items1 = dict({"key1" : 1, "key2" : 2, "key3" : "three"})
print(items1)

# TODO: create a hashtable progressively
items2 = {}
items2["key1"] = 1

print(items2)

# TODO: try to access a nonexistent key


# TODO: replace an item


# TODO: iterate the keys and values in the dictionary
for key, value in items2.items():
  print("Key: ", key, " values: ", value)