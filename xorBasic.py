def main():
    a = '1c0111001f010100061a024b53535009181c'
    b = '686974207468652062756c6c277320657965'
    xor_result = int(a, 16) ^ int(b, 16)

    print('%x' % xor_result)
    




