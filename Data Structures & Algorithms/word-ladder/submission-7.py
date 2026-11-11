from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # 1. build graph: connect words that differ by exactly one char
        adj_list = {beginWord: []}
        for word in wordList:
            if word in adj_list:          # skip dupes / beginWord so edges aren't wiped
                continue
            adj_list[word] = []
            for key in adj_list:
                if len(word) != len(key):
                    continue
                difference = 0
                for i in range(len(word)):
                    if word[i] != key[i]:
                        difference += 1
                if difference == 1:
                    adj_list[key].append(word)
                    adj_list[word].append(key)

        # 2. BFS: first time we reach endWord is the shortest path
        q = deque([(beginWord, 1)])
        seen = {beginWord}
        while q:
            node, dist = q.popleft()
            if node == endWord:
                return dist
            for next_node in adj_list[node]:
                if next_node not in seen:
                    seen.add(next_node)
                    q.append((next_node, dist + 1))
        return 0