import random

def calc_digit(cpf = []):
    # Generates 9 random digits if no CPF is provided
    if not cpf:
        for i in range(9):
            cpf.append(random.randint(0, 9))

    # Generates number based on an algorithm till the cpf length is 11
    while len(cpf) < 11:

        # Reverts the cpf to calculate the 1st and 2nd digits.
        cpf_reverse = cpf[::-1]
        modifier = 2
        sum = 0

        # Sums the result of the multiplication of the cpf digits by the modifier.
        # Multiplication is CPF Digit (from right to left (that is why the list was reversed)) * Modifier (starting from 2).
        for i in range(len(cpf_reverse)):
            sum += cpf_reverse[i] * modifier
            modifier += 1

        # Determines the 1st and 2nd digits based on the remainder of a division.
        # Division is sum of the previous multiplication by 11.
        # If the remainder is less than 2, the digit is 0, if it is equal or greater than 2, the digit is 11 - remainder.
        if sum % 11 < 2:
            cpf.append(0)
        elif sum % 11 >= 2:
            cpf.append(11 - (sum % 11))

    return cpf

def main():
    choice = input("Você quer:\n1 - Gerar CPF\n2 - Validar CPF\nEscolha: ")
    if choice == '1':
        cpf = calc_digit()
        # Prints the CPF in the format XXX.XXX.XXX-XX
        print("Seu CPF gerado é: ", end='')
        for i in range(len(cpf)):
            if i == 3 or i == 6:
                print('.', end='')
            elif i == 9:
                print('-', end='')
            print(cpf[i], end='')
        print('\n')

    elif choice == '2':
        cpf = input("Digite o CPF para validar: ")
        # Cleans the string of non-numeric characters, converts to a list of integers.
        cpf = [int(i) for i in cpf if i.isdigit()]
        # Validates CPF length
        if len(cpf) != 11:
            print("CPF inválido. O CPF deve ter 11 dígitos.")
            return
        # Calls the calc_digit with only the first 9 digits and compares the valid cpf returned by the function with the user provided cpf.
        if calc_digit(cpf[0:9]) == cpf:
            print("CPF válido.")
        else:
            print("CPF inválido.")
        

if __name__ == '__main__':
    main()