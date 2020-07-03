class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None


    def insert_rec(self, point, value):
        if point == None:
            return Node(value)
        if value > point.value:
            point.right = self.insert_rec(point.right, value)
        if value < point.value:
            point.left = self.insert_rec(point.left, value)
        return point
        
    def insert(self, value):
        self.root = self.insert_rec(self.root, value)


    def pre(self,point):
        if point != None:
            print(point.value)
            self.pre(point.left)
            self.pre(point.right)

    def pre_order(self):
        print ("pre order values are:")
        self.pre(self.root)


    def in_o(self,point):
        if point != None:
            self.in_o(point.left)
            print(point.value)
            self.in_o(point.right)

    def in_order(self):
        print ("In order values are:")
        self.in_o(self.root)

    def post(self,point):
        if point != None:
            self.post(point.left)
            self.post(point.right)
            print(point.value)


    def post_order(self):
        print ("Post values are:")
        self.post(self.root)

    def rec_search(self, point, value):
        if point.value == value:
            return True
        if point == None:
            return False
        elif point.value > value:
            return self.rec_search(point.left, value)
        else:
            return self.rec_search(point.right, value)
                
    def search(self, value):
        return self.rec_search(self.root, value)
 

tree1 = Tree()
tree1.insert(7)
tree1.insert(6)
tree1.insert(5)
tree1.insert(4)
tree1.insert(3)
print(tree1.in_order())
print(tree1.search(6))