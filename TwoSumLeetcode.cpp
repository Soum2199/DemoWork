// DSA using C++
//Leetcode Q.1  -  two sum
https://leetcode.com/problems/two-sum/description/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // return 5;
        for(int i=0; i<nums.size(); i++){
            for(int j=i+1; j<nums.size(); j++){
                if(nums[i]+nums[j] == target){
                    return {i,j};
                }
            }
        }
        return {-1, -1};
    }
};

//T.C. = Overall O(n^2),  S.C. = O(1)
//--------------------------------------------------------------------------------------------------------------------------

//java
// class Solution {
//     public int[] twoSum(int[] nums, int target) {

//         HashMap<Integer,Integer> map = new HashMap<>();
        
//         for(int i = 0;i<=nums.length;i++) {
//             int j = target - nums[i];

//             if (map.containsKey(j)) {
//                 return new int[] { map.get(j), i };
//             }
//             map.put(nums[i], i);
//         }
//         return new int[] {};
//     }
// }

//js
// var twoSum = function(nums, target) {
//     for (let i=0;i<nums.length-1;i++){
//             for (let j=i+1;j<nums.length;j++){
//                 if ((nums[i]+nums[j])==target){
//                     return [i,j];
//                 }
//             }
//         }
// };