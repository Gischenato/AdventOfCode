import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Explorer {
     int total;
     int[] valores;

     public Explorer(){
          this.total = 0;
          valores = leArquivo("input.txt");
          insert(0);
          tot();
     }

     private int insert(int pos){
          if(pos > valores.length) return pos;
          int qntFilhos = valores[pos++];
          int qntDados = valores[pos++];
          if(qntFilhos == 0){
               for(int i = 0; i < qntDados; i++) this.total += valores[pos++];
          }
          else{
               for(int i = 0; i < qntFilhos; i++) pos = insert(pos);
               for(int i = 0; i < qntDados; i++) this.total += valores[pos++];
          }
          return pos;
     }

     public void tot(){
          System.out.println(this.total);
     }

       
     public static int[] leArquivo(String arquivo){
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
