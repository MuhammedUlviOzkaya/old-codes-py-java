package newestPackage;

public class Page {

    private int pageNumber;
    private String content;

    public Page(int pageNumber, String content){
        this.pageNumber = pageNumber;
        this.content = content;
    }

    public Page(){
        this(-1,null);
    }

    public int getPageNumber(){
        return this.pageNumber;
    }

    public void setPageNumber(int pageNumber){
        this.pageNumber = pageNumber;
    }

    public String getContent(){
        return this.content;
    }

    public void setContent(String content){
        this.content = content;
    }


}
