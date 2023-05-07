s_msg=input("Enter your message : ")
sm_l=list(s_msg)
key=list(input("enter key : "))
ke1=[]
p=0
for i in sm_l:
    ke1.append(key[p])
    p=(p+1)%len(key)

def encrypt(sm_l,key):
    l1=[]
    o=0
        
    for k in sm_l:
        x=0
        
        ke=int(ord(key[o]))
        m=int(ord(k))
        o=o+1
        if k.isupper():
            x=65
        else: 
            x=97
        
        j=chr(((m-x)+(ke-x))%26+x)
        
            
        l1.append(j)
    return l1

def decrypt(l1,key):
    l2=[]
    o=0
    for k in l1:
        x=0
        ke=int(ord(key[o]))
        m=int(ord(k))
        o=o+1
        if k.isupper():
            x=65
        else: 
            x=97
        
        j=chr(((m-x)-(ke-x) +26)%26+x)
        
            
        l2.append(j)
    return l2

en_sml=encrypt(sm_l,ke1)
print("Encrypted data is : ")
for x in en_sml:
    print(x,end="")
print()
de_sml=decrypt(en_sml,ke1)
print("Decrypted data is : ")
for x in de_sml:
    print(x,end="")










'''def encrypt(pt,key):


def decrypt(
print("encrypted message is: ")    
k=0
for i in l1:
   x=l1[k]
   y=l2[k]
   k=k+1
   print(encrypt(x,y),end="")

print("decrpyted message is:")
m=0
for i in l3:
    x=l3[m]
    y=l2[m]
    m=m+1
    print(decrypt(x,y),end="")
'''


   
