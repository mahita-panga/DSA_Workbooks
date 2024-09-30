"""
Disjoint Set -> Data Structure in Graphs which helps us identify if two components
of a dynamic graph(changing graph) are connected or not and helps us create a new
graph/union based on conditions

This DS has two major methods:
    ->Find:
        This helps us identify the ultimate parent of a certain node in the graph
    4
     \
      3             In this graph, if we do find(1) it will return the ultimate parent of 1
       \             This is done via recursion.
        2            Another intersting component is path compression,
         \            Once we find the ultimate parent of certain node, we will update the parent
          1           of this node to be pointed to the ultimate parent, so that next time we avoid recaluclation

    Pseudo-code:
        find(parent,X): #find ultimate parent of X. parent[] is the parent array which save the parent information.
            if parent[X]==X:
                return X   #The current node is parent of itself
            parent[X] = find(parent,parent[X])  #Path Compression Logic where I am updating the current node's parent to the ultimate parent
            return parent[X]
    ->Union:
        This is used to join two disconnected components together to form one huge graph.
        -> Union is done by Rank / Size
        UNION BY RANK:
            We maintain a rank array which depicts the rank/depth of the MST.
            We attach the smaller tree i.e. tree of lower rank with larger rank
            and in case if both ranks are same, then we can attach either of it

        ***NOTE: RANK is increased only when the two sets being merged have the same rank.
        This action is performed between two nodes u and v as:
            -> Find ultimate parents of u and v as pu, pv
            -> Get rank[pu] and rank[pv]
            -> Connect smaller rank to larger rank
            -> Update the rank only if the height of tree is going to increase

Ex dry run:
Nodes: (1,2)(2,3)(4,5)(1,5)    1-2 2-3 4-5 1-5
-> rank = [0,0,0,0,0], parent = [1,2,3,4,5] //Initially every node is a parent of itself
-> Union(1,2): pu=p[1]=1, pv=p[2]= 2 , r[pu]=0,r[pv]=0 => either can be attached.
Attach 2 to 1:  p[2]= 1 => parent = [1,1,3,4,5]
                and rank[1] = 0+1 =1 //since depth of 1 is there
                => rank=[1,0,0,0,0]
1
 \
  2

-> Union(2,3): pu=p[2]=1, pv = p[3]=3, r[pu]=r[1]=1, r[pv]=r[3]=0 => Attach 3 to 1
Attach 3 to 1: p[3] = 1 => parent=[1,1,1,4,5]
                rank remains same
1
|\
2 3
->Union(4,5): pu = p[4]=4, pv=5, r[4]==r[5]//both 0,either can be attached
Attach 5 to 4: p[5] = 4 => parent = [1,1,1,4,4]
                rank[4] = +1 as depth increased and both had same ranks
4
 \
  5
->Union(1,5): pu = p[1]=1, pv = p[5]=4, r[1]==r[4]//both 1, either can be attached
Attaching 4 to 1: p[4]=1 =>parent = [1,1,1,1,4]
                rank[1] = +1 as depth increased and both 1&4 had same ranks.
                rank = [2,0,0,1,0]
Final MST:
    1
   /|\
  2 3 4
       \
        5
=> When doing find, we can perform path compression to help us quickly identify the parent.
NOTE: Do not update rank when doing path compression.


UNION BY SIZE:
    -> Instead of rank, we maintain a size array which tells us the size of the MST or the number of nodes in MST
    This is much more intuitive to us rather than rank because after path compression, rank is distorted.


"""
class DSU:
    def __init__(self, N):
        # Initially, each element is its own parent
        self.par = list(range(N + 1))
        # Initially, each element has a rank of 0
        self.rank = [0] * (N + 1)
        self.size = [1]*(N+1)

    # Find the ultimate parent (with path compression)
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])  # Path compression
        return self.par[x]

    # Union two sets by rank
    def unionByRank(self, x, z):
        rootX = self.find(x)
        rootZ = self.find(z)

        if rootX != rootZ:  # Only union if they're in different sets
            # Union by rank
            if self.rank[rootX] > self.rank[rootZ]:
                self.par[rootZ] = rootX
            elif self.rank[rootX] < self.rank[rootZ]:
                self.par[rootX] = rootZ
            else: #if ranks are equal
                self.par[rootZ] = rootX
                self.rank[rootX] += 1
    #Union By SIZE
    def unionBySize(self, x, z):
         rootX = self.find(x)
         rootZ = self.find(z)

         if rootX != rootZ:  # Only union if they're in different sets
             if self.size[rootX] > self.size[rootZ]:
                 self.par[rootZ] = rootX
                 self.size[rootZ] += self.size[rootX]
             else: #No need to check other case because
                 self.par[rootX] = rootZ
                 self.size[rootX] += self.size[rootZ]

# Function to process the operations
def processQueries(N, queries):
    dsu = DSU(N)

    for query in queries:
        operation = query[0]

        if operation == "UNION":
            X = query[1]
            Z = query[2]
            dsu.union(X, Z)

        elif operation == "FIND":
            X = query[1]
            print(dsu.find(X))

# Example Usage:
N = 5
queries = [
    ("UNION", 1, 2),
    ("FIND", 2),
    ("UNION", 3, 4),
    ("FIND", 4),
    ("UNION", 2, 3),
    ("FIND", 3),
    ("FIND", 1)
]

processQueries(N, queries)
