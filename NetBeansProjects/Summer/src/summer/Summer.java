
package summer;


public class Summer {

    
    public static void main(String[] args) {
        
        System.out.println(largestPalindrome(999, 999));
       
       
       
}
    
    public static int reverse(int number){
        int reversed = 0;
        int reduced;
        
        while(number > 0){
            reduced = number % 10;
            reversed = (reversed * 10) + reduced;
            number = number / 10;
        }
        return reversed;
    }
    
    public static boolean isPalindrome(int number){
        return reverse(number) == number;
    }
    
    public static int largestPalindrome(int a, int b){
        int result = 0;
        int largest = 0;
        for(int i = a; i >= 0; i--){
            for(int j = b; j >= 0; j--){
                result = i * j;
                if(isPalindrome(result)){
                    largest = Math.max(largest, result);
                }
            }
        }
        return largest;
    }
    
    
    
    
}
    
    
