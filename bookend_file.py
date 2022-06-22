import sys

def bookend_file(fname):
    with open(fname, 'r') as file:
        contents = file.read()
        mod_contents = '<MAIN>' + '\n' + contents + '\n' + '</MAIN>'
    with open(fname, 'w') as file:
        file.write(mod_contents)    

def main():
    fname = sys.argv[1]
    bookend_file(fname)

if __name__ == '__main__':
    main()