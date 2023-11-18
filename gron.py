
def json():
    


def main():
    
    parser = argparse.ArgumentParser(description="count liens, words and characters of the file or from the standard input(STDIN)")
    parser.add_argument("input_file", nargs='?',type =argparse.FileType("r"),default= sys.stdin, help = "Read input from satndard input(stdin)")
    parser.add_argument('-l','--lines',help='Print total line count', action ='store_true')
    parser.add_argument('-c', '--characters',help ='print total count of characters', action = 'store_true')
    parser.add_argument('-w','--words', help ='print total count of words', action= 'store_true')

    arguments=  parser.parse_args()
    print(arguments)
    
    
    try:
         json_123 = json(arguments.input_file.name)
        file_name = arguments.input_file.name
        if os.name == 'nt':
            file_name = Path(arguments.input_file.name).as_posix()

        if not arguments.lines and not arguments.words and not  arguments.characters:
            arguments.lines = arguments.words = arguments.characters = True
        
        print(f"{'     ' + str(lines) if arguments.lines else ''}{'   '+str(words) if arguments.words else ''}{'   ' +str(characters) if arguments.characters else ''}{' '+file_name if arguments.input_file.name != '<stdin>' else ''}", end = "")
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()