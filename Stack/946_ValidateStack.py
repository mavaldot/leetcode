class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, 0
        stk = [-inf]
        while i < len(pushed):
            if popped[j] != stk[-1]:
                stk.append(pushed[i])
                i += 1
            else:
                stk.pop(-1)
                j += 1
            #print(stk)
        
        while j < len(popped):
            #print(stk)
            if popped[j] != stk[-1]:
                return False
            stk.pop(-1)
            j += 1
        
        return True