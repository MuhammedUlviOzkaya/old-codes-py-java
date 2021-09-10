package newestPackage;

import java.util.ArrayList;

public class Questions {
    public static void main(String[] args){
        MyStack myStack = new MyStack();

        Ogrenci ogr1 = new Ogrenci("Buz",20,1343145,560);

        myStack.push(ogr1);
        myStack.yazdir();

        Ogrenci ogr2 = new Ogrenci("Nur",25,21344143,272);
        Ogrenci ogr3 = new Ogrenci("Kaan",17,13243,679);
        Ogrenci ogr4 = new Ogrenci("Şam",20,124135,745);
        Ogrenci ogr5 = new Ogrenci("Asu",27,213413,683);

        myStack.push(ogr2);
        myStack.push(ogr3);
        myStack.push(ogr4);
        myStack.push(ogr5);

        myStack.yazdir();
        System.out.println("Our stack contains "+myStack.kacElemanVar()+" elements.");
        myStack.pop();

        myStack.yazdir();
        System.out.println("Our stack contains "+myStack.kacElemanVar()+" elements.");







    }


}

class MyStack{

    private ArrayList<Object> liste;

    public MyStack(){
        liste = new ArrayList<>();


    }

    public int kacElemanVar(){
        return liste.size();
    }

    public boolean bosMu(){
        if(liste.size()>0){
            return false;
        }else{
            return true;
        }

    }

    public Object elemanGoster(){
        return liste.get(kacElemanVar()-1);

    }

    public Object pop(){
        Object geriyeDondurulecekEleman = liste.get(kacElemanVar() - 1);
        liste.remove(kacElemanVar() - 1);
        return geriyeDondurulecekEleman;

    }

    public void push(Object eklenecekEleman){
        liste.add(eklenecekEleman);
    }

    public void yazdir(){
        System.out.println("--------------------YIĞIN İÇERİĞİ--------------------");
        for(int i = 0; i<liste.size(); i++){
            System.out.println(i+". indekste: "+liste.get(i));
        }


    }


}