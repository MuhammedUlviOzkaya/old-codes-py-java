package newestPackage;

public class Library {

    private int bookCount;
    private Book[] books;

    public Library(int bookCount){
        this.bookCount = bookCount;
        this.books = new Book[bookCount];
    }

    public Library(){
        this(0);
    }

    public void addBooks(Book b1){
        this.books[b1.getId()] = b1;
    }

    public Book getOneBook(int id){
        return this.books[id];
    }

    public Book [] getBooksByAuthorName(String authorName){
        Book bArray[] = new Book [this.bookCount];
        int counter = 0;
        for(int i = 0; i<this.bookCount; i++){
            if(books[i].getAuthorName().equals(authorName)){
                bArray[counter] = books[i];
                counter++;
            }
        }

        return bArray;
    }

    public Book getOneBookByName(String name){
        for(int i = 0; i<this.bookCount; i++){
            if(books[i].getName().equals(name)){
                return books[i];
            }
        }
        return null;
    }

    public int getBookCount(){
        return this.bookCount;
    }

    public void setBookCount(int bookCount){
        this.bookCount = bookCount;
        this.books = new Book[bookCount];
    }

    public static void main(String[] args){
        Library lib = new Library(30);
        for(int i = 0; i<lib.getBookCount(); i++){
            int randomPageCount = 50 + (int)(Math.random() * 100);
            Book b = new Book(i+"","Ali Ayşe", i, randomPageCount);
            for(int j = 0; j<randomPageCount; j++){
                Page p1 = new Page(j, "j: "+j);
                b.addPage(p1);
            }
            lib.addBooks(b);
        }


    }





}
