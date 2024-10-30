
# Jeanna Matthews, RSA PHASE 1
# Some helpful references
# https://zerobone.net/blog/math/extended-euklidean-algorithm/
# https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/

import sys, getopt

iter = 0

def gcd_loop(a, b):
    global iter
    while b:
        iter+=1
        qn = a//b
        rn = a%b

        print (a, "=", qn, "*", b, "+", rn)
        
        a = b
        b = rn

        print ("gcd_loop, iter ", iter, "a ", a, "b ", b, "q ", qn, "r ", rn)
        
        
    return a

# TODO: Write a more compact version of gcd_loop
def gcd_loop_compact(a, b):
    global iter
    while b:
        iter+=1

        # Do we actually need to compute the qn? Why or why not?
        # for just gcd, we don't actually need to compute qn - just rn
        #qn = a//b
        #rn = a%b

        # Is there a more compact way to write the same thing?
        # How can you update a and b without the intermediate variable rn?
        temp = b
        b = a%b
        a = temp
        
        print ("gcd_loop_compact, iter ", iter, "a ", a, "b ", b)
        
    return a

def gcd_recursive(a, b):
    global iter
    iter+=1
    print ("gcd_recursive, iter ", iter, "a ", a, "b ", b)
        
    if a == 0:
        return b

    return gcd_recursive(b % a, a)


# Write a well comments, not compact, non-recursive version of extended_gcd_loop
def extended_gcd_loop(a, b):

    global iter

    # TODO: Once your code is complete, consider whether this is necessary?
    if a == 0:
       return b, 0, 1

   # Why is this the correct inititialization?
    x = 1
    y = 0
    x1 = 0
    y1 = 1
    x2 = 0
    y2 = 0

    while b != 0:
        iter+=1

        qn = a // b

        rn = a % b
        a = b
        b = rn

    
        x2 = x - qn * x2
        y2 = y - qn * y2

        x = x1
        y = y1
        x1 = x2
        y1 = y2
        
        print ("extended_gcd_loop, iter ", iter, "a ", a, "b ", b, "x ", x, "y ", y)
        

    return a, x, y


def extended_gcd_recursive(a, b):

    global iter
    iter+=1

    print ("extended_gcd_recursive, iter ", iter, "a ", a, "b ")
    
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_gcd_recursive(b % a, a)

    x = y1 - (b//a) * x1
    y = x1

    print ("extended_gcd_recursive, iter ", "x ", x, "y ", y)
    
    return gcd, x, y


def MMI_loop(a, n):

    gcd, x, y = extended_gcd_loop(a,n)
    if (gcd != 1):
        print("MMI does not exist")

    else:
        print ("Coefficients: ", x, " and ", y)

        print ("x % n", x%n)
        # TODO: will either of these variants work? why or why not?
        # If yes say why? If no, show an example where they do not?
        #return (x % n + n) % n
        return x %n


def MMI_recursive(a, n):

    gcd, x, y = extended_gcd_recursive(a,n)
    if (gcd != 1):
        print("MMI does not exist")

    else:
        print ("Coefficients: ", x, " and ", y)

        print ("x % n", x%n)
        #return (x % n + n) % n
        return x %n    
        
###################################

if (len(sys.argv) != 3):
    print (sys.argv[0], "intA intB")
    sys.exit(2)

a = int (sys.argv[1])
b = int (sys.argv[2])

print ("*****************gcd_loop")
iter = 0
gcd_GOLD = gcd_loop(a,b)
print ("GCD of ", a, " and ", b, "=", gcd_GOLD)
print ("gcd_loop: iterations: ", iter)


print ("*****************gcd_loop_compact")
iter = 0
# TODO: UNCOMMENT
gcd = gcd_loop_compact(a,b)
if (gcd != gcd_GOLD):
    print ("gcd_loop_compact FAIL!")
    
print ("GCD of ", a, " and ", b, "=", gcd)
print ("gcd_loop_compact: iterations: ", iter)


print ("*****************gcd_loop_recursive")
iter = 0
# TODO: Compare the iterations of gcd_loop and gcd_recursive for ~10 pairs
# Are they the same? always the same?
# If always the same say why? If not always the same, show some examples and explain why not
gcd = gcd_recursive(a,b)
print ("GCD of ", a, " and ", b, "=", gcd)
print ("gcd_recursive: iterations: ", iter)

print ("*****************extended_gcd_recursive")
iter = 0
gcd, x, y = extended_gcd_recursive(a,b)
print ("GCD of ", a, " and ", b, "=", gcd)
print ("Coefficients: ", x, " and ", y)
print ("extended_gcd_recursive: iterations: ", iter)

if (gcd != gcd_GOLD):
    print ("gcd_loop_compact FAIL!")
    
if (a*x +b*y != gcd):
    print ("FAIL")
    
print ("*****************TODO: extended_gcd_loop")
iter = 0
# TODO: UNCOMMENT
#gcd, x, y = extended_gcd_loop(a,b)
#print ("GCD of ", a, " and ", b, "=", gcd)
#print ("Coefficients: ", x , " and ", y)
#print ("extended_gcd_loop: iterations: ", iter)

#if (gcd != gcd_GOLD):
#    print ("gcd_loop_compact FAIL!")
    
#if (a*x +b*y != gcd):
#    print ("FAIL")

print ("*****************TODO: MMI_loop")
iter = 0

# TODO: UNCOMMENT
#if (gcd ==1):
#    mmi = MMI_loop(a,b)
#    print ("MMI of ", a, " and ", b, "=", mmi)

    # We want a*mmi%b == 1
    #if (a*mmi%b != 1):
        #print ("FAIL")
    # In  other words we want a*mmi == ((a*mmi)//b) *b +1
    #if a*mmi != ((a*mmi)//b) *b +1:
       #print ("FAIL")


print ("*****************MMI_recursive")
iter = 0

if (gcd ==1):
    mmi = MMI_recursive(a,b)
    print ("MMI of ", a, " and ", b, "=", mmi)

    if (a*mmi%b != 1):
        print ("FAIL")
    if (a*mmi == (a*mmi)/b +1):
        print ("FAIL")
    # We want a*mmi%b == 1
    if (a*mmi%b != 1):
        print ("FAIL")

    # In  other words we want a*mmi == ((a*mmi)//b) *b +1
    if a*mmi != ((a*mmi)//b) *b +1:
        print ("FAIL")

        

print ("*****************pow")
# You can use pow(<number to find MMI of>, -1, <modulus>) to find the MMI
# https://docs.python.org/3/library/functions.html#pow
# Do you get the following error? Use python3 instead of python
# Need python version >= 3.8
# TypeError: pow() 2nd argument cannot be negative when 3rd argument specified
#mmi = pow(a, -1, b)
#print ("MMI of ", a, " and ", b, "=", mmi)
