#creating a function to filter the elements by starting letter
def letterfilter(let,list):
    #checking the starting letter of each values in list by using startswith() function
    newlist = [x for x in list if x.startswith(let)]
    return newlist

#creating a function for extracting numbers from the list
def numberExtraction(list):
    newlist = [x for x in list if x.isdigit()]
    #checking if the list length is 0, if yes then we gotta print no elements are digit
    if len(newlist)==0:
        k = 0
        return k
    #if the list has some elements we are returning the list
    else:
        return newlist

#creating a function to extract strings out of the list
def stringExtraction(list):
    #isalpha() checks whether the list element is a string or not
    newlist = [x for x in list if x.isalpha()]
    if len(newlist) == 0:
        k = 0
        return k
    else:
        return newlist



print("ENTER THE NUMBER OF ELEMENTS IN THE LIST !\n")
x = input()
if x.isnumeric() == True:
    list=[]
    print("\nENTER THE NAMES ONE BY ONE\ N")
    #getting list inputs from the user
    for x in range(x):
        b = str(input())
        list.append(b)
    print("\nTHE LIST YOU HAVE ENTERED IS = ",list)
    print("PRESS Y/N TO CONTINUE WITH LIST OPERATIONS")
    userinput = input().upper()
    if userinput == 'Y':
            print("\nSELECT THE OPERATION")
            print("\n\n1. LETTER FILTER\n2. EXTRACT NUMBERS\n3. EXTRACT STRINGS\n4. REVERSE THE WHOLE LIST\n5. EXTRACT NUMBERS AND FIND THE LARGEST")
            ch = int(input())
            if ch == 1:
                print("\nENTER YOUR LETTER TO FILTER (input is case sensitive) ")
                let= str(input())
                print("\nFILTERED LIST IS = ",letterfilter(let,list))
            elif ch == 2:
                n = numberExtraction(list)
                if n == 0:
                    print("\nSORRY NO ELEMENTS ARE DIGITS")
                else:
                    print("\nNUMBER EXTRACTED LIST = ",numberExtraction(list))
            elif ch == 3:
                n = stringExtraction(list)
                if n == 0:
                    print("\nSORRY NO ELEMENTS ARE STRINGS")
                else:
                    print("\nSTRING EXTRACTED LIST = ", stringExtraction(list))
            elif ch == 4:
                rev = list[::-1]
                print("\nORDER REVERSED LIST = ",rev)
            elif ch == 5:
                n = numberExtraction(list)
                if n == 0:
                    print("\nSORRY NO ELEMENTS ARE DIGITS")
                else:
                    print("\nLARGEST NUMBER IN YOUR LIST = ",max(numberExtraction(list)))
            else:
                print("\nINVALID CHOICE")

    elif userinput == 'N':
            print("\nOKAY, THANK YOU!")
    else:
            print("\nSORRY SOMETHING WENT WRONG")
else:
     print("\nENTER A NUMBER PLEASE !")














