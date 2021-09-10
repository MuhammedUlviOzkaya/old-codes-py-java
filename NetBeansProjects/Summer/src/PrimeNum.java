
public class PrimeNum {
    public static void main(String [] args){
        
        int primeCounter = 0;
        int prime = 2;
        while(primeCounter != 1000000){
            if((isPrime(prime))){
                primeCounter++;
            }
            prime++;
        }
        System.out.println("10001st prime number is: " + (prime - 1));
        
        }
    
    public static boolean isPrime(int num){
        
        for(int i = 2; i <= num/2; i++){
            if(num % i == 0){
                return false;
            }
        }
        return true;
    }
    
    
    
    
    
}
