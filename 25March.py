file=open("./test/test.txt","r")

first_line= file.readline()
print("Total Number of rectangles: {}".format(first_line))

data_chunk=[]
for rest_line in file.readlines():  # read rectangles into the nested list
    lst = []
    for num in rest_line.split():
        lst.append(float(num))
    data_chunk.append(lst)
"""
To compare rectangel rec2 and rec1, if it is nested or not.

Output: True, it means rec2 inside rec1
Input: rec2, rec1
"""
def check_rec_inside(rec1,rec2):
    tl = (rec1[0]<rec2[0] and rec1[1] < rec2[1] )  # compare minimum corner, top left
    br = (rec1[2]>rec2[2] and rec1[3] > rec2[3] )  # compare maximum corner, bottom right
    return tl and br


"""
find all boxes that contains rec1

Output: index of all boxes from the original chunk
Input: rec1, current rectangle
Input: arr-> all the data chunks
"""
def find_containing(rec1, arr):
    res = []
    i=0
    for num in arr:
        if (check_rec_inside(num,rec1)):
            res.append(i)
        i=i+1
    return res

"""
It find the smallest box

Output: index of the minimum
Input chunk: actual datachunk value
Input: arr is index list
"""
def find_minimum(arr, chunk):
    min_obj = -1
    min_size = 30000000
    i = 0
    for num in arr:
        sz = (chunk[num][2]-chunk[num][0])*(chunk[num][3]-chunk[num][1])
        if (min_size>sz):
            min_size = sz
            min_obj = num
        i = i + 1
    return min_obj

"""
Finding the smallest element that is a parent of current element
This create a tree struecture in an array. the array has its internal dependency.
parent rectangle(bigger box) default index is set to -1, and its child index value indicate its parent list index at 
the datachunk 
This function try to find all parents of index list

Output: indexes of parents
Input: arr is actual datachunk 
"""
def find_parent(arr):
    res = []
    for val in arr:
        i = find_minimum(find_containing(val,arr),arr)
        res.append(i)
    return res

"""
Finding distance, for larger dataset, this could be issue, because of running of stack. due to recursion
root distance should set to 0, this is determined by -1 from input parent indexes
child distance add incremental 1, which is determined by its parents

Output: distance count
Input: parent, parent indexes
Input: i index of the current item
"""
def find_distance_from_root(parent, i):
    if (parent[i]==-1):
        return 0
    return 1+find_distance_from_root(parent,parent[i])


"""
Finding all the distances from the root
Output: all the distances of the nodes from the root
Input, Parent is parent indexes
"""
def find_distances(parent):
    i=0
    res=[]
    for num in parent:
        res.append(find_distance_from_root(parent,i))
        i=i+1
    return res

"""
Assume that the root rectangle is 0, its child rectangle is sea, its child's child rectangle is land ....
Count the even indexes, which is the land
"""
def count_even_node(lst):
    sum=0
    for item in lst:
        if item %2 ==0:
            sum=sum+1
    return sum


#print(find_parent(data_chunk))
#print(find_distances(find_parent(data_chunk)))
print("Number of lands found: ", count_even_node(find_distances(find_parent(data_chunk))))