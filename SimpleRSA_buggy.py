#random number generator for 'e': random.randint(lower-bound, upper-bound) -- This is inclusive
#https://docs.python.org/3/library/random.html#random.randint
import random  

import math  
#GCD function: math.gcd(<comparable values>) --returns GCD
#https://docs.python.org/3/library/math.html#math.gcd

#For finding Modular Multiplicative Inverse, use pow(<number to find MMI of>, -1, <modulus>)
#https://docs.python.org/3/library/functions.html#pow


#TODO: Bring your completed extended_gcd_loop and MMI_loop functions from Phase 1
#use MMI_loop instead of pow 


#TODO: In addition to using MMI_loop instead of pow, there are several bugs in this file
#Identify the buggy lines and fix them

class RSA_KeyGeneration:
    def __init__(self, p, q):
        """assume p and q are distinct primes"""

        self.__n = p*q #bug found: self.__phi_n is incorrect as n = p*q
        self.__z= (p-1)*(q-1) #bug found: changed to being var z as z = (p-1)(q-1)

        # 13 is co-prime with 46*72 because 13 is prime
        # 1 < 13 < 46*72
        self.__e = 13
        
        self.__d = pow(self.__e, -1, self.__z) #bug found: using self.__n here when z must be used to determine a d 
        
    def getPrivateKey(self):
        return self.__d, self.__n

    def getPublicKey(self):
			
        return self.__e, self.__n


if __name__ == "__main__":

    # 47 and 73 are both prime
    p = 47
    q = 73

    keygen = RSA_KeyGeneration(p, q)
    # generate the necessary keypair values here, using the RSA_KeyGeneration class's initialization

    message = 13

    if (message >= p*q):
        print ("message must be less than n")
        
    # Use the RSA encryption method to cipher and then decipher a message.

    # Encyrpt
    public = keygen.getPublicKey()
    encrypted_message = pow(message, public[0], public[1])

    
    # this ciphered message could then be transferred over a secure, but not necessarily private, connection
    private = keygen.getPrivateKey()

    #Decrypt
    decrypted_message = pow(encrypted_message, private[0], private[1])

    if (public[1] != private[1]):
        print ("these should both be n")

    # Until you fix the bugs you will get "There's an issue!"
    if message == decrypted_message:
        print("Your message has been successfully transferred!")
    else:
        print("There's an issue!")
