class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:

        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        
        cur.word = True

        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                ch = word[i]
                # ".ab"
                #  c -->{ a --> {b: {True }} }
                if ch == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                else:
                    if ch not in cur.children:
                        return False
                    cur = cur.children[ch]

            return cur.word
        return dfs(0, self.root)




'''

rather than just using hash mamp which typically stores 1 to 1 relationship
make a new object, and have it contain both a map + a boolean

'''