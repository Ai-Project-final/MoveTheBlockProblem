# abhi chalta kuch nai h....


class brick():
    def __init__(self, pos):

        self.size = (2, 1)
        self.gridpos = pos


def addbricks(arr, rows, cols):
    print(arr)
    f = open('brick.txt', 'r')
    lines = f.readlines()

    print(lines)
    i = j = 0
    for l in lines:

        for word in l:
            if(word == "\n"):
                pass
            else:
                # print(word)
                if(word == '.'):
                    arr[j][i] = brick((j, i))
                    print("adding at", i, j)
                else:
                    arr[j][i] = '0'
                print(arr[j][i], "    ", j, ' ', i)
                j += 1

        i += 1
        j = 0
    print(arr)
    draw(arr, rows, cols)


def draw(arr, rows, cols):
    i = j = 0
    for l in range(rows):
        st = ''
        for m in range(cols):
            if(arr[m][l] == '0'):
                st += " . "
            else:
                st += " B "
        print(st)


def maiin():
    rows, cols = (7, 8)
    arr = [[0]*rows]*cols
    arr = addbricks(arr, rows, cols)


maiin()
