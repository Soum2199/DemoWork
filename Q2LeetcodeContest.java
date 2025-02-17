/* Q2.
You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.
Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.
Answers within 10^(-5) of the actual answer will be accepted.

Example 1:
Input: squares = [[0,0,1],[2,2,1]]
Output: 1.0000

Example 2:
Input: squares = [[0,0,2],[1,1,1]]
Output: 1.16667
*/

import java.util.*;

public class SquareArea {
    public static double findYCoordinate(int[][] squares) {
        double totalArea = 0.0;
        List<double[]> events = new ArrayList<>(); // (y-coordinate, area)

        // Calculate total area and prepare events
        for (int[] square : squares) {
            int x = square[0], y = square[1], l = square[2];
            double area = l * l;
            totalArea += area;
            events.add(new double[]{y, area}); // Bottom-left corner
            events.add(new double[]{y + l, -area}); // Top-right corner
        }

        // Sort events by y-coordinate
        Collections.sort(events, Comparator.comparingDouble(a -> a[0]));

        double low = 0.0, high = totalArea;
        double targetArea = totalArea / 2.0;

        // Binary search for the y-coordinate
        while (high - low > 1e-7) {
            double mid = (low + high) / 2.0;
            double areaAbove = 0.0;

            // Calculate area above the mid line
            for (double[] event : events) {
                double y = event[0];
                double area = event[1];

                if (y > mid) {
                    areaAbove += area;
                }
            }

            if (areaAbove < targetArea) {
                low = mid; // Move up
            } else {
                high = mid; // Move down
            }
        }

        return low;
    }

    public static void main(String[] args) {
        int[][] squares1 = {{0, 0, 1}, {2, 2, 1}};
        System.out.printf("Output: %.4f\n", findYCoordinate(squares1)); // Output: 1.0000

        int[][] squares2 = {{0, 0, 2}, {1, 1, 1}};
        System.out.printf("Output: %.5f\n", findYCoordinate(squares2)); // Output: 1.16667
    }
}
