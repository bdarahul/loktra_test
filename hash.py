# Write code to find a string of characters that contains only letters from acdegilmnoprstuw
# such that the hash(the_string) is 930846109532517
# if hash is defined by the following pseudo-code:
#Int64 hash (String s) {
#    Int64 h = 7
#    String letters = "acdegilmnoprstuw"
#    for(Int32 i = 0; i < s.length; i++) {
#        h = (h * 37 + letters.indexOf(s[i]))
#    }
#    return h
#}
# For example, if we were trying to find the 7 letter string where hash(the_string) was 680131659347, the answer would be "leepadg".


# ------------------------------------------------------------------------------------- #


# hashn(S) method will take the string as an input and print the hash code in number 

def hashn(S):
    L = len(S)
    n = L
    l = 'acdegilmnoprstuw'
    for i in range(0,L):
        try:
            n = (n * 37 + l.index(S[i]))
        except:
            print("INVALID STRING PASS")
    return(n)
# --------------------------------------------------------------------------------------#

# hashl(n) method will take the hash code as an input and print the corresponding String

def hashl(n):
    li = []
    while(n > 0):
        l = 'acdegilmnoprstuw'
        a = n%37
        try:
            li.append(l[a])
        except:
            li.append(l[0])
            print("Due to high value of integer its is converted into exponent form and printing wrong value at location")
        n = n - a
        n = n/37
        n = int(n)
    li.pop()
    li.reverse()
    result = ''
    for i in range(0,len(li)):
        result = result + li[i]
    return(result)

if __name__ == '__main__':
    print("Total no. of test cases 4")
    n = ['almgi','wgmnla','dgtuw','dupma']
    l = [347033439,16442380198,350689049,351191198] 
    for i in range(0,4):
        print('-'*30)
        print("Test Case :",i)
        print("String Pass:",n[i],','"Integer value:",hashn(n[i]))
        print("Integer Pass:",l[i],','"String value:",hashl(l[i]))

