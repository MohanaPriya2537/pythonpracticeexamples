# Append text to a file and display the text

def read(fname):
    with open('fname', "a+") as f:
        f.write("Welcome\n")
        f.write("Python class")
        a=f.read()
        print(a)
read('../abc.txt')