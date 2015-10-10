# Cell class
class Cell():
    def __init__(self, v, quad, l):
        self.value = v              #int- current value of cell
        self.quadrants = quad       #list of int- valid quadrants
        self.loc = l[:]             #self's location in val[][]
        self.region = {}            #dict{int=list}-
        for q in quad:              #   adjacent cells in each quadrant
            self.region[q] = [l]

    # update all connected cells in quadrant q
    def update_region(self, q):
        global val, curr_age
        next_cells = self.region[q][:]
        while next_cells:
            curr_loc = next_cells.pop()
            if valid_loc(curr_loc):
                val[curr_loc[0]][curr_loc[1]].value = curr_age+1

    # expand region in quadrant q (add a diagonal border if valid)
    def expand_region(self, x, y, q):
        global N,M,val,start,curr_age
        #last recursion (terminate)
        if x - start[0] == curr_age:
            #if valid, add to region
            if valid_index(x,y) and [x,y] not in self.region[q]:
                self.region[q].append([x,y])
                return True
            else:
                return False
        #check current cell
        if valid_index(x,y) == False:
            return False
        #recurse
        if q%2 == 1:
            a = x+1
            b = y+1
        else:
            a = x+1
            b = y-1
        if self.expand_region(a,b,q) == False:
            return False
        else:
            self.region[q].append([x,y])
            return True


# Input
import sys
N, M = map(int, sys.stdin.readline().split())
val = []
tmp_sum = 0
for x in range (N):
    curr = sys.stdin.readline().strip()
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
            val[x][y] = Cell(1,list(curr_quad),[x,y])
            tmp_sum += 1
        else:
            val[x][y] = Cell(0,[],[x,y])

# if no footprints, ans = 0, exit
if tmp_sum == 0:
    print 0
    exit()


# Check valid quad and remove failed case
#tested - works
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

# [debug] check valid loc
def valid_loc(loc):
    global N,M
    if len(loc) != 2:
        return False
    x,y = loc
    return False if (x<0 or y<0 or x>=N or y>=M) else True

#loop
curr_age = 1
start = []
cont = True
while (cont):
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
                if val[x][y].expand_region(start[0],start[1],curr_q):
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

# final matrix
'''
for x in range (N):
    for y in range (M):
        sys.stdout.write(str(val[x][y].value))
    sys.stdout.write('\n')
'''
print (curr_age-1)
