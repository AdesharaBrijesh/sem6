import math   
key = "epic"
def encryptMessage(msg): 
    cipher = "" 
    k_indx = 0
    msg_len = float(len(msg)) 
    msg_lst = list(msg) 
    key_lst = sorted(list(key)) 
    col = len(key) 
    row = int(math.ceil(msg_len / col))  
    fill_null = int((row * col) - msg_len) 
    msg_lst.extend('_' * fill_null) 
    matrix = [msg_lst[i: i + col]  
              for i in range(0, len(msg_lst), col)] 
    for _ in range(col): 
        c_idx = key.index(key_lst[k_indx]) 
        cipher += ''.join([row[c_idx]  
                          for row in matrix]) 
        k_indx += 1
    return cipher 
def decryptMessage(cipher): 
    msg = "" 
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(cipher)) 
    msg_lst = list(cipher)  
    col = len(key) 
    row = int(math.ceil(msg_len / col)) 
    key_lst = sorted(list(key)) 
    d_cipher = [] 
    for _ in range(row): 
        d_cipher += [[None] * col] 
    for _ in range(col): 
        c_idx = key.index(key_lst[k_indx]) 
        for j in range(row): 
            d_cipher[j][c_idx] = msg_lst[msg_indx] 
            msg_indx += 1
        k_indx += 1
    try: 
        msg = ''.join(sum(d_cipher, [])) 
    except TypeError: 
        raise TypeError("This program cannot", 
                        "handle repeating words.") 
    null_count = msg.count('_') 
    if null_count > 0: 
        return msg[: -null_count] 
    return msg 
msg = "dharmaysure"  
cipher = encryptMessage(msg) 
print("Encrypted Message: {}". 
               format(cipher))   
print("Decryped Message: {}". 
       format(decryptMessage(cipher)))