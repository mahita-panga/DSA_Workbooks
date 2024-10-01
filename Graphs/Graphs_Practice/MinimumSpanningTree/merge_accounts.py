"""
LC 721:
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially,
but all of their accounts definitely have the same name.
After merging the accounts,
return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Intuition:
•Treat each email as a unique node, and for each account, if two emails belong to the same account, we need to union them.
•The goal is to find connected components of emails that belong to the same account.
•Use Disjoint Set Union (DSU) to group emails based on shared ownership across different accounts.

Action Steps:
->Convert names to nodes. Maintain a nodemap to help us convert back nodes to names later
-> Create an email_map which contains the mail_id:node and if we encounter a duplicate mail id,
which means the mail id is already present for some node, then we union both these nodes i.e. duplicate mail wala and original
-> Once done, just iterate over mail_map so that we can construct the result:
    -> We will find ultimate parent of the node and keep adding the mails to the set
-> We create final list which converts parent node to name and sorts all the mails.
"""
class Disjoint_Set:
    def __init__(self, N):
        self.parent = [i for i in range(N+1)]
        self.size = [1] * (N+1)

    def get_parent(self):
        return self.parent

    def findUP(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findUP(self.parent[node])  # Path compression
        return self.parent[node]

    # Union by Size
    def UnionBySize(self, u, v):
        pu = self.findUP(u)
        pv = self.findUP(v)

        if pu != pv:  # They are in different sets
            # Attach the smaller tree under the larger tree
            if self.size[pu] < self.size[pv]:
                self.parent[pu] = pv  # Attach u's root to v's root
                self.size[pv] += self.size[pu]  # Update size of v's root
            else:
                self.parent[pv] = pu  # Attach v's root to u's root
                self.size[pu] += self.size[pv]  # Update size of u's root


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = Disjoint_Set(n*1000)
        nodes_map = {}
        mail_map = {}
        for i in range(n):
            nodes_map[i] = accounts[i][0]
            for mail in accounts[i][1:]:
                if mail not in mail_map:
                    mail_map[mail] = i
                else:
                    ds.UnionBySize(i,mail_map[mail])

        res = {}
        for mail,parent in mail_map.items():
            parent_id = ds.findUP(parent)
            if parent_id not in res:
                res[parent_id] = set([mail]) #DONT DO nodes_map[parent_id] here as it will remove duplicate keys.
            else:
                res[parent_id].add(mail)
        ans = []
        for pid,email in res.items():
            ans.append([nodes_map[pid]]+sorted(email))
        return ans
