#create mutiplication table

"""
1 2 3
2 4 5 
3 6 9 
"""

tableSize = int(input("Enter size of table: "))

for row in range(1, tableSize + 1 ): # Loop through rows
    for col in range (1 , tableSize + 1 ):  # for every row loop the cols
        ans = row * col

        if (len(str(ans)) == 1):
            print(f" {ans}", end = " ")
        else:
            print(f"{row * col}", end=" ")
    print() 