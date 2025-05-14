import java.util.List;

class Solution {
    public int minimumSumSubarray(List<Integer> nums, int l, int r) {
        int n = nums.size();
        if (n == 0 || l > n || r < 1 || l > r) {
            return 0; // Edge case handling
        }
        
        int minSum = Integer.MAX_VALUE;
        
        // Use a sliding window approach to find the minimum sum of subarrays
        for (int length = l; length <= r; length++) {
            int currentSum = 0;
            
            // Calculate the sum of the first 'length' elements
            for (int i = 0; i < length; i++) {
                currentSum += nums.get(i);
            }
            minSum = Math.min(minSum, currentSum);
            
            // Slide the window across the array
            for (int i = length; i < n; i++) {
                currentSum += nums.get(i) - nums.get(i - length);
                minSum = Math.min(minSum, currentSum);
            }
        }
        
        return minSum;
    }
}