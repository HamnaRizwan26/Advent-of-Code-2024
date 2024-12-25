import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Day2Part2 {

    // Method to check if a report is safe
    public static boolean isSafe(int[] levels) {
        for (int i = 0; i < levels.length - 1; i++) {
            int diff = Math.abs(levels[i] - levels[i + 1]);
            if (diff < 1 || diff > 3) return false; // Adjacent levels must differ by 1 to 3
        }
        return isIncreasing(levels) || isDecreasing(levels); // Must be all increasing or all decreasing
    }

    // Check if levels are strictly increasing
    public static boolean isIncreasing(int[] levels) {
        for (int i = 0; i < levels.length - 1; i++) {
            if (levels[i] >= levels[i + 1]) return false;
        }
        return true;
    }

    // Check if levels are strictly decreasing
    public static boolean isDecreasing(int[] levels) {
        for (int i = 0; i < levels.length - 1; i++) {
            if (levels[i] <= levels[i + 1]) return false;
        }
        return true;
    }

    // Check if the report becomes safe after removing one level
    public static boolean isSafeWithOneRemoval(int[] levels) {
        for (int i = 0; i < levels.length; i++) {
            int[] modified = new int[levels.length - 1];
            int index = 0;
            for (int j = 0; j < levels.length; j++) {
                if (j != i) modified[index++] = levels[j]; // Copy all elements except the one being removed
            }
            if (isSafe(modified)) return true;
        }
        return false;
    }

    public static void main(String[] args) {
        List<int[]> reports = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader("input.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] levelsStr = line.split("\\s+"); // Split by spaces
                int[] levels = Arrays.stream(levelsStr).mapToInt(Integer::parseInt).toArray();
                reports.add(levels);
            }
        } catch (IOException e) {
            System.err.println("Error reading the file: " + e.getMessage());
            return;
        }

        int safeCount = 0;
        for (int[] report : reports) {
            // Check if the report is safe directly or becomes safe by removing one level
            if (isSafe(report) || isSafeWithOneRemoval(report)) {
                safeCount++;
            }
        }

        System.out.println("Safe reports count: " + safeCount);
    }
}
