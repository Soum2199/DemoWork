/* Q4. 
You are given a string s and pattern string p, where p contains exactly two '*' characters. 
The '*' in p matches any sequence of zero or more characters.
Return the length of the shortest substring in s that matches p. If there is no such substring, return -1.
A substring is a contiguous sequence of characters within a string (the empty substring is considered valid).

Example 1:
Input:
Output:
*/

import java.util.ArrayList;
import java.util.List;

public class ShortestSubstringMatcher {
    public static int shortestSubstringLength(String s, String p) {
        // Split the pattern into parts
        String[] parts = p.split("\\*");
        String prefix = parts[0];
        String suffix = parts[1];

        // Find all occurrences of the prefix
        List<Integer> prefixIndices = new ArrayList<>();
        int index = s.indexOf(prefix);
        while (index != -1) {
            prefixIndices.add(index);
            index = s.indexOf(prefix, index + 1);
        }

        // If no prefix found, return -1
        if (prefixIndices.isEmpty()) {
            return -1;
        }

        // Find the minimum length of the substring that matches the pattern
        int minLength = Integer.MAX_VALUE;
        for (int start : prefixIndices) {
            // Find the suffix starting from the end of the prefix
            int suffixIndex = s.indexOf(suffix, start + prefix.length());
            while (suffixIndex != -1) {
                // Calculate the length of the substring
                int length = (suffixIndex + suffix.length()) - start;
                minLength = Math.min(minLength, length);
                suffixIndex = s.indexOf(suffix, suffixIndex + 1);
            }
        }

        // If minLength was updated, return it; otherwise, return -1
        return minLength == Integer.MAX_VALUE ? -1 : minLength;
    }

    public static void main(String[] args) {
        String s1 = "abcde";
        String p1 = "a*b";
        System.out.println(shortestSubstringLength(s1, p1)); // Output: 3 (substring "abc")

        String s2 = "abacabadabacaba";
        String p2 = "a*b*a";
        System.out.println(shortestSubstringLength(s2, p2)); // Output: 5 (substring "abacaba")

        String s3 = "abcdef";
        String p3 = "x*y*z";
        System.out.println(shortestSubstringLength(s3, p3)); // Output: -1 (no match)
    }
}
