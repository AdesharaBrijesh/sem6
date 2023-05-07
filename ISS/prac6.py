def encryption(pt,key):
    k = 0
    cf=""
    while k < len(pt):
        i1 = k 
        i2 = k + 1
        k =  k + 2
        for i in range(5):
            for j in range(5):
                if pt[i1] == key[i][j] or (pt[0] =='J' and key[i][j] == 'I'):
                    r1=i
                    c1=j
                elif pt[i2] == key[i][j] or (pt[1] =='J' and key[i][j] == 'I'):
                    r2=i
                    c2=j
        if r1 == r2 :
            cf = cf + key[r1][(c1+1)%5] + key[r1][(c2+1)%5]
        elif c1 == c2 :
            cf = cf + key[(r1+1)%5][c1] + key[(r2+1)%5][c1]
        else:
            cf = cf + key[r1][c2] + key[r2][c1]
    return cf   

def decryption(cf,key):
    pt=" "
    k = 0
    while k < len(cf):
        i1 = k 
        i2 = k + 1
        k =  k + 2
        for i in range(5):
            for j in range(5):
                if cf[i1] == key[i][j] or (cf[0] =='J' and key[i][j] == 'I'):
                    r1=i
                    c1=j
                elif cf[i2] == key[i][j] or (cf[1] =='J' and key[i][j] == 'I'):
                    r2=i
                    c2=j
        if r1 == r2 :
            pt = pt + key[r1][(c1-1)%5] + key[r1][(c2-1)%5]
        elif c1 == c2 :
            pt = pt + key[(r1-1)%5][c1] + key[(r2-1)%5][c1]
        else:
            pt = pt + key[r1][c2] + key[r2][c1]    
    return pt
keymatrix = [['M','O','N','A','R'],
             ['C','H','Y','B','D'],
             ['E','F','G','I','K'],
             ['L','P','Q','S','T'],
             ['U','V','W','X','Z']]
for i in range(5): 
    for j in range(5): 
        print(keymatrix[i][j], end = " ") 
    print()
pt = input("Enter Plain Text = ")
cf = encryption(pt,keymatrix)
print("cipher text = ",cf)
var = decryption(cf,keymatrix)
print("Plain text = ",var)    
