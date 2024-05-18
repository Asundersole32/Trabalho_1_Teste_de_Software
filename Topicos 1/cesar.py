def cifra_cesar(test_number: int, key_list: list, code_list: list):
    if test_number <= 0:
        return False

    for tests in range(test_number):

        key = key_list[tests]
        code = code_list[tests]

        if 0 > key > 25:
            return False

        lettlers_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                         "T", "U", "V", "W", "X", "Y", "Z"]

        code_lettler_list = list(code)

        descriptified_code = ""

        for lettler in code_lettler_list:
            if lettler not in lettlers_list:
                return False
            else:
                for index in range(len(lettlers_list)):
                    if lettler == lettlers_list[index]:
                        index = index - key
                        descriptified_code = descriptified_code + lettlers_list[index]
                        break

        print(descriptified_code)
    return True

