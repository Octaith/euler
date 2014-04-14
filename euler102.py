from __future__ import division

with open('triangles.txt') as f:
    s = f.read().split('\n')[:-1]

tr = []
for r in s:
    tr.append([int(i) for i in r.split(',')])


# http://en.wikipedia.org/wiki/Barycentric_coordinate_system#Determining_whether_a_point_is_inside_a_triangle
def check(t):
    x, y = 0, 0
    x1, y1, x2, y2, x3, y3 = t
    det = (y2-y3)*(x1-x3) + (x3-x2)*(y1-y3)
    l1 = ((y2-y3)*(x-x3) + (x3-x2)*(y-y3))/det
    l2 = ((y3-y1)*(x-x3) + (x1-x3)*(y-y3))/det
    l3 = 1 - l1 - l2
    # print l1, l2, l3
    return 0 <= l1 <= 1 and 0 <= l2 <= 1 and 0 <= l3 <= 1


print sum(check(t) for t in tr)
