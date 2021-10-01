from binascii import a2b_base64
import pickle
with open('test.pickle', 'rb') as f:
    pic = pickle.load(f)

pic=pic.split(',')
binary_data = pic[1]
binary_data = a2b_base64(binary_data)
fd = open('image.png', 'wb')
fd.write(binary_data)
fd.close()