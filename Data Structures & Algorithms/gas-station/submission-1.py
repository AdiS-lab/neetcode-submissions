class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:    

        # so essentially only ONE walk through is needed 
        # if the sum loops back and doesn't reach the index it's looping for 
        # then can return - 1
        # if haven't looped and gas[i] < cost[i] then you can just continue


        # append to itself because only one loop matters
        for j in range(len(gas)):
            gas.append(gas[j])
            cost.append(cost[j])

        check = i =  0
        gas_sum = 0

        while check < (len(gas) / 2):
            cur_sum = gas[i] + gas_sum

            if cur_sum >= cost[i]:
                if i - (len(gas) / 2) == check:
                    return check
                else:    
                    gas_sum = cur_sum - cost[i]   

            else:
                check = i + 1
                print(check)
                gas_sum = 0
            
            i += 1

        return -1

                



        
        