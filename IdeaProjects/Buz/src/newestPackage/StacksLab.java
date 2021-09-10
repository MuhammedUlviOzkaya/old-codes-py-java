package newestPackage;

import java.util.ArrayList;

public class StacksLab {

    public static void main(String [] args){
        StacksLab myStack = new StacksLab();

        String s = "Ben bir graffiti sanatçısıyım.";
        System.out.println(s);

        System.out.println(s.substring(4,8));




    }


    private ArrayList<Object> liste;

    public StacksLab(){
        liste = new ArrayList<>();
    }

    public int kacElemanVar(){
        return liste.size();
    }

    public boolean bosMu(){
        if(liste.size()>0){
            return true;
        }else return false;
    }

    public Object elemanGoster(){
        return liste.get(kacElemanVar()-1);
    }

    public Object pop(){
        Object dondurulecekEleman = liste.get(liste.size()-1);
        liste.remove(kacElemanVar()-1);
        return dondurulecekEleman;
    }

    public void push(Object eklenecekEleman){
        liste.add(eklenecekEleman);
    }

    public void yazdır(){
        System.out.println("**********************YIĞIN İÇERİĞİ**********************");
        for(int i = 0; i<liste.size(); i++){
            System.out.println(i+". indekste "+liste.get(i));
        }
    }


}
