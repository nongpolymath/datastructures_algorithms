class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_string = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert_string(self, word):
        current = self.root
        for ch in word:
            node = current.children.get(ch)            
            if node is None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.end_of_string = True
        print("Successfully inserted")
        
    def search_string(self, word):        
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if node is None:
                return False
            current = node
        return current.end_of_string


def delete_string(root, word, index):
    if index == len(word):
        if root.end_of_string == True:
            root.end_of_string = False
            return True
        else:
            return False
    
    ch = word[index]
    child_node = root.children.get(ch)
    if child_node is None:
        return False
    
    can_delete = delete_string(child_node, word, index + 1)
    
    if can_delete:
        if not child_node.end_of_string and not child_node.children:
            del root.children[ch]
            return True
        else:
            return False
    else:
        return False


        

        
newTrie = Trie()
newTrie.insert_string("APP")
newTrie.insert_string("APPL")
print(newTrie.search_string("APPLE"))