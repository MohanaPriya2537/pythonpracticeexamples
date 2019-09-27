# Read an entire text file

def read(fname):
    txt = open(fname)
    print(txt.read())
read('fname.txt')