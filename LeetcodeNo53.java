//   https://leetcode.com/problems/maximum-subarray/
 // Your code here
        int ans = Integer.MIN_VALUE;
        int sum = 0;
       for (int index = 0; index < arr.length; index++) {
          sum = Math.max(arr[index]+sum, arr[index]);
          ans = Math.max(sum, ans);
        }
        // return sum;
        return ans;

----------------------------------------------------------

class Solution {
    public int maxSubArray(int[] arr) {
        int ans = Integer.MIN_VALUE;
        int sum = 0;
       for (int index = 0; index < arr.length; index++) {
          sum = Math.max(arr[index]+sum, arr[index]);
          ans = Math.max(sum, ans);
        }
        // return sum;
        return ans;

    }
}