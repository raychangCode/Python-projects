import sys

FILE = 'data/small/small-2000.txt'


def main():
    with open(FILE, 'r') as f:
        for line in f:
            if len(line) <= 5:
                year = line.strip()
                print(year)
            else:
                name_line = line.split(',')
                rank = name_line[0].strip()
                name1 = name_line[1].strip()
                name2 = name_line[2].strip()
                print(f'r= {rank}, n1= {name1}, n2= {name2}')


if __name__ == '__main__':
    main()