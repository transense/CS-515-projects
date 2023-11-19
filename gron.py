import json
import sys
import argparse
import os

def json_to_gron(data, prefix="json"):
    gron = f"{prefix} = {{}};\n"
    
    
    def convert(obj, prefix="json"):
        nonlocal gron
        if isinstance(obj, dict):
            for i, value in sorted(obj.items()):
                new_prefix = f"{prefix}.{i}"
                if isinstance(value, dict):
                    gron += f"{new_prefix} = {{}};\n"
                convert(value, new_prefix)
        elif isinstance(obj, list):
            gron += f"{prefix} = [];\n"
            if all(isinstance(item, dict) for item in obj):
                for i, value in enumerate(obj):
                    new_prefix = f"{prefix}[{i}]"
                    gron += f"{new_prefix} = {{}};\n"
                    convert(value, new_prefix)
            else:
                for i, value in enumerate(obj):
                    new_prefix = f"{prefix}[{i}]"
                    convert(value, new_prefix)
        else:
            gron += f"{prefix} = {json.dumps(obj)};\n"
    
    convert(data)
    return gron

def main():
    
    parser = argparse.ArgumentParser(description="count liens, words and characters of the file or from the standard input(STDIN)")
    parser.add_argument("input_file", nargs='?',type =argparse.FileType("r"),default= sys.stdin, help = "Read input from satndard input(stdin)")
    # parser.add_argument('-l','--lines',help='Print total line count', action ='store_true')
    # parser.add_argument('-c', '--characters',help ='print total count of characters', action = 'store_true')
    # parser.add_argument('-w','--words', help ='print total count of words', action= 'store_true')

    arguments =  parser.parse_args()
    
    try:
        file = open(arguments.input_file.name)
        content = json.load(file)
        
        print(json_to_gron(content))
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
    