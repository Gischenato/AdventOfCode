import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Explorer2 {
     int total;
     int[] valores;

     public Explorer2(){
          valores = leArquivo("input.txt");
          System.out.println(insert(0).tot);
     }

     class Node{
          int pos;
          int tot;

          public Node(int pos, int tot){
               this.pos = pos;
               this.tot = tot;
          }
     }

     private Node insert(int pos){
          int tot = 0;
          int qntFilhos = valores[pos++];
          int qntDados = valores[pos++];
          int[] filhos = new int[qntFilhos];

          for(int i = 0; i < qntFilhos; i++){
               Node t = insert(pos);
               pos = t.pos;
               filhos[i] = t.tot;
          }
          for(int i = 0; i < qntDados; i++) {
               if(qntFilhos == 0)
                    tot += valores[pos++];
               else{
                    int a = valores[pos++];
                    if(--a < filhos.length)
                         tot += filhos[a];
               }
          }
          return new Node(pos, tot);
     }
       
     private static int[] leArquivo(String arquivo){
          try (BufferedReader reader = new BufferedReader(new FileReader(arquivo))) {
               String line = reader.readLine();
               String[] numsInt = line.split(" ");
               int[] nums = new int[numsInt.length];
               int i = 0;
               for (String string : numsInt) {
                    nums[i] = Integer.parseInt(string);
                    i++;
               }   
               return nums;
          } catch (IOException e) {
               System.out.println("erro");
               return null;
          }
     }

}
