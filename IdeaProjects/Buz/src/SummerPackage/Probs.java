package SummerPackage;

public class Probs {
    public static void main(String[] args) {
        boolean control = true;
        int number = 20;
        while (1 == 1) {
            for(int i = 1; i <= 20; i++){
                if(number % i != 0){
                    control = false;
                    break;
                }

            }
            if(control){
                System.out.println(number);
                System.exit(0);

            }



            number++;

        }




    }
}

