package SummerPackage;

public class ClassJava {
    public static void main(String[] args) {
        int c = 20;
        while (1==1)
        {
            boolean all = true;
            for (int i = 1; i < 21; i++)
            {
                all = true;
                if ( c % i != 0 )
                {
                    all = false;
                    break;
                }
            }
            if ( all )
            {
                System.out.println( c );
                System.exit(0);
            }

            c++;
        }
    }
}
