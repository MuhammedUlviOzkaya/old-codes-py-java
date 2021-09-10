import java.util.*;
public class DivisibleNum {
    public static void main(String[] args) {
        
        int limit = 10;
        
        primeDivisors(limit);
        
        
        
    }
    
    public static void primeDivisors(int number){
        int controller = number;
        for(int i = 2; i < number; i++){
            if(number % i == 0){
                int counter = 0;
                while(number % i == 0){
                    controller = controller / i;
                    counter++;
                }
                System.out.print(i+"^"+counter+"x");
                number = controller;
            }
            
        }
    }
}
