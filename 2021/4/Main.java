import java.io.BufferedReader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

     public static void main(String[] args) {

          try (Scanner reader = new Scanner(Paths.get("input.txt"))) {

               String[] numeros = reader.nextLine().split(",");

               ArrayList<int[][]> tabelas = new ArrayList<int[][]>();

               String line;
               int linha = 0;
               int[][] tabela = new int[5][5];
               while (reader.hasNext()) {
                    line = reader.nextLine();
                    if(line.equals("")) {
                         linha = 0;
                         tabelas.add(tabela);
                         System.out.println("Teste");
                         tabela = new int[5][5];
                    }

                    String[] valores = line.split(" ");

                    for(int i = 0; i<valores.length; i++){
                         tabela[linha][i] = Integer.parseInt(valores[i]);
                    }

                    linha++;
               }

               for (int[][] matriz : tabelas) {
                    System.out.println(matriz.length);
               }

          } catch (Exception e) {
               // TODO: handle exception
          }

     }
}