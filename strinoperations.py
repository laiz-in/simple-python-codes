print("\n Enter two strings as inputs . string1 and string2 respectively \n")
string1 = str(input()).upper()
string2 = str(input()).upper()
print(" STRING 1 = ",string1)
print(" STRING 2 = ",string2,"\n\n\n")
# got two input strings from user for the operations

#creating class
class stringop:

    #creating function for concatenation
    def concatenation(stringinput1, stringinput2):
        return stringinput1 + stringinput2

    #creating function for string reversal
    def reversal(string1,string2):
        x = "".join(reversed(string1))
        y = "".join(reversed(string2))
        return x ,y

    #creating a function for the trimming operations
    def trim(string1,string2):
        x = string1[:2]
        y = string2[:3]
        return x,y

    #creating a function to count the lenghth of both the strings
    def leng(string1,string2):
        return len(string1), len(string2)

#calling concatenation function
print("CONCATENATED STRING IS        = ",stringop.concatenation(string1, string2))

#callingn the reversal function, function returns the mutiple values as a tuple
z = stringop.reversal(string1, string2)
print("STRING 1 REVERSED             = ",z[0])
print("STRING 2 REVERSED             = ",z[1])

#calling the trim function
trim = stringop.trim(string1,string2)
print("STRING 1 TRIMMED UPTO INDEX 2 = ",trim[0])
print("STRING 2 TRIMMED UPTO INDEX 3 = ",trim[1])

#calling the length function
length = stringop.leng(string1,string2)
print("LENGTH OF THE 1ST STRING      = ",length[0], "letters")
print("LENGTH OF THE 2ND STRING      = ",length[1], "letters")

