import * from package.util.*;
   
 public static int complementNumber(int x) {
        String numStr = String.valueOf(x);
        StringBuilder complementStr = new StringBuilder();
        
        for (char digit : numStr.toCharArray()) {
            complementStr.append(9 - (digit - '0'));  // Compute complement
        }
        
        return Integer.parseInt(complementStr.toString());  // Convert back to int to remove leading zeros
    }
    
    // Function to count valid pairs
    public static int countPairs(int[] arr) {
        int count = 0;
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arr[i] == complementNumber(arr[j])) {
                    count++;
                }
            }
        }
        return count;
    }
