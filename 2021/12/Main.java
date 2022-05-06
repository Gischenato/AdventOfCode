import java.io.File;
import java.util.Scanner;

public class Main {
     public static void main(String[] args) {
          Grafo g = new Grafo();
     
          try (Scanner scan = new Scanner(new File("input.txt"))){
               String line;
               while(scan.hasNext()){
                    line = scan.nextLine();
                    String[] data = line.split("-");
                    g.insert(data[0], data[1]);
                    g.insert(data[1], data[0]);
               }

          } catch (Exception e) {
               System.out.println("Deu erro");
          }
          System.out.println(g);
          g.caminhos("start", "end");
          System.out.println(g.total);
     }
}