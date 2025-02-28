public class Program {

    public static void main(String[] args) {
        try{
            int a = 10/0;
        } catch(Exception e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
            // System.out.println(e.printStackTrace());
        }
    }
}