// Muhammed Ulvi Özkaya 180315041
package project;


public class Question2 {
    
    
    public static void main(String[] args) {
        String s = "The deadline for Introduction to Programming Project1 is December 20, 2019.";
        System.out.println(wordsCount(s));
        System.out.println(charachtersCount(s));
        System.out.println(digitCount(s));
        System.out.println(firstNonRepating(s));
        System.out.println(findfreqOfo(s));

    }
    public static int wordsCount(String s) {
        String[] temp;
        temp = s.split(" ");
        return temp.length;
    }

    public static int charachtersCount(String s) {
        String[] temp;
        temp = s.split(" ");
        return s.length() - temp.length - 1;
    }

    public static int digitCount(String s) {
        int size = s.length();
        int i;
        int count = 0;

        for (i = 0; i < size; i++) {
            if (s.charAt(i) >= '0' && s.charAt(i) <= '9') {
                count++;
            }
        }
        return count;
    }

    public static char firstNonRepating(String s) {
        int size = s.length();
        String s1 = s.toLowerCase();
        int i;
        int j;
        int count = 0;
        for (i = 0; i < size; i++) {
            for (j = 0; j < size; j++) {
                if (i != j) {
                    if (s1.charAt(i) != s1.charAt(j)) {
                        count++;
                    }
                }

            }
            if (count == (size - 1)) {
                return s.charAt(i);
            } else {
                count = 0;
            }
        }
        return 'x';
    }

    public static int findfreqOfo(String s) {
        int size = s.length();
        int i;
        int count = 0;
        for (i = 0; i < size; i++) {
            if (s.charAt(i) == 'o') {
                count++;
            }
        }
        return count;
    }
}
