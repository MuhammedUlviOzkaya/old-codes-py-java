
public class NewClass {
    public static void main(String[] args) {
        String studentId = "180315041";
        String name = "Muhammed Özkaya";
        String edNo = "1";
        String res = "";
        
        String[] names = name.split(" ");
        
        String last3 = Character.toString(studentId.charAt(6)) + Character.toString(studentId.charAt(7)) + Character.toString(studentId.charAt(8));
        String first = Character.toString(name.charAt(0));
        String last = Character.toString(names[1].charAt(0));
        int lastIndex = studentId.charAt(8);
        
        System.out.println(lastIndex);
        
        res = last3 + first + last + edNo + lastIndex;
        
        System.out.println(res);
        
        
        
        
        
        
        
        
        
               
    }
}
