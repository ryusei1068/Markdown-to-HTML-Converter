import markdown
import sys


def read_content(inputpath):
    with open(inputpath) as f:
        return f.read()


def write_content(ouputpath, content, option):
    with open(ouputpath, option) as f:
        f.write(content)


def convert_html(*args):
    verify_arguments(2, *args)
    args = args[0]

    inputpath = args[0]
    outputpath = args[1]

    if not verify_file_extend(inputpath, len(inputpath) - 3, '.md') or not verify_file_extend(outputpath, len(outputpath) - 5, '.html'):
        sys.stdout.buffer.write(b'invalid file extend\n')
        sys.exit(1)

    content = read_content(inputpath)
    html = markdown.markdown(content)
    write_content(outputpath, html, 'w')


def verify_arguments(n, *args):
    if n != len(*args):
        sys.stdout.buffer.write(b'valid number of arguments\n')
        sys.exit(1)


def verify_file_extend(path, start, extend):
    return path.find(extend, start) != -1


def main():
    args = sys.argv[1:]

    if len(args) <= 1:
        sys.stdout.buffer.write(b'valid your input,\n python3 file-converter.py markdown inputfile outputfile \n')
        sys.exit(1)

    
    hash_map = {}
    hash_map['markdown'] = convert_html
    
    if args[0] in hash_map.keys():
        hash_map[args[0]](args[1:])
    else:
        print("not found, ", args[0])

if __name__ == "__main__":
    main()