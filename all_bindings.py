import os

OUTPUT_FILE = 'keybindings.xml'
SNIPPET_FOLDER = 'keybinding-snippets'

def main():
    fout = open(OUTPUT_FILE, 'w')
    for file in os.listdir(SNIPPET_FOLDER):
        fname = os.path.join(SNIPPET_FOLDER, file)
        f = open(fname, 'r')
        fout.write(f.read())
    fout.close()

if __name__ == '__main__':
    main()
