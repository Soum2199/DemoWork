//Just a binary search code its
class Solution {
    public int[] twoSum(int[] numbers, int target) {
          while (left <= right) {
            int mid = left + (right - left) / 2;
            long long midSquared = (long long)mid * mid; // Use long long to prevent overflow

            if (midSquared == x) {
                return mid; // Found the exact square root
            } else if (midSquared < x) {
                left = mid + 1; // Move to the right half
            } else {
                right = mid - 1; // Move to the left half
            }
        }
        return right; // The largest integer whose square is <= x
    }
}

//Dated 21/01/2025