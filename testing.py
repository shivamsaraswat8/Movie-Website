class Tree:
    def __init__(self,val):
        self.val=val
        self.children={}
        self.end=False

class Trie:
    def __init__(self):
        self.root=Tree(None)


    def insert(self,word):
        parent=self.root
        for i,char in enumerate(word):
            if char not in parent.children:
                parent.children[char]=Tree(char)
            parent=parent.children[char]
            if i == len(word)-1:
                parent.end=True

    def search(self,word):
        parent=self.root
        for char in word:
            if char not in parent.children:
                return False
            parent=parent.children[char]
        return parent.end

    def startfrom(self,prefix):
        parent=self.root
        for char in prefix:
            if char not in parent.children:
                return False
            parent=parent.children[char]
        return True


r=Trie()
r.insert("mother")
r.insert("people")
r.insert("maa")
print(r.search("people"))
print(r.search("love"))
print(r.startfrom("pe"))
print(r.startfrom("re"))
print(r)
    
