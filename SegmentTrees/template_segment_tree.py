#Segment Tree Initialization

#Node initialization
class SegTreeNode:
    def __init__(self,val=0):
        self.val = val
        #identify what all elements should be present in the node like
        #value or value with some aggregate like xor/min and max etc.

    def get_val(self):
        return self.val
#THIS METHOD is to merge two segtree nodes
def merge(left: SegTreeNode, right: SegTreeNode) -> SegTreeNode:
    node = SegTreeNode()
    node.val = left.val + right.val #Determine the action to do
    return node


class SegmentTree:
    def __init__(self,arr) -> SegTreeNode:
        self.n = len(arr)
        self.arr = arr
        self.tree = [SegTreeNode()]*(4*self.n+1) #Segment tree array should be 4*N+1 to ensure we are covering all the cases
        #build segtree structure
        self.build(1,0,self.n-1)

    def build(self,idx,start,end):
        if start==end:
            #Leaf node: Directly assign value from array
            self.tree[idx] = SegTreeNode(self.arr[start])
        else:
            mid = (start+end)//2
            #Build left and right children
            self.build(2*idx,start,mid) #<-Left child
            self.build(2*idx+1,mid+1,end) #<-Right child
            self.tree[idx] = merge(self.tree[2*idx],self.tree[2*idx+1]) #Combine childern value to create the node

    def update(self,idx,start,end,pos,val): #Update the position with the val
        if start==end:
            #Leafnode, update the value
            self.tree[idx] = SegTreeNode(val)
        else:
            mid = (start + end) // 2
            # Update the correct child
            if pos <= mid:
                self.update(2 * idx, start, mid, pos, val)
            else:
                self.update(2 * idx + 1, mid + 1, end, pos, val)
            # Recompute the current node based on children
            self.tree[idx] = merge(self.tree[2 * idx], self.tree[2 * idx + 1])


    def query(self,idx,start,end,L,R): #query over range [L,R]
        if start>R or end<L: # Out of range boundary
            return SegTreeNode(0) #Return the identity element like 0 for sum or -1 for min/max

        if start>=L and end<=R:
            #means curr node is Fully within the required range
            return self.tree[idx] #return the node value

        #Partiallu within the range i.e. curr node contains part of the required range
        mid = (start+end)//2
        left_res = self.query(2*idx,start,mid,L,R) #Query in left child
        right_res = self.query(2*idx+1,mid+1,end,L,R)

        return merge(left_res,right_res)

    #Wrapper methods:
    def range_query(self,L,R):
        return self.query(1,0,self.n-1,L,R)

    def point_update(self,pos,val):
        return self.update(1,0,self.n-1,pos,val)

arr = [2,3,-1,5,-2,4,8,10]
seg_tree = SegmentTree(arr)

# Query range sum from index 1 to 4
print(seg_tree.range_query(1, 4).val)

seg_tree.point_update(3,10)

# Query again from index 1 to 4
print(seg_tree.range_query(1, 4).val)
