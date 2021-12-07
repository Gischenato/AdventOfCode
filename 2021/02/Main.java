import java.io.BufferedReader;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Main
 */
public class Main {

     public static void main(String[] args) {
          
          Path path = Paths.get("input.txt");
          int depht = 0;
          int horizontal = 0;
          int aim = 0;
          
          try(BufferedReader reader = Files.newBufferedReader(path, Charset.forName("utf8"))){

               String line;
               while ((line = reader.readLine()) != null) {
                    String[] dados = line.split(" ");
                    switch (dados[0]) {
                         case "forward":
                              horizontal += Integer.parseInt(dados[1]);
                              depht += aim * Integer.parseInt(dados[1]);

                              break;
                    
                         case "down":
                              aim += Integer.parseInt(dados[1]);


                              break;

                         case "up":
                              aim -= Integer.parseInt(dados[1]);


                         default:
                              break;
                    }
               }
          } catch (Exception e) {
               //TODO: handle exception
          }


          System.out.println(depht * horizontal);
     }
}