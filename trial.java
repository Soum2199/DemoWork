// A Java program by me
// code below

class Solution {
    public int minArraySum(int[] nums, int k, int op1, int op2) {
        int n = nums.length;

        // Sort the array in ascending order to prioritize reducing larger elements
        Arrays.sort(nums);

        // Perform operations to minimize the sum
        for (int i = 0; i < n && k > 0; i++) {
            // Check if we can apply op2 (set to zero) or op1 (reduce by a value)
            if (op2 < nums[i]) {
                // If op2 is less than the current element, use op2
                nums[i] = op2;
                k--;
            } else if (op1 > 0) {
                // If we can reduce by op1, use op1
                nums[i] -= op1;
                // Ensure we don't go below zero
                if (nums[i] < 0) {
                    nums[i] = 0;
                }
                k--;
            }
        }
        // Calculate the minimum sum after operations
        int minSum = 0;
        for (int num : nums) {
            minSum += num;
        }
        return minSum;
    }
}
