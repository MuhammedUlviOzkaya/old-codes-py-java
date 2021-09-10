package com.company;
import java.util.*;

public class Ters {
    public static void main(String[] args) {
        Student tumOgrenciler[] = new Student[100];
        for(int i = 0; i<100; i++){
            int rastgeleID = (int)(Math.random()*5000);
            int rastgeleNotDegeri = (int)(Math.random()*100);

            Student yeni = new Student(rastgeleID, rastgeleNotDegeri);
            tumOgrenciler[i] = yeni;





        }
        ogrenciSirala(tumOgrenciler);
        for(int i = 0; i<100; i++){
            tumOgrenciler[i].ogrenciBilgileri();
        }



    }

    public static void ogrenciSirala(Student[] tumOgrenciler){
        for(int i = 0; i<tumOgrenciler.length-1; i++){
            int oAnkiEnKucukNot = tumOgrenciler[i].getNotDegeri();
            int oAnkiEnKucukNotunIndex = i;

            for(int j = i+1; j<tumOgrenciler.length-1; j++){
                if(oAnkiEnKucukNot < tumOgrenciler[j].getNotDegeri()){
                    oAnkiEnKucukNot = tumOgrenciler[j].getNotDegeri();
                    oAnkiEnKucukNotunIndex = j;
                }

            }

            if(oAnkiEnKucukNotunIndex != i){ //Gerekli ise değerleri yer değiştiriyor.
                tumOgrenciler[oAnkiEnKucukNotunIndex] = tumOgrenciler[i];
                tumOgrenciler[i].setNotDegeri(oAnkiEnKucukNot);

            }


        }



    }


}

class Student{
    private int id;
    private int notDegeri;

    public Student(int id, int notDegeri){
        this.id = id;
        this.notDegeri = notDegeri;

    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getNotDegeri() {
        return notDegeri;
    }

    public void setNotDegeri(int notDegeri) {
        this.notDegeri = notDegeri;
    }

    public void ogrenciBilgileri(){
        System.out.println("Öğrenci ID: "+id+" Not: "+notDegeri);
    }
}

