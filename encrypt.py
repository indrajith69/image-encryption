
def encrypt(path,key):
        with open(path, 'rb') as fin:
                image = fin.read()
                image = bytearray(image)

        for index, values in enumerate(image):
                image[index] = values ^ key

        with open(path, 'wb') as fin:
                fin.write(image)

decrypt = encrypt

path = r'photo.jpg'
key = 127 #1->255

encrypt(path,key)
decrypt(path,key)

