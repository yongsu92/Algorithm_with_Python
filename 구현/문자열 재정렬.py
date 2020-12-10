import sys
sys.stdin = open('input_char_sort.txt','r')

for t in range(1,int(input())+1):
    char = []
    num = 0
    for i in list(input()):
        if i.isdigit():
            num += int(i)
        else:
            char.append(i)
    char.sort()

    if num > 0:
        char.append(str(num))
    print("".join(char))
