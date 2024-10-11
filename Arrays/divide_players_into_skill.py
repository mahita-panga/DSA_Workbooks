"""
2491. Divide Players Into Teams of Equal Skill
You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.
The chemistry of a team is equal to the product of the skills of the players on that team.
Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.


Example 1:

Input: skill = [3,2,5,1,3,4]
Output: 22
Explanation:
Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.


Intuition:
    -> Came up with a 2-sum pairs logic.  Identify each team skill and accordingly
    pair up the teams.
    TC: O(N), SC:O(N)

    THERE is a better approach : 2pointer
    sort the array   -> [1,2,3,3,4,5]
    Pair lower skill with higher skill players ->(1,5)(2,4)(3,3)
    In case any pair does not have req sum, return -1 as pairing is not possible.

"""
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total_skill = sum(skill)
        n = len(skill)
        teams = n//2
        team_skill = total_skill//teams

        if n==2:
            return skill[0]*skill[1]

        if total_skill%teams !=0:
            return -1

        pair_sum = {}
        chem = 0
        for i in skill:
            if i in pair_sum and pair_sum[i] > 0:
                chem += i*(team_skill-i)
                pair_sum[i]-=1
            else:
                if team_skill-i in pair_sum:
                    pair_sum[team_skill-i]+=1
                else:
                    pair_sum[team_skill-i] = 1

        if any(count > 0 for count in pair_sum.values()):
            return -1

        return chem

class TwoPtrSolution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Step 1: Sort the skill array
        skill.sort()

        total_skill = skill[0] + skill[-1]  # Required sum for each pair
        chemistry_sum = 0

        # Step 2: Pair players using two pointers
        for i in range(len(skill) // 2):
            # Check if the sum of current pair matches the required total_skill
            if skill[i] + skill[-i - 1] != total_skill:
                return -1  # Invalid configuration, return -1
            # Calculate the chemistry (product of pair) and add it to the sum
            chemistry_sum += skill[i] * skill[-i - 1]

        return chemistry_sum  # Return total chemistry
