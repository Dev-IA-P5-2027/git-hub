### cc toi 

numb = int(input("Mets un nombre : 10"))
def dec_go_bin(n):
    bits = ""
    while n > 0:
        bits = str(n % 2) + bits
        n = n // 2
    return bits
binaire = dec_go_bin(numb)
print(f"{numb} : {binaire}")

