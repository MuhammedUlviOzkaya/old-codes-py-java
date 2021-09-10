package newestPackage;

public class Book {

    private String name;
    private String authorName;
    private int id;
    private int pageCount;
    private Page[] pages;

    public Book(String name, String authorName, int id, int pageCount){
        this.name = name;
        this.id = id;
        this.authorName = authorName;
        this.pageCount = pageCount;
        this.pages = new Page[pageCount];
    }

    public Book(){
        this(null,null,0,0);
    }

    public void addPage(Page p1){
        this.pages[p1.getPageNumber()] = p1;
    }

    public String getName(){
        return this.name;
    }

    public void setName(String name){
        this.name = name;
    }

    public String getAuthorName(){
        return this.authorName;
    }

    public void setAuthorName(String authorName){
        this.authorName = authorName;
    }

    public int getId(){
        return this.id;
    }

    public void setId(int id){
        this.id = id;
    }

    public void setPageCount(int pageCount){
        this.pageCount = pageCount;
        this.pages = new Page[pageCount];
    }

    public int getPageCount(){
        return this.pageCount;
    }

    public Page getOnePage(int pageNumber){
        return this.pages[pageNumber];
    }










}
