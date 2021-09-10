package newestPackage;

public class Scenario {

    public static void main(String [] args){

        TaskStack ts = new TaskStack(10);
        ts.push(new Tasks("Lesson l",'l'));
        char c [] = {'O','O','P'};
        ts.push(new Tasks(c));
        System.out.println(ts.pop());

        String val = ts.pop();
        System.out.println(val);
        ts.push(new Tasks(val,0,val.length()-1));
        System.out.println(ts.pop());



    }
}
