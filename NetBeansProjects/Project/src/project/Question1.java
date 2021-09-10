// Muhammed Ulvi Özkaya 180315041
package project;




public class Question1 {
    
        
        
        
        
    

    public static void main(String[] args) {
        
        displayPattern(9);
        
        
    }
    public static void displayPattern(int n) {
        int i;
        int j;
        int k;
        int value = 1;

        for (i = 1; i < (n + 1); i++) {
            if (i < (n + 1) / 2) {
                k = i;
            } else {
                k = n - i + 1;
            }
            for (j = 1; j < (k + 1); j++) {
                System.out.print(value * value + " ");
                value += 2;

            }
            value = 1;
            System.out.println("");
        }
    }
}
    
    

