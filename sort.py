# coding: utf-8

'''
    Description:
    Sorts the entries at the lowest level and the order of the top-level
    contents do not match the order of the actual entries.

    Credits:
	Vinta
	https://github.com/vinta/awesome-python
'''

def main():
    with open('README.md', 'r') as read_me_file:
        read_me = read_me_file.readlines()
        print(read_me)

    blocks = []
    last_indent = None
    for line in read_me:
        s_line = line.lstrip()
        indent = len(line) - len(s_line)
        if any([s_line.startswith(s) for s in ['* [', '- [']]):
            if indent == last_indent:
                blocks[-1].append(line)
            else:
                blocks.append([line])
            last_indent = indent
        else:
            blocks.append([line])
            last_indent = None

    with open('README.md', 'w+') as sorted_file:
        blocks = [''.join(sorted(block, key=lambda s: s.lower())) for block in blocks]
        sorted_file.write(''.join(blocks))
        print(blocks)

if __name__ == "__main__":
    main()
