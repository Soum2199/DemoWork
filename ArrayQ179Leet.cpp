class Solution {
public:
    string largestNumber(vector<int>& nums) {
        // Sort the numbers using Merge Sort
        nums = mergeSort(nums, 0, nums.size() - 1);
        // Concatenate sorted numbers to form the largest number
        string largestNum;
        for (int num : nums) {
            largestNum += to_string(num);
        }
        // Handle the case where the largest number is zero
        return largestNum[0] == '0' ? "0" : largestNum;
    }

private:
    vector<int> mergeSort(vector<int>& nums, int left, int right) {
        // Base case: a single element is already sorted
        if (left >= right) return {nums[left]};
        int mid = left + (right - left) / 2;
        // Recursively sort the left and right halves
        vector<int> leftHalf = mergeSort(nums, left, mid);
        vector<int> rightHalf = mergeSort(nums, mid + 1, right);
        // Merge the sorted halves
        return merge(leftHalf, rightHalf);
    }

    vector<int> merge(vector<int>& leftHalf, vector<int>& rightHalf) {
        vector<int> sortedNums;
        int leftIndex = 0, rightIndex = 0;
        // Merge the two halves based on custom comparison
        while (leftIndex < leftHalf.size() && rightIndex < rightHalf.size()) {
            if (compare(leftHalf[leftIndex], rightHalf[rightIndex])) {
                sortedNums.push_back(leftHalf[leftIndex++]);
            } else {
                sortedNums.push_back(rightHalf[rightIndex++]);
            }
        }
        // Append remaining elements from left half
        while (leftIndex < leftHalf.size())
            sortedNums.push_back(leftHalf[leftIndex++]);
        // Append remaining elements from right half
        while (rightIndex < rightHalf.size())
            sortedNums.push_back(rightHalf[rightIndex++]);
        return sortedNums;
    }

    bool compare(int firstNum, int secondNum) {
        // Compare concatenated strings to decide the order
        return to_string(firstNum) + to_string(secondNum) >
               to_string(secondNum) + to_string(firstNum);
    }
};

// The time complexity is approximately O(n log n * k) and the space complexity is O(n).