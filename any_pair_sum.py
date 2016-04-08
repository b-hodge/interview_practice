# Given a list of numbers and a target sum, display any one pair of numbers from the list whose sum is equal to the target
# Always returns the first pair totalling to the sum
def pairwise_sum(nums, t, debug):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if debug: print("Testing the sum of %d and %d." % (nums[i], nums[j]))
            if nums[i] + nums[j] == t:
                if debug: print("Found pair (%d, %d) summing to %d" % (nums[i], nums[j], t))
                return (nums[i], nums[j])
            if debug: print("The sum of %d and %d is not equal to the target." % (nums[i], nums[j]))

print("\nFirst test case")
assert pairwise_sum([1, 2, 3], 3, debug=True) == (1, 2)

print("\nSecond test case")
assert pairwise_sum([1, 2, 3, 5], 6, debug=True) == (1, 5)

print("\nThird test case")
assert pairwise_sum([1, 2, 3], 10, debug=True) == None

print("\nFourth test case")
assert pairwise_sum([1, 2, 3], 2, debug=True) == None
