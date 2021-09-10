// Muhammed Ulvi Özkaya 180315041 FORMAL EDUCATION
package javaapplication1;

import java.util.Scanner;


public class JavaApplication1 {

    
    public static void main(String[] args) {
        maxNegative();
        
    }
    public static void maxNegative(){
        int numbers [] = new int [10];
        int max = Integer.MIN_VALUE;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter 10 value: ");
        for(int i = 0; i<numbers.length; i++){
            numbers[i] = input.nextInt();
            if(numbers[i]<0 && numbers[i]>max){
                max = numbers[i];
            }
        }
        System.out.println("Maximum negative value in the array is: "+max);
        
    }
    
    
}
