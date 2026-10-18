class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        window_count = {}

        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1

        # build first window
        for c in s2[:len(s1)]:
            window_count[c] = window_count.get(c, 0) + 1

        if window_count == s1_count:
            return True

        # slide the window: add one right, remove one left
        for i in range(len(s1), len(s2)):
            # add new char on right
            window_count[s2[i]] = window_count.get(s2[i], 0) + 1

            # remove old char on left
            old = s2[i - len(s1)]
            window_count[old] -= 1
            if window_count[old] == 0:
                del window_count[old]

            if window_count == s1_count:
                return True

        return False