def solution(nums):
    select = len(nums) // 2
    nums = set(nums)

    if len(nums) >= select:
        return select
    else:
        return len(nums)