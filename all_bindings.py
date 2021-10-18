import os

OUTPUT_FILE = 'keybindings.xml'
BINDINGS_FOLDER = 'keybinding-snippets'

def main():
    fout = open(OUTPUT_FILE, 'w')
    for file in os.listdir(BINDINGS_FOLDER):
        fname = os.path.join(BINDINGS_FOLDER, file)
        f = open(fname, 'r')
        # print(f.read())
        fout.write(f.read())
    fout.close()


if __name__ == '__main__':
    main()
    