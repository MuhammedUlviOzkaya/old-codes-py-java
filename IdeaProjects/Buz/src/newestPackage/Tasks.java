package newestPackage;

public class Tasks {

    private String result;

    public Tasks(String w, char c){
        replaceWord(w,c);
    }

    public Tasks(String w, int index, int index2){
        subWord(w,index,index2);
    }

    public Tasks(char [] c){
        collectWord(c);
    }

    public void replaceWord(String w, char c){
        char c1 = w.charAt(0);
        w = w.replace(c1,c);
        this.result = w;
    }

    public void subWord(String w, int index1, int index2){
        w = w.substring(index1,index2);
        this.result = w;
    }

    public void collectWord(char [] c){
        this.result = "";

        for(int i = 0; i<c.length; i++){
            this.result = this.result + c[i];
        }
    }

    public String getResult(){
        return this.result;
    }

    public void setResult(String res){
        this.result = res;
    }









}
