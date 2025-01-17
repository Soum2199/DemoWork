//A sample java code below which was for a contest
//code below

public class CircularShift {

    public static String shiftString(String s, String direction) {
        StringBuilder shiftedString = new StringBuilder();

        for (char c : s.toCharArray()) {
            char newChar;
            if (direction.equals("left")) {
                // Shift left
                newChar = (char) ((c - 'a' - 1 + 26) % 26 + 'a');
            } else if (direction.equals("right")) {
                // Shift right
                newChar = (char) ((c - 'a' + 1) % 26 + 'a');
            } else {
                throw new IllegalArgumentException("Direction must be 'left' or 'right'");
            }
            shiftedString.append(newChar);
        }

        return shiftedString.toString();
    }

    public static void main(String[] args) {
        String s = "abcxyz";
        String leftShifted = shiftString(s, "left");
        String rightShifted = shiftString(s, "right");

        System.out.println("Original: " + s);
        System.out.println("Left Shifted: " + leftShifted);   // Output: "zabwyz"
        System.out.println("Right Shifted: " + rightShifted); // Output: "bcdyza"
    }
}

//	Thank  you!.