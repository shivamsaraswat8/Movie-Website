class Treenode:
    def __init__(self,value):
        self.value=value
        self.children={}
        self.endhere=False

class Trie:
     def __init__(self):
         '''Initialize data structure'''
         self.root=Treenode(None)

     def insert(self, word):
         '''Insert a word into the trir.
            :type word:str
            :rtype: void
         '''

         parent = self.root
         for i,char in enumerate(word):
             if char not in parent.children:
                 parent.children[char] = Treenode(char)
             parent = parent.children[char]
             if i == len(word)-1:
                 parent.endhere = True

     def search(self,word):
          '''
          Returns if the word is in the trie.
          :type word: str
          :rtype: bool
          '''

          parent = self.root
          for char in word:
              if char not in parent.children:
                  return False
              parent = parent.children[char]
          return parent.endhere

     def startswith(self, prefix):
          '''
          Returns if there is any word in the trie that starts with
          the given prefix
          :type  prefix:str
          :rtype: bool
          '''
          parent = self.root
          for char in prefix:
              if char not in parent.children:
                  return False
              parent = parent.children[char]
          return True



t=Trie()
t.insert("abcd")
t.insert("abe")
t.insert("people")
print(t.startswith("ta"))
