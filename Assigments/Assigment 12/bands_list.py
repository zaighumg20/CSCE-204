#Author : Talha Gill

#file named bands.txt
file_name = "bands.txt" 

#write list of bands in file
def writeBands(bands):
    #open file in write mode
    file = open(file_name,"w") 
    #write bands in file
    for band in bands:
        file.write(band+"\n")

#function is ued to readBands from file
def readBands():
    #create list named bands
    bands=[]
    #open file
    with open(file_name) as file:
        #read band from file 
        for line in file:
            #add in list 
            bands.append(line.strip())
    #return list of bands
    return bands

#This function is used to print all bands 
def listBands(bands):
    for band in bands:
        print('- ',band)

#this function is used to add bands in list
def addBands(bands):
    #take input in band name
    newband=input('Enter Band name: ')
    #loop through the list of bands
    for band in bands:
        #if ban found print the message
        if band == newband:
            print('Sorry',band, 'was already on the list')
            return bands
    
    #if it's new band add to the list
    print(newband,'was added!')
    bands.append(newband)
    #retun the band list
    return bands

#This function is used to delete band from bands list
def deleteBands(bands):
    delete_band=input('Enter Band name: ')
    for band in bands:
        #if band found then delete the band
        if band == delete_band:
            print(band,'was deleted')
            bands.remove(band)
            return bands
    
    #if band not found then print the message
    print('Sorry your band was not found in the list')
    return bands
 
#definition of main function
def main():
   #read bands list
    bands = readBands()
    #choice menu
    while True:
        #do the operation according to choice
        choice = input('Enter (L)ist, (A)dd, (D)elete, or (Q)uit: ').lower()
        if choice == 'l':
            listBands(bands)
        elif choice == 'a':
            bands = addBands(bands)
        elif choice == 'd':
            bands = deleteBands(bands)
        elif choice =='q':
            print('Good bye!')
            break
        else:
            print('Invalid command, try again.')
    #write list of bands in the file
    writeBands(bands)

#main function
if __name__== '__main__':
    main()