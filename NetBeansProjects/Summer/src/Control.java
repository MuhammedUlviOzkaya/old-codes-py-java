

import java.util.Scanner;

public class Control {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = "apple";
        String res = "_ _ _ _ _";
        String guess;
        String temp;
        
        int choose, flag = 0;

        int count = str.length() * 2;
        char letter;

        while (count > 0) {
            System.out.println(res);
            System.out.println("\nEnter a letter. You have " + count + " left. Please enter 0 for guessing all word.");
            letter = scanner.nextLine().charAt(0);
            if (letter == '0') {
                System.out.println("\nPlease enter your guess: ");
                guess = scanner.nextLine();
                if (str.equals(guess)) {
                    System.out.println("\nCorrect! Please Enter 0 for replay or enter 1 for exit.");
                    choose = scanner.nextInt();
                    if (choose == 0) {
                        res = "_ _ _ _ _";
                        count = str.length() * 2;
                        System.out.println(res);
                        System.out.println("\nEnter a letter. You have " + count + " left. Please enter 0 for guessing all word.");
                        scanner.nextLine(); // enterı tutsun diye
                        letter = scanner.nextLine().charAt(0);

                    } else {
                        return;
                    }
                }
            }

            temp = res;
            res = compare(letter, str, res);

            if (res.equals(temp)) {
                count = count - 1;
            }
            if (count == 0) {
                System.out.println("\nYou did not find! Please Enter 0 for replay or enter 1 for exit.");
                choose = scanner.nextInt();
                if (choose == 0) {
                    res = "_ _ _ _ _";
                    count = str.length() * 2;
                    scanner.nextLine(); // enterı tutsun diye

                } else {
                    return;
                }
            }
            flag = 0;
            for (int k = 0; k < str.length(); k++){
                    if(str.charAt(k) == res.charAt(2 * k))
                        flag++;
            }
            if (flag == str.length()) {
                System.out.println("\nCorrect! Please Enter 0 for replay or enter 1 for exit.");
                choose = scanner.nextInt();
                if (choose == 0) {
                    res = "_ _ _ _ _";
                    count = str.length() * 2;

                    scanner.nextLine(); // enterı tutsun diye

                } else {
                    return;
                }
            }
        }

    }

    public static String compare(char a, String str, String res) {
        int i;
        int size = str.length();
        StringBuilder sb = new StringBuilder(res);
        for (i = 0; i < size; i++) {
            if (str.charAt(i) == a) {

                sb.setCharAt(i * 2, a);
            }
            
        }
        res = sb.toString();
        return res;
    }

}
