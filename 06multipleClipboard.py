# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw delete <keyword> - delete keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw clear - clear all keywords.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        print('new keyword savved')
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    if sys.argv[1].lower() == 'delete':
        print('delete keyword successful')
        del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        print('all keywords copied to clipboard')
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        print('clipboard update')
        pyperclip.copy(mcbShelf[sys.argv[1]])

    if sys.argv[1].lower() == 'clear':
        mcbShelf.clear()
        print('clear all keywords!')


mcbShelf.close()