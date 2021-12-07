import java.io.BufferedReader;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main2 {

     public static void main(String[] args) {

          int dias = 1500000000;
          
          long[] peixes = new long[9];

          int[] valores = getVals();

          for (int i : valores) {
               peixes[i]++;
          }

          for(int i = 0; i < dias; i++){
               long aux0 = peixes[0];
               long aux1 = peixes[1];
               long aux2 = peixes[2];
               long aux3 = peixes[3];
               long aux4 = peixes[4];
               long aux5 = peixes[5];
               long aux6 = peixes[6];
               long aux7 = peixes[7];
               long aux8 = peixes[8];

               peixes[8] = aux0;
               peixes[7] = aux8;
               peixes[6] = aux7 + aux0;
               peixes[5] = aux6;
               peixes[4] = aux5;
               peixes[3] = aux4;
               peixes[2] = aux3;
               peixes[1] = aux2;
               peixes[0] = aux1;
          }

          long soma = 0;
          for(int i = 0; i<=8; i++){
               soma += peixes[i];
               System.out.println(peixes[i]);
          }
          
          System.out.println("\n" + soma);

     }


     public static int[] getVals(){
          try (BufferedReader reader = Files.newBufferedReader(Paths.get("input.txt"))){
               String line = reader.readLine();

               String[] dados = line.split(",");
               int[] valores = new int[dados.length];

               for (int i = 0; i < dados.length; i++) {
                    valores[i] = Integer.parseInt(dados[i]);
               }

               return valores;


          } catch (Exception e) {
               e.printStackTrace();
          }

          return null;
     }
}