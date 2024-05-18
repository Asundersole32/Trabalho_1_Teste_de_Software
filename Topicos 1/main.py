from cesar import cifra_cesar


test_quantity = int(input())

code_key_list = []
criptified_code_list = []

for quantity in range(test_quantity):
    criptified_code = str(input())
    code_key = int(input())

    code_key_list.append(code_key)
    criptified_code_list.append(criptified_code)

fuction_test = cifra_cesar(test_quantity, code_key_list, criptified_code_list)
