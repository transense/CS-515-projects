import argparse
import os
from pathlib import Path
import re
import sys
def wc(file):
    if file == '<stdin>':
        content = sys.stdin.read()
        #print(f"'{content}'")
        lines = content.count('\n')
        characters = len(content)
        words = len(content.split())
        # print("No of Words",len(words))
        return  lines, words, characters

        # print(file)
    
    file = open(file)
    #print(f"'{file.readlines()}'")
    lines = len(file.readlines())
    # print("Sentences = ", len(file.readlines()))
    file.seek(0)
    content = file.read()
    characters = len(content)
    # print("No of character", len(content)+1)
    words = len(content.split())
    # print("No of Words",len(words))
    return  lines, words, characters

def main():
    
    parser = argparse.ArgumentParser(description="count liens, words and characters of the file or from the standard input(STDIN)")
    parser.add_argument("input_file", nargs='?',type = argparse.FileType("r"),default= sys.stdin, help = "Read input from satndard input(stdin)")
    parser.add_argument('-l','--lines',help='Print total line count', action ='store_true')
    parser.add_argument('-c', '--characters',help ='print total count of characters', action = 'store_true')
    parser.add_argument('-w','--words', help ='print total count of words', action= 'store_true')

    arguments=  parser.parse_args()
    # print(arguments)
    
    
    # try:
    lines, words, characters = wc(arguments.input_file.name)
    file_name = arguments.input_file.name
    if os.name == 'nt':
        file_name = Path(arguments.input_file.name).as_posix()

    if not arguments.lines and not arguments.words and not  arguments.characters:
        arguments.lines = arguments.words = arguments.characters = True
    
    print(f"{'     ' + str(lines) if arguments.lines else ''}{'   '+str(words) if arguments.words else ''}{'   ' +str(characters) if arguments.characters else ''}{' '+file_name if arguments.input_file.name != '<stdin>' else ''}", end = "")
    # except Exception as e:
    #     print(e)
    #     sys.exit(1)

if __name__ == "__main__":
    main()