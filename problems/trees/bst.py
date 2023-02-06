class Empty:

    def __init__(self):
        # nothing to do!
        pass

    def is_empty(self):
        return True

    def is_leaf(self):
        return False

    def num_nodes(self):
        return 0

    def height(self):
        return 0

    def contains(self, n):
        return False

    def insert(self, n):
        return Node(n, Empty(), Empty())

    def inorder(self):
        return []

    def min_item(self):
        return None

    def max_item(self):
        return None

    def balanced_everywhere(self):
        return True
    
    def add_to_all(self, _):
        return Empty()

    def path_to(self, _):
        return None
    
    def __str__(self):
        return ""

class Node:

    def __init__(self, n, left, right):
        self.value = n
        self.left = left
        self.right = right

    def is_empty(self):
        return False

    def is_leaf(self):
        return self.left.is_empty() and self.right.is_empty()

    def num_nodes(self):
        return 1 + self.left.num_nodes() + self.right.num_nodes()

    def height(self):
        return 1 + max(self.left.height(), self.right.height())

    def contains(self, n):
        if n < self.value:
            return self.left.contains(n)
        elif n > self.value:
            return self.right.contains(n)
        else:
            return True

    def insert(self, n):
        if n < self.value:
            return Node(self.value, self.left.insert(n), self.right)
        elif n > self.value:
            return Node(self.value, self.left, self.right.insert(n))
        else:
            return self

    def inorder(self):
        if self.is_leaf():
            return [self.value]
        return self.left.inorder() + [self.value] + self.right.inorder()

    def min_item(self):
        if self.left.is_empty():
            return self.value
        return self.left.min_item()

    def max_item(self):
        if self.right.is_empty():
            return self.value
        return self.right.max_item()

    def balance_factor(self):
        return self.right.height() - self.left.height()

    def balanced_everywhere(self):
        bal = abs(self.balance_factor()) <= 1
        if self.is_leaf():
            return bal 
        return self.left.balanced_everywhere() and bal and self.right.balanced_everywhere()

    def add_to_all(self, val):
        bst = Empty().insert(self.value + val)
        bst.left = self.left.add_to_all(val)
        bst.right = self.right.add_to_all(val)
        return bst

    def path_to(self, val):
        if val == self.value:
            return [self.value]
        if val < self.value:
            return [self.value] + self.left.path_to(val)
        return [self.value] + self.right.path_to(val)

    def __str__(self):
        if self.is_leaf():
            return str(self.value)
        return str(self.value) + "\n" + str(self.left) + str(self.right)

if __name__ == "__main__":
    bst = Empty().insert(42).insert(10).insert(15).insert(63)

    print(f"The number of nodes is {bst.num_nodes()}")
    print(f"The height is {bst.height()}")
    print(bst.inorder())
    print(bst.min_item(), bst.max_item())
    print(bst.balance_factor())
    print(bst.balanced_everywhere())
    print(bst.add_to_all(10).inorder())
    print(bst.inorder())
    print(bst.path_to(15))
    print(bst)
