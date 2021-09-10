package newestPackage;

public class Exss {
    public static void main(String[] args) {
        ClassB nesne = new ClassB();
        System.out.println("2. nesne geldi.");
        ClassB nesne2 = new ClassB();



    }
}

class ClassA{

    int i = 10;

    {
        System.out.println("A'nın Initialization blok çalıştı.");
    }

    static{
        System.out.println("A'nın statik bloğu çalıştı.");
    }



    public ClassA(){
        System.out.println("A sınıfı nesnesi oluşturuldu.");
    }



}

class ClassB extends ClassA{

    int i = 20;

    static{
        System.out.println("B sınıfı statik bloğu.");
    }

    {
        System.out.println("B'nin initialization bloğu.");
    }

    public ClassB(){
        System.out.println("B sınıfı nesnesi oluşturuldu.");
        }
}


