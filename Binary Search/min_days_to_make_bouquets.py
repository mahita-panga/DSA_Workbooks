"""
You are given an integer array bloomDay, an integer m and an integer k.
You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

"""
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        lb,ub = 0, max(bloomDay)+1
        def can_make_bouquet(mid):
            bq_cnt = 0
            cur_cnt = 0
            for i in bloomDay:
                if i<=mid: #flower bloomed
                    cur_cnt+=1
                else:
                    cur_cnt = 0
                if cur_cnt==k:
                    bq_cnt+=1
                    cur_cnt = 0
            return bq_cnt>=m


        while lb<ub: #We need min val in the search space, so we can use lb<ub check , range is right exclusive.
            mid = (lb+ub)//2
            if can_make_bouquet(mid):
                ub = mid
            else:
                lb = mid+1

        return lb
