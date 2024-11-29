"""
https://leetcode.com/problems/best-position-for-a-service-centre/

MATHEMATICAL APPROACH.
#https://leetcode.com/problems/best-position-for-a-service-centre/solutions/731717/python3-geometric-median

"""

class Solution:
    def get_eucledian_distance(self,x,y,positions):
        return sum([sqrt((x-xx)**2 + (y-yy)**2) for xx,yy in positions])

    def getMinDistSum(self, positions: List[List[int]]) -> float:

        #take center point, keep moving the point by some amount x and calculate the new distance, if new distance is small, update the candidate
        #amount x should be drcreased to a satisfied precision.

        x, y = sum(x for x, _ in positions)/len(positions), sum(y for _,y in positions)/len(positions)

        dist = self.get_eucledian_distance(x,y,positions)

        delta = 100 #based on constraint 0<x,y<100
        while delta > 1e-6:
            to_reduce = True
            for dx,dy in (-1,0),(0,-1),(0,1),(1,0):
                xx = x+dx * delta
                yy = y+dy * delta
                curr_dist = self.get_eucledian_distance(xx,yy,positions)
                if curr_dist < dist:
                    dist = curr_dist
                    x,y = xx,yy
                    to_reduce = False
                    break

            #Premature reduction of delta even when the improved delta is found, Instead check if reduction is needed
            if to_reduce:
                delta = delta/2

        return dist
