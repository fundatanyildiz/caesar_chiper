def shift(step):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z']
    shifted_alphabet = []
    for i, item in enumerate(alphabet):
        if i + step > len(alphabet):
            left = (i + step) % len(alphabet)
            item = alphabet[left]
        elif i + step == len(alphabet):
            item = alphabet[0]
        else:
            item = alphabet[i + step]
        shifted_alphabet.append(item)
    return alphabet, shifted_alphabet


def combine_letters(array, alphabet):
    text = ''
    for n in array:
        if type(n) is int:
            text += alphabet[n]
        else:
            text += n
    return text


def encrypt_decrypt(message, operation):
    alphabet, shifted_alphabet = shift(key)
    index_array = []
    if operation == "e":
        for i in message.upper():
            if i in alphabet:
                ind = alphabet.index(i)
                index_array.append(ind)
            else:
                index_array.append(i)
        return combine_letters(index_array, shifted_alphabet)
    elif operation == "d":
        for i in message.upper():
            if i in shifted_alphabet:
                ind = shifted_alphabet.index(i)
                index_array.append(ind)
            else:
                index_array.append(i)
        return combine_letters(index_array, alphabet)


try:
    op = input("Do you want to (e)ncrypt or (d)ecrypt?: ").lower()
    key = int(input("Please enter the key (0 to 26) to use.: "))
    msg = input("Message: ")
    print(encrypt_decrypt(msg, op))
except:
    print("Please enter a valid operation")
