import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.LinkedList;

public class Teste {
     public static void main(String[] args) {
          LinkedList<Integer> teste = new LinkedList<>();
          for(int i = 0; i < 1000000000 	; i++){
               for(int k = 0; k < 1000000000; k++){
                    teste.add(1);
               }
               System.out.println(teste.size());
          }

     }
}
