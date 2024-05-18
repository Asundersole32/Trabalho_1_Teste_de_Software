def cifra_cesar(test_size: int, key_list: list, code_list: list):
    if test_size <= 0:
        return False

    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for index_teste in range(test_size):
        # Key represents the amount of shift applied
        key = key_list[index_teste]
        if 0 > key or key > 25:
            return False

        code = code_list[index_teste]
        if not code.isalpha() or not code.isupper():
            return False

        decoded = ""

        for letter in code:
            alf_index = alfabeto.find(letter)
            desc_index = alf_index - key

            if desc_index < 0:
                desc_index += 26

            decoded += alfabeto[desc_index]

        print(decoded)
    return True