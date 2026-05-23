class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
      
        while i < len(arr)-1:
            j = i+1
            max_val = arr[j]
            while j < len(arr):
                 # these loop for all right greatest element
                if arr[j] > max_val:
                    max_val = arr[j]
                j += 1
            arr[i] = max_val
            i += 1
        arr[-1] = -1
        return arr

       