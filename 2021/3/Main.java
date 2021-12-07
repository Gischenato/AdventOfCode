import java.io.BufferedReader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;

/**
 * Main
 */
public class Main {

     public static void main(String[] args) {
          Path path = Paths.get("input.txt");
          try (BufferedReader reader = Files.newBufferedReader(path)){
           
               ArrayList<ArrayList<Character>> bits = new ArrayList<>();


               String line;

               bits.add(new ArrayList<Character>());
               bits.add(new ArrayList<Character>());
               bits.add(new ArrayList<Character>());
               bits.add(new ArrayList<Character>());
               bits.add(new ArrayList<Character>());
               bits.add(new ArrayList<Character>());
               bits.add(new ArrayList<Character>());
               bits.add(new ArrayList<Character>());
               bits.add(new ArrayList<Character>());
               bits.add(new ArrayList<Character>());
               bits.add(new ArrayList<Character>());
               bits.add(new ArrayList<Character>());

               while ((line = reader.readLine()) != null) {
                    
                    char[] dados = line.toCharArray();


                    for(int i = 0; i<dados.length; i++){

                         bits.get(i).add(dados[i]);

                    }
               }

               int[] palavra = new int[12];
               
               int pos = 0;

               for (ArrayList<Character> arrayList : bits) {
                    int ums = 0;
                    int zeros = 0;

                    ums = (int) arrayList.stream().filter(p -> p == '1').count();
                    zeros = (int) arrayList.stream().filter(p -> p == '0').count();

                    palavra[pos] = ums > zeros ? 1 : 0;

                    pos++;
               }



               for (int i : palavra) {
                    System.out.print(i);
               }
               System.out.println();
               for (int i : palavra) {
                    i = i == 0 ? 1 : 0;
                    System.out.print(i);
               }

          } catch (Exception e) {

               e.printStackTrace();
          }


     }
}