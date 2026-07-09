# 1. Contains Duplicate | Arrays & Hashing
# Tetikleyici: "daha önce gördüm mü? sorusunu "
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False


solution_object = Solution()
nums = [1, 2, 3, 3]
sonuc = solution_object.hasDuplicate(nums)
print(f"Listede tekrar eden eleman var mı?: {sonuc}")

# --- İlk kendi çözümüm (brute force, O(n^2)) --- 
# for i in range(len(nums)):
    # for j in range(i+1, len(nums)):
        # if nums[i] == nums[j]:
            # return True
# return False