import java.io.BufferedReader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;

/**
 * Main
 */
public class Main {

     public static void main(String[] args) {
          
          ArrayList<LanterFish> peixes = new ArrayList<>();
          for (int i : getVals()) {
               peixes.add(new LanterFish(i, false));
          }

          int dias = 80;


          for(int i = 0; i<=dias; i++){
               String frase = i == 0 ? "initial state:" : "After " + i + " days:";
               System.out.print(frase + " ");
               for (int j = 0; j < peixes.size(); j++) {
                    LanterFish lanterFish = peixes.get(j);
                    if(lanterFish.timer == 0){
                         // System.out.print(lanterFish.timer + ",");
                         if(!(i == dias))peixes.add(new LanterFish(8));
                         lanterFish.timer = 6;
                    }else{
                         if(!lanterFish.recemNascido){ 
                              // System.out.print(lanterFish.timer + ",");
                              lanterFish.dia();
                         }
                    }
                    if(lanterFish.recemNascido) lanterFish.recemNascido = false;
               }
               System.out.print(peixes.size());
               System.out.println();
          }

          

          System.out.println("\n" + peixes.size());

     }


     public static int[] getVals(){
          try (BufferedReader reader = Files.newBufferedReader(Paths.get("input2.txt"))){
               String line = reader.readLine();

               String[] dados = line.split(",");
               int[] valores = new int[dados.length];

               for (int i = 0; i < dados.length; i++) {
                    valores[i] = Integer.parseInt(dados[i]);
               }

               return valores;


          } catch (Exception e) {
               //TODO: handle exception
          }

          return null;
     }
}