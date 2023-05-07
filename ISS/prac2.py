"""1. key 8
HelloWelcomeToUVPCE

2. key 23
Thisiscaesercipheralgorithm

3. key 17
CaeserCipherisWeakAlgorithm

4. key 13
YouAreSmarttoAttackCaeserCipher
"""


key=1
msg=input("enter encrypted message ")
msglist=list(msg)
l2=[]
k=0

def dec(msga,k):
    for d in msga:
            x=0
            m=int(ord(d))
            if d.isupper():
                x=65
            else: 
                x=97
            
            j=chr((m-k-x)%26+x)
            print(j,end="")

while(k<25):
    print("\nkey is= ",k)
    dec(msglist,k)
    k=k+1    