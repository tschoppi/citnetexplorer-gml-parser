import sys

def main():
    if len(sys.argv) != 4:
        str = """CitNet Parser usage:
    {} publications_file citations_file output_file
    """.format(sys.argv[0])
        sys.exit(str)
    
    from .citnetparser import parse_citnet, print_gml

    pubs, cits = parse_citnet(sys.argv[1], sys.argv[2])
    print_gml(pubs, cits, sys.argv[3])

if __name__ == '__main__':
    main()
