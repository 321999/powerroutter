// we are going import list form java collection 
// instead of importing one by we will * to import 
import java.util.*;
public class LongestStringUsingJava {
    public static void main(String[] args) {
        // input of string 
        String input = "Welcome to PowerRouter";
      // converting string into an array of words 
        String[] words = input.split("\\s+");

        // List to store unique substrings without duplicates
        List<String> uniqueStrings = new ArrayList<>();

        for (String word : words) {
            // List to store characters of the current word without duplicates
            List<Character> newList = new ArrayList<>();
      // we are using list so we can use for each loop 
            for (char ch : word.toCharArray()) {
                // Logic to store only non-duplicate characters
                if (!newList.contains(ch)) {
                    newList.add(ch);
                } else {
                    newList.clear();
                    break;
                }
            }
            // Convert the list of characters to a string
            StringBuilder stringBuilder = new StringBuilder();
            for (char ch : newList) {
                stringBuilder.append(ch);
            }

            uniqueStrings.add(stringBuilder.toString());
        }

        // Find the maximum length string from the list
        int max = uniqueStrings.get(0).length();
        for (String str : uniqueStrings) {
            if (str.length() > max) {
                max = str.length();
            }
        }

        // Output the substring with the maximum length
        for (String str : uniqueStrings) {
            if (str.length() == max) {
                System.out.println("OUTPUT: " + str);
            }
        }
    }
}
