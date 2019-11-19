# math={'john':55.0,'tam':66.0}
# for key in math.keys():
#     print(key)


# dict ={'god':55,'bobby':88}
# print(dict)
# doc ={'lion':98,'king':89}
# dict.update(doc)
# print(dict)

#add two dictionary
dict ={'god':55,'bobby':88}
doc ={'lion':98,'king':89}
d={}
for d in (dict, doc):
    d.update(dict)
print(d)
#chek weather key is present or not.
if 'lion' in dict:
    print('Key is present in the dictionary')
else:
    print('key is not present in the dictionary')