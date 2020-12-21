
# globals
rows, cols = (7, 8)


class brick():
    def __init__(self, pos, ty):

        self.gridpos = pos
        self.typ = ty
        self.orientation = ""

    def check_orientation(self, arr):
        c, r = self.gridpos
        if (c > 0):
            if(not (arr[r][c-1] == '0')):
                self.orientation = 'horizontal'
                self.linked = arr[r][c-1]
        if(r > 0):
            if(not (arr[r-1][c] == '0')):
                self.orientation = 'vertical'
                self.linked = arr[r-1][c]
        if(c < cols-1):
            if(not (arr[r][c+1] == '0')):
                self.orientation = 'horizontal'
                self.linked = arr[r][c+1]
        if(r < rows-1):
            if(not (arr[r+1][c] == '0')):
                self.orientation = 'vertical'
                self.linked = arr[r+1][c]


def addbricks():

    # print(arr)
    f = open('brick.txt', 'r')
    lines = f.readlines()
    array = []
    # print(lines)
    i = j = 0
    for l in lines:
        temp = []
        for word in l:
            if(word == "\n"):
                pass
            else:
                # print(word)
                if(word == ','):
                    temp.append(brick((j, i), 'main'))
                elif(word == '.'):
                    temp.append(brick((j, i), 'brick'))
                    #print("adding at", i, j)
                else:
                    temp.append('0')
                j += 1
        array.append(temp)

        i += 1
        j = 0
    draw(array, 1)

    return array


def draw(arr, state):
    i = j = 0
    for l in range(rows):
        st = ''
        for m in range(cols):
            arr
            if(arr[l][m] == '0'):
                st += " . "
            elif(arr[l][m].typ == 'main'):
                st += " M "
                if (state == 1):
                    arr[l][m].check_orientation(arr)
            elif(arr[l][m].typ == 'brick'):
                st += " B "
                if (state == 1):
                    arr[l][m].check_orientation(arr)
        print(st)


def move(arr, direction, pos):
    i, j = pos
    if(direction == '+' and not (arr[i][j] == '0')):
        if(arr[i][j].orientation == 'vertical'):
            k, l = arr[i][j].linked.gridpos
            if(l > i):
                # print(arr[i][j].linked.gridpos)
                arr[l+1][k] = arr[l][k]
                arr[l][k] = '0'
                arr[l+1][k].gridpos = (l+1, k)
                arr[i+1][j] = arr[i][j]
                arr[i][j] = '0'
                arr[i+1][j].gridpos = (i+1, j)

            if(l < i):
                # print(arr[i][j].linked.gridpos)
                arr[i+1][j] = arr[i][j]
                arr[i][j] = '0'
                arr[i+1][j].gridpos = (i+1, j)
                arr[l+1][k] = arr[l][k]
                arr[l][k] = '0'
                arr[l+1][k].gridpos = (l+1, k)

        if(arr[i][j].orientation == 'horizontal'):
            k, l = arr[i][j].linked.gridpos
            if(k > j):
                # print(arr[i][j].linked.gridpos)
                arr[l][k+1] = arr[l][k]
                arr[l][k] = '0'
                arr[l][k+1].gridpos = (l, k+1)
                arr[i][j+1] = arr[i][j]
                arr[i][j] = '0'
                arr[i][j+1].gridpos = (i, j+1)

            if(k < j):
                # print(arr[i][j].linked.gridpos)
                arr[i][j+1] = arr[i][j]
                arr[i][j] = '0'
                arr[i][j+1].gridpos = (i, j+1)
                arr[l][k+1] = arr[l][k]
                arr[l][k] = '0'
                arr[l][k+1].gridpos = (l, k+1)
    else:
        print("no brick at ", pos)

    if(direction == '-' and not (arr[i][j] == '0')):
        if(arr[i][j].orientation == 'vertical'):
            k, l = arr[i][j].linked.gridpos
            if(l < i):
                # print(arr[i][j].linked.gridpos)
                arr[l-1][k] = arr[l][k]
                arr[l][k] = '0'
                arr[l-1][k].gridpos = (l-1, k)
                arr[i-1][j] = arr[i][j]
                arr[i][j] = '0'
                arr[i-1][j].gridpos = (i-1, j)

            if(l > i):
                # print(arr[i][j].linked.gridpos)
                arr[i-1][j] = arr[i][j]
                arr[i][j] = '0'
                arr[i-1][j].gridpos = (i-1, j)
                arr[l-1][k] = arr[l][k]
                arr[l][k] = '0'
                arr[l-1][k].gridpos = (l-1, k)

        if(arr[i][j].orientation == 'horizontal'):
            k, l = arr[i][j].linked.gridpos
            if(k < j):
                # print(arr[i][j].linked.gridpos)
                arr[l][k-1] = arr[l][k]
                arr[l][k] = '0'
                arr[l][k-1].gridpos = (l, k-1)
                arr[i][j-1] = arr[i][j]
                arr[i][j] = '0'
                arr[i][j-1].gridpos = (i, j-1)

            if(k > j):
                # print(arr[i][j].linked.gridpos)
                arr[i][j-1] = arr[i][j]
                arr[i][j] = '0'
                arr[i][j-1].gridpos = (i, j-1)
                arr[l][k-1] = arr[l][k]
                arr[l][k] = '0'
                arr[l][k-1].gridpos = (l, k-1)
    else:
        print("no brick at ", pos)

    return arr


def check_goal():
    pass


def maiin():

    arr = addbricks()
    arr = move(arr, '+', (6, 1))
    print("\n\n\n\n")
    draw(arr, 0)


maiin()
