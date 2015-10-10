# Cell class
class Cell():
    def __init__(self, v, quad, l):
        self.value = v              #int- current value of cell
        self.quadrants = quad       #list of int- valid quadrants
        self.loc = l[:]             #self's location in val[][]
        self.region = {}            #dict{int=list}-
        for q in quad:              #   adjacent cells in each quadrant
            self.region[q] = []

    # update all connected cells in quadrant q
    def update_region(self, q):
        global val, curr_age
        next_cells = self.region[q][:]
        next_cells.append(self.loc)
        while next_cells:
            curr_loc = next_cells.pop()
            val[curr_loc[0]][curr_loc[1]].value = curr_age+1

    # expand region in quadrant q (add a diagonal border if valid)
    def expand_region(self, q):
        global start,curr_age
        ret = True
        #check cells on border
        x = start[0]
        y = start[1]
        for i in range (curr_age+1):
            if valid_index(x,y) == False:
                ret = False
                break
            x += 1
            y = y+1 if q%2 == 1 else y-1
        #all cells on path valid
        if ret:
            x = start[0]
            y = start[1]
            for i in range (curr_age+1):
                if [x,y] not in self.region[q]:
                    self.region[q].append([x,y])
                x += 1
                y = y+1 if q%2 == 1 else y-1
        return ret

# Input
from sys import stdin
N, M = map(int, stdin.readline().split())
NM = min(N,M)
if NM == 1:
    print 1
    exit()
val = []
for x in range (N):
    curr = stdin.readline().strip()
    val.append([])

    # possible quadrants
    quadrants = set([1,2,3,4])
    if x-1 < 0:
        quadrants.discard(1)
        quadrants.discard(2)
    if x+1 >= N:
        quadrants.discard(3)
        quadrants.discard(4)

    for y in range (M):
        curr_quad = quadrants.copy()
        # possible quadrants for current cell
        if y-1 < 0:
            curr_quad.discard(3)
            curr_quad.discard(2)
        if y+1 >= M:
            curr_quad.discard(1)
            curr_quad.discard(4)

        # add Cell object to each val[][] cell
        val[x].append([])
        if curr[y] == '#':
            map_empty = False
            val[x][y] = Cell(1,list(curr_quad),[x,y])
        else:
            val[x][y] = Cell(0,[],[])


# Check valid quad and remove failed case
def valid_quad(x, y, quad):
    global N,M,val,start,curr_age
    if quad == 1:
        if x-curr_age < 0 or y+curr_age >= M  \
                or val[x-curr_age][y].value == 0 \
                or val[x][y+curr_age].value == 0:
            val[x][y].quadrants.remove(quad)
            return False
        else:
            start = [x-curr_age, y]
            return True
    if quad == 2:
        if x-curr_age < 0 or y-curr_age < 0 \
                or val[x-curr_age][y].value == 0 \
                or val[x][y-curr_age].value == 0:
            val[x][y].quadrants.remove(quad)
            return False
        else:
            start = [x-curr_age, y]
            return True
    if quad == 3:
        if x+curr_age >= N or y-curr_age < 0 \
                or val[x+curr_age][y].value == 0 \
                or val[x][y-curr_age].value == 0:
            val[x][y].quadrants.remove(quad)
            return False
        else:
            start = [x, y-curr_age]
            return True
    if quad == 4:
        if x+curr_age >= N or y+curr_age >= M \
                or val[x+curr_age][y].value == 0 \
                or val[x][y+curr_age].value == 0:
            val[x][y].quadrants.remove(quad)
            return False
        else:
            start = [x, y+curr_age]
            return True

# Check valid index
def valid_index(x,y):
    global N,M,val
    return False if (x<0 or y<0 or x>=N or y>=M or val[x][y].value == 0) else True


#loop
curr_age = 1
start = []
cont = True
while (cont and curr_age <= NM):
    # update each cell
    for x in range (N):
        for y in range (M):
            if val[x][y].value == 0:
                continue
            # update possible quads on the way -- tested, works
            next_quad = val[x][y].quadrants[:]
            while next_quad:
                valid_quad(x,y,next_quad.pop())
            # iterate through possible quads
            next_quad = val[x][y].quadrants[:]
            while next_quad:
                curr_q = next_quad.pop()
                if curr_q not in val[x][y].quadrants \
                        or valid_quad(x,y,curr_q) == False:
                    continue
                if val[x][y].expand_region(curr_q):
                    val[x][y].update_region(curr_q)

    # check terminating condition
    for i in range (N):
        if (cont == False):
            break
        for j in range (M):
            if val[i][j].value != 0 and val[i][j].value <= curr_age:
                cont = False
                break
    curr_age += 1

'''
# final matrix
for x in range (N):
    for y in range (M):
        sys.stdout.write(str(val[x][y].value))
    sys.stdout.write('\n')
'''
print (curr_age-1)
