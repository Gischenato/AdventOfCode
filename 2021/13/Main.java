import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
     public static int maxX;
     public static int maxY;

     public static void main(String[] args) throws IOException{
          String arquivo = "input.txt";
          BufferedReader reader = Files.newBufferedReader(Paths.get(arquivo));
          
          List<String[]> folds = new ArrayList<>();

          maxX = 0;
          maxY = 0;

          String line;
          
          while ((line = reader.readLine()) != null) {
               if(line.isBlank()) continue;
               if(line.startsWith("fold")){
                    folds.add(line.split(" "));
                    continue;
               }
               
               String[] data = line.trim().split(",");
               int x = Integer.parseInt(data[0]);
               int y = Integer.parseInt(data[1]);

               maxX = Math.max(maxX, x);
               maxY = Math.max(maxY, y);
               
          }

          maxX++;
          maxY++;

          reader.close();
          reader = Files.newBufferedReader(Paths.get(arquivo));
          boolean[] paper = new boolean[maxY * maxX];

          while ((line = reader.readLine()) != null) {
               if(line.isBlank()) continue;
               if(line.startsWith("fold")){
                    
                    continue;
               }
               
               String[] data = line.trim().split(",");
               int x = Integer.parseInt(data[0]);
               int y = Integer.parseInt(data[1]);
               
               paper[maxX * y + x] = true;
          }

          for (String[] instruction : folds) {
               int foldPos = Integer.parseInt(instruction[2].split("=")[1]);
               String foldWhere = instruction[2].split("=")[0];
               if(foldWhere.equals("x")) paper = foldX(paper, foldPos);
               if(foldWhere.equals("y")) paper = foldY(paper, foldPos);
               print(paper);
          }
          print(paper);
          System.out.println(conta(paper));
     }


     public static void print(boolean[] paper){
          System.out.println("======================");
          int i = 0;          
          for(boolean b : paper){
               if(i % maxX == 0)System.out.println();
               System.out.print(b ? "#" : ".");
               i++;
          }
          System.out.println("\n======================");          
     }


     public static boolean[] foldX(boolean[] paper, int pos){
          for(int y = 0; y<maxY; y++){
               int x0 = pos-1;
               for(int x = pos + 1; x<maxX; x++){
                   paper[maxX*y + x0] = paper[maxX*y + x] ? true : paper[maxX*y + x0];  
                   x0--;                  
               }
          }          
          boolean[] newPaper = new boolean[pos * maxY];

          for(int y = 0; y<maxY; y++){
               for(int x = 0; x<pos; x++){
                    newPaper[pos*y + x] = paper[maxX*y + x];
               }
          }
          maxX = pos;

          return newPaper;
     }

     public static boolean[] foldY(boolean[] paper, int pos){
          boolean[] newPaper = Arrays.copyOf(paper, maxX * pos);
          maxY = pos;

          for(int y = 1; y < pos + 1; y++){
               for(int x = 0; x < maxX; x++){
                    newPaper[maxX * (pos -  y) + x] = paper[maxX * (pos + y) + x] ? true : newPaper[maxX * (pos - y) + x];
               }
          }

          return newPaper;
     }

     public static int conta(boolean[] paper){
          int total = 0;
          for (boolean b : paper) {
               if(b) total++;
          }
          return total;
     }

}