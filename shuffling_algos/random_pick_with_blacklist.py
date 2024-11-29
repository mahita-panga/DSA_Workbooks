"""
https://leetcode.com/problems/random-pick-with-blacklist
given an integer n and an array of unique integers blacklist. Design an algorithm to pick a random integer in the range [0, n - 1] that is not in blacklist. Any integer that is in the mentioned range and not in blacklist should be equally likely to be returned.

Optimize your algorithm such that it minimizes the number of calls to the built-in random function of your language.


    arr - contains all elements not in blacklist
    Fisher yates shuffle to ensure all elements are placed in equal probability => arr[1,2,3..n]
    => probability of first element is 1/n, second element is 1/n-1 ... 1/1
    => total prob: 1/n!

    for j in range(len(self.arr)):
        rand_index = random.randint(j,len(self.arr)-1)
        self.arr[j],self.arr[rand_index] = self.arr[rand_index],self.arr[j]
    return self.arr[random.randint(0,len(self.arr)-1)]

    Above solution is not scalable, instead of storing the array, we can
    use a map-based approach

    create a map for blacklisted numbers to ensure whenever a blacklisted number is picked, we change it to the valid number range.
    So, whenever we pick a number randomly and if that number is in blacklisted range then we swap it with valid number
"""

class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.blacklist = set(blacklist)
        self.valid_range = n - len(blacklist)
        self.map = {}
        last = n-1
        for i in self.blacklist:
            if i<self.valid_range:
                # Find a number in the range [valid_range, n-1] not in blacklist
                while last in self.blacklist:
                    last-=1 #Pick a number from last which is not in blacklist set
                self.map[i] = last
                last-=1 #Move the range


    def pick(self) -> int:
        rand = random.randint(0, self.valid_range - 1)
        return self.map.get(rand,rand)
        #map.get(a,'0) => if a in map, get map[a] else return 0


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
