def spiliter(text):
    b = ""
    for i in text[::-1]:
        if len(b) %4 == 0 & len(b) == 0:
            b = b + "," + i 
        else:   
            b = b + i
    return b[::-1][0: -1]