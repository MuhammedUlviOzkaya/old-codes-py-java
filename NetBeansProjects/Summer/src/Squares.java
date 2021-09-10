
public class Squares {
    public static void main(String[] args) {
        
        System.out.println(sumSquareDifference(1000));
        
    }
    
    public static int sumSquareDifference(int n){
        return (n * (n + 1) / 2) * (n * (n + 1) / 2) - n * (n + 1) * ((2 * n) + 1) / 6;
    }
    
    
}
