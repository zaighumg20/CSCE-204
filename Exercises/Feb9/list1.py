# learning list
toys = ["doll", "trunk", "car", "train", "crayons"]
toys.append("phone")
toys.append("marker")
toys.append("bottle")
toys.append("soda")
toys.append("ball")

# display all the items in the list
'''for i range(10)
    print(toys[i])
    '''
'''
for toy in toys:
    print(toy)
 
'''
 # remove
if "doll" in toys:
    toys.remove("doll")
 
for toy in toys:
    print(toy)