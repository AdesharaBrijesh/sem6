
key=1
s_msg=input("Enter your message : ")
sm_l=list(s_msg)

def encrypt(sm_l,key):
    l1=[]
    for k in sm_l:
        if (ord(k)==32):
            l1.append(" ")
        else:    
            x=0
            m=int(ord(k))
            if k.isupper():
                x=65
            else: 
                x=97
            if m%2==0:
                j=chr((m+key-x)%26+x)
            else:
                j=chr((m-key-x)%26+x)
            l1.append(j)
    return l1

def decrypt(l1,key):
    l2=[]
    for k in l1:
        if(ord(k)==32):
            l2.append(" ")
        else:
            x=0
            m=int(ord(k))
            if k.isupper():
                x=65
            else: 
                x=97
            if m%2==0:
                j=chr((m+key-x)%26+x)
            else:
                j=chr((m-key-x)%26+x)
            l2.append(j)
    return l2

en_sml=encrypt(sm_l,key)
print("Encrypted data is : ")
for x in en_sml:
    print(x,end="")
print()
de_sml=decrypt(en_sml,key)
print("Decrypted data is : ")
for x in de_sml:
    print(x,end="")

