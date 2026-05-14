class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums += [val]
        self.nums = sorted(self.nums)
        return self.nums[-self.k]
