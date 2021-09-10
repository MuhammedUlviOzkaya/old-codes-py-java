package newestPackage;

public class TaskStack {
    private Tasks [] stack;
    private int pointer;

    public TaskStack(int length){
        stack = new Tasks[length];

     }
     public boolean isEmpty(){
        return pointer <= 0;
     }

     public boolean isFull(){
        return pointer == this.stack.length - 1;
     }

     public void push(Tasks t){
        if(isFull()){
            System.out.println("Stack is full! You can't push a new task.");
        }else{
            this.stack[pointer] = t;
            pointer ++;
        }
     }

     public String pop(){
        if(isEmpty()){
            System.out.println("Stack is empty! You can't pop task from the stack");
            return null;
        }
        else{
            pointer--;
            String val = this.stack[pointer].getResult();
            this.stack[pointer] = null;

            compress();
            return val;
        }
     }

     public void compress(){
        Tasks [] tArray = new Tasks[this.stack.length];
        int nPointer = 0;
        for(int i = 0; i<tArray.length; i++){
            if(this.stack[i] != null){
                tArray[i] = this.stack[i];
                nPointer++;
            }
            else{
                break;
            }


        }
        this.stack = tArray;
        this.pointer = nPointer;
     }




}
