IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

InvP = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

R0 = [57, 49, 41, 33, 25, 17, 9,
      1, 58, 50, 42, 34, 26, 18,
      10, 2, 59, 51, 43, 35, 27,
      19, 11, 3, 60, 52, 44, 36,
      63, 55, 47, 39, 31, 23, 15,
      7, 62, 54, 46, 38, 30, 22,
      14, 6, 61, 53, 45, 37, 29,
      21, 13, 5, 28, 20, 12, 4]

L0 = [14, 17, 11, 24, 1, 5, 3, 28,
      15, 6, 21, 10, 23, 19, 12, 4,
      26, 8, 16, 7, 27, 20, 13, 2,
      41, 52, 31, 37, 47, 55, 30, 40,
      51, 45, 33, 48, 44, 49, 39, 56,
      34, 53, 46, 42, 50, 36, 29, 32]


E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

SBOX = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]
]

SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

ALL_KEYS = []


def str_to_bit_array(s):
    bit_array = list()
    for byte in s:
        bits = bin(byte)[2:] if isinstance(byte, int) else bin(ord(byte))[2:]
        while len(bits) < 8:
            bits = "0" + bits
        for bit in bits:
            bit_array.append(int(bit))
    # print(bit_array)
    return bit_array


def bit_array_to_str(bit_arr):
    result = ''
    for i in range(0, len(bit_arr), 8):
        byte = bit_arr[i:i + 8]
        s = ''.join([str(b) for b in byte])
        result = result + chr(int(s, 2))
    return result


def create_keys(key_text):
    temp_key_bit_array = []

    key_bit_array = str_to_bit_array(key_text)
    for i in range(0, len(R0)):  # из 64 в 56 бит
        temp_key_bit_array.append(key_bit_array[R0[i]])

    key_left = temp_key_bit_array[:28]
    key_right = temp_key_bit_array[28:]

    for i in range(0, 16):  # цикл. сдвиги влево
        key_48bit_array = []
        key_left = key_left[SHIFT[i]:] + key_left[:SHIFT[i]]
        key_right = key_right[SHIFT[i]:] + key_right[:SHIFT[i]]
        temp_key_bit_array = key_left + key_right
        for j in range(0, len(L0)):
            key_48bit_array.append(temp_key_bit_array[L0[j] - 1])
        ALL_KEYS.append(key_48bit_array)  # вновь перемешиваем


def sbox_substitution(m_array):
    six_bit_arrays = [m_array[i:i + 6] for i in range(0, len(m_array), 6)]
    result = []
    s = ""

    for j in range(0, len(six_bit_arrays)):
        row = int(str(six_bit_arrays[j][0]) + str(six_bit_arrays[j][5]), 2)
        col = int(str(six_bit_arrays[j][1]) + str(six_bit_arrays[j][2]) + str(six_bit_arrays[j][3]) +
                  str(six_bit_arrays[j][4]), 2)
        sboxintvalue = SBOX[j][row][col]
        s = s + format(sboxintvalue, '04b')  # преобразуем в 4 бит
    for c in s:
        result.append(int(c))
    return result


def perform_round(right_part, round_num):
    expanded_array = []
    permuted_array = []
    for i in range(0, len(E)):  # расширяем до 48бит
        expanded_array.append(right_part[E[i] - 1])
    temp_array = [i ^ j for i, j in zip(expanded_array, ALL_KEYS[round_num])]  # xor с 48бит ключом
    sboxresult = sbox_substitution(temp_array)  # из 48 бит в 32
    for i in range(0, len(P)):
        permuted_array.append(sboxresult[P[i] - 1])
    # print(permuted_array)
    return permuted_array


def perform_rounds(m_array, is_encrypt):
    left_part = m_array[:32]
    right_part = m_array[32:]
    if is_encrypt:
        for i in range(0, 16):
            temp_array = right_part
            right_part = [k ^ l for k, l in zip(left_part, perform_round(right_part, i))]
            left_part = temp_array
        return right_part + left_part
    else:
        for i in range(16, 0, -1):
            temp_array = right_part
            right_part = [k ^ l for k, l in zip(left_part, perform_round(right_part, i - 1))]
            left_part = temp_array
    return right_part + left_part


def ip_text(text, is_encrypt):
    perm_arr = IP if is_encrypt is False else InvP
    arr = []
    for i in range(0, len(perm_arr)):
        arr.append(text[perm_arr[i] - 1])
    return arr


def encrypt(key_text, plain_text):
    s = ""
    create_keys(key_text)
    text_array = [plain_text[i:i + 8] for i in range(0, len(plain_text), 8)]

    if len(plain_text) % 8 != 0:
        text_array[len(text_array) - 1] = str(text_array[len(text_array) - 1]).ljust(8, " ")

    for i in range(0, len(text_array)):
        inv_perm_array = ip_text(perform_rounds(ip_text(str_to_bit_array(text_array[i]), False), True), True)
        s = s + bit_array_to_str(inv_perm_array)
    return s


def decrypt(encrypted_text, key_text):
    create_keys(key_text)
    s = ""
    text_array = [encrypted_text[i:i + 8] for i in range(0, len(encrypted_text), 8)]
    for i in range(0, len(text_array)):
        decrypt_part = ip_text(perform_rounds(ip_text(str_to_bit_array(text_array[i]), False), False), True)
        s = s + bit_array_to_str(decrypt_part)
    return s


def main():
    text = "qwerty11233ytrewq"
    first_key = "674kh333"
    second_key = "87612345"

    result_2DES = encrypt(first_key, encrypt(second_key, text))
    result_3DES = encrypt(first_key, encrypt(second_key, encrypt(first_key, text)))
    print("2DES encrypt result: ", result_2DES)
    print("3DES encrypt result: ", result_3DES+"\n")

    result_2DES = decrypt(decrypt(result_2DES, second_key), first_key)
    result_3DES = decrypt(decrypt(decrypt(result_3DES,first_key), second_key), first_key)
    print("2DES decrypt result: ", result_2DES)
    print("3DES decrypt resulr: ", result_3DES)


if __name__ == "__main__":
    main()