
public class ListClass {
    public static void main(String [] args){
        int number = 20;
        for(int i = 2; i*i <= number; i++ ){
            while(number % i == 0){
                System.out.println(i+" and "+number);
                i++;
            }
            
        }
        
        
        
        
    } 
    
}
