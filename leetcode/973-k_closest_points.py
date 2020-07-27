import heapq

def kClosest(points: list(list()), K: int) -> list(list()):
    return heapq.nsmallest(K, points, lambda p: p[0] * p[0] + p[1] * p[1])

print(kClosest([[3,3],[5,-1],[-2,4]], 2))