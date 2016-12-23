l = []

def insert_list(i,e):
    l.insert(i,e)

def remove_list(e):
    l.remove(e)

def append_list(e):
    l.append(e)


if __name__ == '__main__':
    N = int(input())

    while N != 0:
        user_input = input()
        if 'insert' in user_input:
            a = user_input.split()
            insert_list(int(a[1]), int(a[2]))
        elif 'print' == user_input:
            print(l)
            continue
        elif 'remove' in user_input:
            a = user_input.split()
            remove_list(int(a[1]))
        elif 'append' in user_input:
            a = user_input.split()
            append_list(int(a[1]))
        elif 'sort' == user_input:
            l.sort()
        elif 'pop' == user_input:
            l.pop()
        elif 'reverse' == user_input:
            l.reverse()
        N -= 1
