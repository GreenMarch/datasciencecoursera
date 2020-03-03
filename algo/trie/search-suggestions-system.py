class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.suggestions = []


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word):
        root = self.root
        for char in word:
            print("char", char)
            if char not in root.children:
                root.children[char] = Node(char)  # -- add node

            if len(root.suggestions) < 3:
                root.suggestions.append(word)  # ------ add suggestions

            # move further down
            root = root.children[char]

            # don't forget last node
        if len(root.suggestions) < 3:
            print("last node char", char)
            root.suggestions.append(word)

    def find(self, word):
        root = self.root
        res = []  # - collect the suggestions
        for i, char in enumerate(word):
            if char in root.children:
                root = root.children[char]  # - locate char node
                res.append(root.suggestions)  # - append its suggestions
            else:
                break  # -------------- II
        remaining = len(word) - len(res)
        for j in range(remaining):
            res.append([])

        return res


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        # edge cases:
        if len(products) == 1 and products[0] == searchWord:
            return [[searchWord] for i in range(len(searchWord))]

        products.sort()  #
        trie = Trie()
        for product in products:
            trie.insert(product)
        return trie.find(searchWord)

    # Comment - II
# We want to make sure we add an empty list for every character that does not exist down the path we are traversing in the trie
# Once you encounter a char that is not in the same trie path. In other words,
# as soon as the word devaite from the product, you terminate the loop and
# append m empty lists where m is the number of chars remaning in the product name
#  example:
# ["moan"], "mouse"
# [["moan"],["moan"],[],[],[]]