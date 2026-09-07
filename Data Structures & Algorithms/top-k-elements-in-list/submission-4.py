class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: frequency map
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Step 2: buckets
        frq = [[] for _ in range(len(nums) + 1)]

        for num, c in count.items():
            frq[c].append(num)

        # Step 3: collect result
        res = []
        for i in range(len(frq)-1, 0, -1):
            for n in frq[i]:
                res.append(n)
                if len(res) == k:
                    return res
