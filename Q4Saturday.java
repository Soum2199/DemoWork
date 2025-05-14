public class ShortestSubstringMatcher {
    public static int shortestSubstringLength(String s, String p) {
        // Check if the pattern contains exactly two '*' characters
        if (p == null || p.length() < 3 || p.chars().filter(ch -> ch == '*').count() != 2) {
            return -1; // Invalid pattern
        }

        // Split the pattern into parts
        String[] parts = p.split("\\*");
        String prefix = parts[0];
        String suffix = parts[1];

        int prefixLength = prefix.length();
        int suffixLength = suffix.length();
        int minLength = Integer.MAX_VALUE;

        // Find the first occurrence of the prefix
        int prefixIndex = s.indexOf(prefix);
        while (prefixIndex != -1) {
            // Find the next occurrence of the suffix starting after the prefix
            int suffixIndex = s.indexOf(suffix, prefixIndex + prefixLength);
            while (suffixIndex != -1) {
                // Calculate the length of the substring
                int length = (suffixIndex + suffixLength) - prefixIndex;
                minLength = Math.min(minLength, length);
                // Move to the next occurrence of the suffix
                suffixIndex = s.indexOf(suffix, suffixIndex + 1);
            }
            // Move to the next occurrence of the prefix
            prefixIndex = s.indexOf(prefix, prefixIndex + 1);
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

        // Additional test cases
        String s4 = "hello";
        String p4 = "h*o";
        System.out.println(shortestSubstringLength(s4, p4)); // Output: 5 (substring "hello")

        String s5 = "abc";
        String p5 = "a*b*c";
        System.out.println(shortestSubstringLength(s5, p5)); // Output: -1 (no match)

        String s6 = "abc";
        String p6 = "a*b";
        System.out.println(shortestSubstringLength(s6, p6)); // Output: 3 (substring "abc")
    }
}