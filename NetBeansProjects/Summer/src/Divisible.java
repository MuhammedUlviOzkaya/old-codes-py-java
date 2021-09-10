
import java.util.ArrayList;


public class Divisible {

    public static void main(String[] args) {
        System.out.println(divisorCounter(12375));
        
        
        
    }
    public static int divisorCounter(int number){
        int controller = number;
        int divisors = 1;
        int isDivisible = 0;
        for(int i = 2; i <= number / 2; i++){
            int counter = 0;
            while(controller % i == 0){
                controller /= i;
                counter++;
                isDivisible++;
            }
            
            divisors *= (counter+1);
            
        }
        if(isDivisible == 0){
            return 2;
        }
        
        return divisors;
    }
}
