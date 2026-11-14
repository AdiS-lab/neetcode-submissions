class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # mao(x:0, y:0)
        
        seen = {}
        res = []

        for i, ch in enumerate(s):
            if ch in seen:
                print(seen)
                start_ind, res_ind = seen[ch][0], seen[ch][1] 

                sub_str = s[start_ind:i+1]
                print(res_ind)
                print(res)

                res[res_ind] = len(sub_str)

                for v in set(sub_str):
                    seen[v] = [start_ind, res_ind]

                res = res[:res_ind+1]

            else:
                seen[ch] = [i, len(res)]
                res.append(1)

        return res