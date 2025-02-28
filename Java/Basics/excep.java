import java.lang.Exception;
public class Program {

    public static void main(String[] args) {
        try{
            throw new IllegalArgumentException("Invalid exception");
            // int a = 10/0;
        } catch(ArithmeticException e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
        catch(Exception e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
            System.out.println(19/0);
            show();
            // System.out.println(e.printStackTrace());
        } 
    }

    public static void show() {
        System.out.println(19/0);
    }
}