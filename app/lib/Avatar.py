
from binascii import a2b_base64
from os import listdir

def seavAvatar(pic,username):
    pic=pic.split(',')
    binary_data = pic[1]
    binary_data = a2b_base64(binary_data)
    with open(f'pic/avatar/{username}.png', 'wb') as fd:
        fd.write(binary_data)
def hasAvatar(username):
    files = listdir("pic/avatar/")
    for file in files:
        if f"{username}.png"==file:
            return True
    return False


if __name__=="__main__":
    print(hasAvatar('adfffa'))