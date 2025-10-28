### cc toi 

# numb = int(input("Mets un nombre : 10"))
# def dec_go_bin(n):
#     bits = ""
#     while n > 0:
#         bits = str(n % 2) + bits
#         n = n // 2
#     return bits
# binaire = dec_go_bin(numb)
# print(f"{numb} : {binaire}")

A = 1
B = 2
somme = A + B 

def Suite_F():
    # print(somme)
    somme+1 = A, B = B, A + B
    return somme+1

while True :
    somme+1 = Suite_F()
    Suite_F()
    print(f"{somme+1}")
