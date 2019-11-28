import copy
# from lab1 import str_to_bit_array, bit_array_to_str


H = [
        [0xB1, 0x94, 0xBA, 0xC8, 0x0A, 0x08, 0xF5, 0x3B, 0x36, 0x6D, 0x00, 0x8E, 0x58, 0x4A, 0x5D, 0xE4],
        [0x85, 0x04, 0xFA, 0x9D, 0x1B, 0xB6, 0xC7, 0xAC, 0x25, 0x2E, 0x72, 0xC2, 0x02, 0xFD, 0xCE, 0x0D],
        [0x5B, 0xE3, 0xD6, 0x12, 0x17, 0xB9, 0x61, 0x81, 0xFE, 0x67, 0x86, 0xAD, 0x71, 0x6B, 0x89, 0x0B],
        [0x5C, 0xB0, 0xC0, 0xFF, 0x33, 0xC3, 0x56, 0xB8, 0x35, 0xC4, 0x05, 0xAE, 0xD8, 0xE0, 0x7F, 0x99],
        [0xE1, 0x2B, 0xDC, 0x1A, 0xE2, 0x82, 0x57, 0xEC, 0x70, 0x3F, 0xCC, 0xF0, 0x95, 0xEE, 0x8D, 0xF1],
        [0xC1, 0xAB, 0x76, 0x38, 0x9F, 0xE6, 0x78, 0xCA, 0xF7, 0xC6, 0xF8, 0x60, 0xD5, 0xBB, 0x9C, 0x4F],
        [0xF3, 0x3C, 0x65, 0x7B, 0x63, 0x7C, 0x30, 0x6A, 0xDD, 0x4E, 0xA7, 0x79, 0x9E, 0xB2, 0x3D, 0x31],
        [0x3E, 0x98, 0xB5, 0x6E, 0x27, 0xD3, 0xBC, 0xCF, 0x59, 0x1E, 0x18, 0x1F, 0x4C, 0x5A, 0xB7, 0x93],
        [0xE9, 0xDE, 0xE7, 0x2C, 0x8F, 0x0C, 0x0F, 0xA6, 0x2D, 0xDB, 0x49, 0xF4, 0x6F, 0x73, 0x96, 0x47],
        [0x06, 0x07, 0x53, 0x16, 0xED, 0x24, 0x7A, 0x37, 0x39, 0xCB, 0xA3, 0x83, 0x03, 0xA9, 0x8B, 0xF6],
        [0x92, 0xBD, 0x9B, 0x1C, 0xE5, 0xD1, 0x41, 0x01, 0x54, 0x45, 0xFB, 0xC9, 0x5E, 0x4D, 0x0E, 0xF2],
        [0x68, 0x20, 0x80, 0xAA, 0x22, 0x7D, 0x64, 0x2F, 0x26, 0x87, 0xF9, 0x34, 0x90, 0x40, 0x55, 0x11],
        [0xBE, 0x32, 0x97, 0x13, 0x43, 0xFC, 0x9A, 0x48, 0xA0, 0x2A, 0x88, 0x5F, 0x19, 0x4B, 0x09, 0xA1],
        [0x7E, 0xCD, 0xA4, 0xD0, 0x15, 0x44, 0xAF, 0x8C, 0xA5, 0x84, 0x50, 0xBF, 0x66, 0xD2, 0xE8, 0x8A],
        [0xA2, 0xD7, 0x46, 0x52, 0x42, 0xA8, 0xDF, 0xB3, 0x69, 0x74, 0xC5, 0x51, 0xEB, 0x23, 0x29, 0x21],
        [0xD4, 0xEF, 0xD9, 0xB4, 0x3A, 0x62, 0x28, 0x75, 0x91, 0x14, 0x10, 0xEA, 0x77, 0x6C, 0xDA, 0x1D]]


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


def to_int(value):
    return int(''.join(map(str, value)), 2)


def int_to_bit_array(number, count):
    bit_array = []
    for digit in bin(number)[2:]:
        bit_array.append(int(digit))
    while len(bit_array) < count:
        bit_array.insert(0, 0)
    return bit_array


def get_data_from_table(value):
    if '0x' in value:
        value = value[2:]
        if len(value) == 1:
            i = int('0x0', 16)
            j = int(value[0], 16)
            return H[i][j]
    i = int(value[0], 16)
    j = int(value[1], 16)
    return H[i][j]


def split_lists(data, size):
    arr = []
    for i in range(0, len(data), size):
        arr.append(data[i:i + size])
    return arr


def plus_mod_32(a, b):
    int_a = to_int(a)
    int_b = to_int(b)
    int_result = (int_a + int_b) % (2 ** 32)
    result = int_to_bit_array(int_result, 32)
    return result


def minus_mod_32(a, b):
    int_a = to_int(a)
    int_b = to_int(b)
    int_result = (int_a - int_b) % (2 ** 32)
    result = int_to_bit_array(int_result, 32)
    return result


class Belt:

    def __init__(self, key):
        key = str_to_bit_array(key)
        sub_keys = split_lists(key, 32)
        self.sub_keys = sub_keys * 7  # 56 тактовых ключей по 32 бита

    def G_substitution(self, data, r):
        split_list = split_lists(data, 8)
        result = []
        for value in split_list:
            int_val = to_int(value)
            hex_val = str(hex(int_val))
            result.append(get_data_from_table(hex_val))

        for i in range(len(result)):
            result[i] = int_to_bit_array(result[i], 8)

        result = [item for sublist in result for item in sublist]
        result = result[r:] + result[:r]
        while len(result) < 32:
            result.insert(0, 0)
        return result

    def encrypt(self, text):
        bits_text = str_to_bit_array(text)  # 16 байт (блок) -> 128 бит
        words = split_lists(bits_text, 32)

        a = words[0]
        b = words[1]
        c = words[2]
        d = words[3]

        for i in range(1, 9):
            sub_key = copy.deepcopy(self.sub_keys[7 * i - 6 - 1])
            value = plus_mod_32(a, sub_key)
            value = self.G_substitution(value, 5)
            b = [k ^ l for k, l in zip(b, value)]

            sub_key = copy.deepcopy(self.sub_keys[7 * i - 5 - 1])
            value = plus_mod_32(d, sub_key)
            value = self.G_substitution(value, 21)
            c = [k ^ l for k, l in zip(c, value)]

            sub_key = copy.deepcopy(self.sub_keys[7 * i - 4 - 1])
            value = plus_mod_32(b, sub_key)
            value = self.G_substitution(value, 13)
            a = minus_mod_32(a, value)

            sub_key = copy.deepcopy(self.sub_keys[7 * i - 3 - 1])
            value = plus_mod_32(b, c)
            value = plus_mod_32(value, sub_key)
            value = self.G_substitution(value, 21)
            value_i = i % (2 ** 32)
            value_i = int_to_bit_array(value_i, 32)
            while len(value_i) < 32:
                value_i.insert(0, 0)
            e = [k ^ l for k, l in zip(value, value_i)]
            b = plus_mod_32(b, e)
            c = minus_mod_32(c, e)

            sub_key = copy.deepcopy(self.sub_keys[7 * i - 2 - 1])
            value = plus_mod_32(c, sub_key)
            value = self.G_substitution(value, 13)
            d = plus_mod_32(d, value)

            sub_key = copy.deepcopy(self.sub_keys[7 * i - 1 - 1])
            value = plus_mod_32(a, sub_key)
            value = self.G_substitution(value, 21)
            b = [k ^ l for k, l in zip(b, value)]

            sub_key = copy.deepcopy(self.sub_keys[7 * i - 1])
            value = plus_mod_32(d, sub_key)
            value = self.G_substitution(value, 5)
            c = [k ^ l for k, l in zip(c, value)]

            a, b = b, a
            c, d = d, c
            b, c = c, b

        encrypted = b + d + a + c
        encrypted = bit_array_to_str(encrypted)
        return encrypted

    def decrypt(self, text):
        bits_text = str_to_bit_array(text)
        words = split_lists(bits_text, 32)
        a = words[0]
        b = words[1]
        c = words[2]
        d = words[3]

        for i in range(8, 0, -1):

            sub_key = copy.deepcopy(self.sub_keys[7 * i - 1])
            temp = plus_mod_32(a, sub_key)
            temp = self.G_substitution(temp, 5)
            b = [k ^ l for k, l in zip(b, temp)]

            sub_key = copy.deepcopy(self.sub_keys[7 * i - 1 - 1])
            temp = plus_mod_32(d, sub_key)
            temp = self.G_substitution(temp, 21)
            c = [k ^ l for k, l in zip(c, temp)]

            sub_key = copy.deepcopy(self.sub_keys[7 * i - 2 - 1])
            temp = plus_mod_32(b, sub_key)
            temp = self.G_substitution(temp, 13)
            a = minus_mod_32(a, temp)

            sub_key = copy.deepcopy(self.sub_keys[7 * i - 3 - 1])
            temp = plus_mod_32(b, c)
            temp = plus_mod_32(temp, sub_key)
            temp = self.G_substitution(temp, 21)
            value_i = i % (2 ** 32)
            value_i = int_to_bit_array(value_i, 32)
            e = [k ^ l for k, l in zip(temp, value_i)]
            b = plus_mod_32(b, e)

            c = minus_mod_32(c, e)

            sub_key = copy.deepcopy(self.sub_keys[7 * i - 4 - 1])
            temp = plus_mod_32(c, sub_key)
            temp = self.G_substitution(temp, 13)
            d = plus_mod_32(d, temp)

            sub_key = copy.deepcopy(self.sub_keys[7 * i - 5 - 1])
            temp = plus_mod_32(a, sub_key)
            temp = self.G_substitution(temp, 21)
            b = [k ^ l for k, l in zip(b, temp)]

            sub_key = copy.deepcopy(self.sub_keys[7 * i - 6 - 1])
            temp = plus_mod_32(d, sub_key)
            temp = self.G_substitution(temp, 5)
            c = [k ^ l for k, l in zip(c, temp)]

            a, b = b, a
            c, d = d, c
            a, d = d, a

        decoded = c + a + d + b
        decoded = bit_array_to_str(decoded)
        return decoded

    def encrypt_simple_substitute(self, data):
        encoded = []
        blocks = split_lists(data, 16)
        for block in blocks:
            block = self.encrypt(block)
            encoded.append(block)

        encoded = ''.join(encoded)
        return encoded

    def decrypt_simple_substitute(self, data):
        decoded = []
        blocks = split_lists(data, 16)
        for block in blocks:
            decoded.append(self.decrypt(block))

        decoded = ''.join(decoded)
        return decoded

    def encrypt_blocks(self, data, sync):
        encoded = []
        blocks = split_lists(data, 16)
        encoded_sync = self.encrypt(sync)
        for block in blocks:
            res = bit_array_to_str([k ^ l for k, l in zip(str_to_bit_array(encoded_sync), str_to_bit_array(block))])
            encoded_part = self.encrypt(res)
            encoded_sync = encoded_part
            encoded.append(encoded_part)

        encoded = ''.join(encoded)
        return encoded

    def decrypt_blocks(self, data, sync):
        decoded = []
        blocks = split_lists(data, 16)
        temp = self.encrypt(sync)
        for block in blocks:
            bit_temp = str_to_bit_array(temp)
            ans = bit_array_to_str([k ^ l for k, l in zip(str_to_bit_array(self.decrypt(block)), bit_temp)])
            decoded.append(ans)
            temp = block

        decoded = ''.join(decoded)
        return decoded


if __name__ == '__main__':
    key = 'RTYBHncnfeicnjiujUFCTYU234huU-sQ'
    belt = Belt(key)
    data = 'qwertyuioplkjhgfdsazxcvbnmkjhytr'
    print('first')
    enc = belt.encrypt_simple_substitute(data)
    print("encrypted result:  ", enc)
    dec = belt.decrypt_simple_substitute(enc)
    print("decrypted result: ", dec)

    sync = '12345678abcdefgh'
    enc = belt.encrypt_blocks(data, sync)
    print("encrypted result: ", enc)
    decrypted = stb.decrypt_clutch_blocks(encrypted, sync)
    print("Decrypted ", decrypted)