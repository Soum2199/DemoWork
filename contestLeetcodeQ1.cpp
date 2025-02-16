/* Q1. given ana array of integers nums and an integer k, an element nums[i] is considered good if it is strictly greater than the elements at indices i-k and i+k (if those indices exist). If neither of these indices exist, nums[i] is still considered good. Return the sum of all good elements in the array.

Example 1:
Input: nums = [1,3,2,1,5,4], k=2
Output: 12
Explanation:
the good numbers are nums[1]=3, nums[4]=5 and nums[5]=4 because they are strictly greater than the numbers at indices i-k and i+k.

Example 2:
Input: nums = [2,1], k=1
Output: 2
Explanation:
the only good numbers are nums[0]=2 because it is greater than nums[1].
*/

#include <iostream>
#include <vector>

int sumOfGoodElements(const std::vector<int>& nums, int k) {
    int sum = 0;
    int n = nums.size();
    for (int i = 0; i < n; ++i) {
        bool isGood = true;

        // Check the left index (i - k)
        if (i - k >= 0 && nums[i] <= nums[i - k]) {
            isGood = false;
        }
        // Check the right index (i + k)
        if (i + k < n && nums[i] <= nums[i + k]) {
            isGood = false;
        }
        // If it is a good element, add to the sum
        if (isGood) {
            sum += nums[i];
        }
    }
    return sum;
}

int main() {
    std::vector<int> nums = {1, 3, 2, 1, 5, 4};
    int k = 2;
    std::cout << "Output: " << sumOfGoodElements(nums, k) << std::endl; // Output: 12

    nums = {2, 1};
    k = 1;
    std::cout << "Output: " << sumOfGoodElements(nums, k) << std::endl; // Output: 2

    return 0;
}
