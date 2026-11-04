class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        #  sqrt((x1 - x2)^2 + (y1 - y2)^2
        # points[i] = [xi, yi]


        # O(n) + O(logn)

        res = [] # O(k) space

        for v in points:
            x1, y1 = v[0], v[1] 
            distance = math.sqrt((x1 - 0)**2 + (y1 - 0)**2)
            v.append(distance)
        
        print(points)

        res = sorted(points, key=lambda x: x[2]) # sorts ascending (closest distances)

        print(res)
        return [(x, y) for x, y, _ in res][:k]
 
    
            







        