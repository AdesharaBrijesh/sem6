dicts = {"a":"z","b":"y","c":"x","d":"w","e":"v","f":"u","g":"t","h":"s","i":"r","j":"q","k":"p","l":"o","m":"n","n":"m","o":"l","p":"k","q":"j","r":"i","s":"h","t":"g","u":"f","v":"e","w":"d","x":"c","y":"b","z":"a",}
dictc = {"A":"Z","B":"Y","C":"X","D":"W","E":"V","F":"U","G":"T","H":"S","I":"R","J":"Q","K":"P","L":"O","M":"N","N":"M","O":"L","P":"K","Q":"J","R":"I","S":"H","T":"G","U":"F","V":"E","W":"D","X":"C","Y":"B","Z":"A",}
a=input("enter message ")

l1=list(a)
l2=[]

def get_key(val):
   
    if(val.isupper()): 
        for key, value in dictc.items(): 
             if val == value: 
                 return key
  
    else:
        for key, value in dicts.items(): 
             if val == value: 
                 return key
print(" \nencrypted text is")           
for i in l1:
    if(i.isupper()):
        print(dictc[i],end="")
        z=dictc[i]
        l2.append(z)
    elif(ord(i)==32):
	    l2.append(" ")
	    print(i,end="")
    else:
        print(dicts[i],end="")
        z=dicts[i]
        l2.append(z)
print("\nDecrypted text is ")

for i in l2:
    no=ord(i)
    if(no==32):
        
        print(" ",end="")
    else:
        print(get_key(i),end="")  
       

    
