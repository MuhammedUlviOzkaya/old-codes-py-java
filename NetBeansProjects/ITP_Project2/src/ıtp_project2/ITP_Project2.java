// Muhammed Ulvi Özkaya 180315041 
package ıtp_project2;
import java.util.Scanner;

public class ITP_Project2 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String wordArray [] = {"apple","knife","shirt","shoe","monkey","map","door","bird","square","station","picture","pocket","brain","camera","ticket","train","spray","umrella","hospital","horse","hammer","scissors","whistle","cloud","cheese"};
        
        
        int indexOfWord = (int)(Math.random()*25);
        String str = wordArray[indexOfWord];
        String res = "";
        for(int x = 0; x<str.length(); x++){ //for creating space for letters of word.
            res += "_ ";
        }
        String result = res; 
        String guess;
        String temp;
        
        int choose, flag;

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
                        indexOfWord = (int)(Math.random()*25);
                        str = wordArray[indexOfWord];
                        res = "";
                        for(int y = 0; y<str.length(); y++){
            res += "_ ";
        }
                        
                        
                        
                        
                        count = str.length() * 2;
                        System.out.println(res);
                        System.out.println("\nEnter a letter. You have " + count + " left. Please enter 0 for guessing all word.");
                        scanner.nextLine();
                        letter = scanner.nextLine().charAt(0);

                    } else {
                        return;
                    }
                }
                else{
                    System.out.println("Wrong Guess!");
                }
            }

            temp = res;
            res = compare(letter, str, res);

            if (res.equals(temp)) {
                count = count - 1;
            }
            if (count == 0) {
                System.out.println("\nGame Over! Please Enter 0 for replay or enter 1 for exit.");
                choose = scanner.nextInt();
                if (choose == 0) {
                    indexOfWord = (int)(Math.random()*25);
                        str = wordArray[indexOfWord];
                        res = "";
                        for(int z = 0; z<str.length(); z++){
            res += "_ ";
        }
                    
                    
                    count = str.length() * 2;
                    scanner.nextLine(); 

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
                    indexOfWord = (int)(Math.random()*25);
                        str = wordArray[indexOfWord];
                        res = "";
                        for(int t = 0; t<str.length(); t++){
            res += "_ ";
        }
                    
                    
                    
                    count = str.length() * 2;

                    scanner.nextLine(); 

                } else {
                    return;
                }
            }
        }
        
        
        

    }

    public static String compare(char a, String str, String res) { //for replace letters and "_" symbols if the entered letters are true.
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
