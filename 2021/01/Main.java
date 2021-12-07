import java.io.BufferedReader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;

import javax.sound.midi.Patch;

/**
 * Main
 */
public class Main {

     public static void main(String[] args) {
          Path path = Paths.get("input.txt");

          ArrayList<Integer> list = new ArrayList<>();
          try (BufferedReader reader = Files.newBufferedReader(path)){
               String line;
               while ((line = reader.readLine()) != null) {
                    list.add(Integer.parseInt(line));
               }   
          } catch (Exception e) {
     
          }

          int contador = 0;
          for(int i = 0; i < list.size() - 3; i++){
               int soma1 = list.get(i) + list.get(i + 1) + list.get(i + 2);
               int soma2 = list.get(i + 1) + list.get(i + 2) + list.get(i + 3);

               if(soma2 > soma1) contador++;
          }

          System.out.println(contador);
     }
}