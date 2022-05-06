import java.util.ArrayList;
import java.util.HashSet;

public class Grafo {
     HashSet<String> nodos;
     ArrayList<String[]> arestas;
     int total = 0;

     class Node{
          String name;
          Boolean marcado;

          Node(String name){
               this.name = name;
               this.marcado = false;
          }
     }

     public Grafo(){
          nodos = new HashSet<>();
          arestas = new ArrayList<>();
     }

     public void insert(String n1, String n2){
          if(!nodos.contains(n1)) nodos.add(n1);
          if(!nodos.contains(n2)) nodos.add(n2);

          arestas.add(new String[] {n1, n2});
          // arestas.add(new String[] {n2, n1});
     }

     public int caminhos(String ni, String nd){
          ArrayList<String> c = new ArrayList<>();
          c.add(ni);
          return caminhos(nd, ni, new ArrayList<String>(), "", new ArrayList<String[]>(arestas));
     }

     private int caminhos(String nd, String nodo, ArrayList<String> usados, String tab, ArrayList<String[]> arest){
          usados.add(nodo);
          int tot = 0;
          Boolean remover = (int) nodo.charAt(0) >= 97;
          for(int i = 0; i<arest.size(); i++){
               String aresta[] = arest.get(i);
               if(aresta[0].equals(nodo)){
                    if(aresta[1].equals(nd)){
                         usados.add(nd);
                         System.out.println("---------------");                     
                         System.out.println(usados);
                         this.total++; 
                         continue;                    
                    }
                    ArrayList<String[]> novo = new ArrayList<>(arest);
                    boolean print = false;
                    if(print) System.out.println();
                    if(print) System.out.println(novo.size());
                    for(int k = 0; k<novo.size(); k++){
                         String a[] = novo.get(k);
                         if(print) System.out.printf("%s(%s}%s) (%s -> %s) ",tab, nodo, aresta[1], a[0], a[1]);
                         if(remover){
                              if(a[0].equals(nodo) || a[1].equals(nodo) && !((int)a[1].toCharArray()[0] >= 97)){
                                   novo.remove(a);
                                   if(print) System.out.printf("removendo");
                                   k--;
                              }
                         }
                         else{
                              if(a[0].equals(nodo) && a[1] == aresta[1]){
                                   novo.remove(a);
                                   if(print) System.out.printf("removendo");
                                   k--;
                              }
                         }
                         if(print) System.out.println();
                    }
                    tot += caminhos(nd, aresta[1], new ArrayList<>(usados), tab + "\t", novo);
               }
          }
          return tot;
     }

     @Override
     public String toString() {
          String i = "";
          i += "Arestas:\n";
          for (String[] strings : arestas) {
               i += "( ";
               for (String string : strings) {
                    i += string + " ";
               }
               i += ")\n";
          }
          return i;
     }
}