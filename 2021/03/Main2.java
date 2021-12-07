import java.io.BufferedReader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashSet;

/**
 * Main
 */
public class Main2 {

     public static void main(String[] args) {
          Path path = Paths.get("input.txt");
          try (BufferedReader reader = Files.newBufferedReader(path)){
           
               ArrayList<int[]> bits = new ArrayList<>();


               String line;
               for(int i = 0; i<1000; i++){
                    bits.add(new int[12]);
               }
               int linha = 0;
               while ((line = reader.readLine()) != null) {
                    
                    char[] dados = line.toCharArray();

                    for(int i = 0; i< dados.length; i++){
                         bits.get(linha)[i] = Character.getNumericValue(dados[i]);
                         // System.out.print(bits.get(linha)[i]);
                    }
                    // System.out.println();
                    linha++;
               }

               int[] um = new int[12];
               int[] zero = new int[12];



               for (int[] is : bits) {
                   for(int i = 0; i<is.length; i++){
                         if(is[i] == 0) zero[i]++;
                         else um[i]++;

                   } 
               }

               int[] valores = new int[12];

               for(int i = 0; i<12; i++){
                    valores[i] = um[i] >= zero[i] ? 1 : 0;
                    System.out.println(um[i] + " " + zero[i]);
               }

               
               for(int i = 0; i<12; i++){
                    HashSet<int[]> deletados = new HashSet<>();
                    for (int[] vet : bits) {
                         if(vet[i] != valores[i]) deletados.add(vet);
                    }

                    for (int[] js : deletados) {
                         bits.remove(js);
                         if(bits.size() == 1) break;
                    }
                    if(bits.size() == 1) break;
               }

               int[] oxygen = bits.get(0);

               for (int i : oxygen) {
                    System.out.print(i);
               }





               // System.out.println();
               // for (int i : valores) {
               //      System.out.print(i);
               // }









          } catch (Exception e) {

               e.printStackTrace();
          }


     }
}


// ! 010111010011

// ? 101000101001

// 010100011001
// 101000100010