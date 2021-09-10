// Muhammed Ulvi Özkaya 180315041
package project;

import java.util.Scanner;


public class Question3 {
    public static void main(String[] args) {
        String s;
        Scanner data = new Scanner(System.in);
        System.out.print("Enter the Account Number: ");
        s = data.nextLine();
        if (IsAccountValid(s)) {
            System.out.println("The Account Number " + s + " is valid!");
        } else {
            System.out.println("The Account Number " + s + " is invalid!");
        }
    }
    public static boolean IsAccountValid(String s) {
        int i;
        int temp;
        int res1 = 0;
        int res2 = 0;
        int total;
        int k;
        if (s.length() != 16) {
            return false;
        }
        if (s.charAt(0) >= s.charAt(1) || s.charAt(0) > 'a' && s.charAt(0) < 'z' || s.charAt(1) > 'a' && s.charAt(1) < 'z') {
            return false;
        }
        for (k = 2; k < 4; k++) {
            if (!IsPrime(s.charAt(k))) {
                return false;
            }
        }
        for (i = 4; i < 16; i++) {
            if (i % 2 == 0) {
                temp = (s.charAt(i) - 48) * 2;
                if (temp >= 10) {
                    temp = (temp % 10) + (temp / 10) % 10;
                }
                res1 += temp;
            } else {
                res2 += s.charAt(i) - 48;
            }

        }
        total = res1 + res2;
        if (total % 10 != 0) {
            return false;
        }

        return true;
    }

    public static boolean IsPrime(char c) {
        int k = c - 48;
        int i;
        for (i = (k - 1); i > 1; i--) {
            if (k % i == 0) {
                return false;
            }
        }
        return true;
    }
    
}
