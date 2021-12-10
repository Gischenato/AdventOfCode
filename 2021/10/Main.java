import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;

public class Main {
     public static void main(String[] args) throws IOException {
          BufferedReader reader = Files.newBufferedReader(Paths.get("input.txt"));

          ArrayList<Long> values = new ArrayList<>();
          String line;
          int total = 0;

          while ((line = reader.readLine()) != null) {
               Stack<Character> pilha = new Stack<>();
               boolean descartar = false;
               char[] dados = line.toCharArray();
               for (char c : dados) {
                    boolean correto = false;
                    if (pilha.size() > 0) {
                         char anterior = pilha.get(pilha.size() - 1);
                         switch (c) {
                              case ')':
                                   if (anterior == '(')
                                        correto = true;
                                   else
                                        total += 3;
                                   break;
                              case ']':
                                   if (anterior == '[')
                                        correto = true;
                                   else
                                        total += 57;
                                   break;

                              case '}':
                                   if (anterior == '{')
                                        correto = true;
                                   else
                                        total += 1197;
                                   break;

                              case '>':
                                   if (anterior == '<')
                                        correto = true;
                                   else
                                        total += 25137;
                                   break;

                              default:
                                   break;
                         }
                    }

                    if (correto)
                         pilha.pop();
                    else if (c == '(' || c == '{' || c == '[' || c == '<')
                         pilha.push(c);
                    else {
                         descartar = true;
                         break;
                    }
               }

               if (descartar)
                    continue;

               String completar = "";
               while (!pilha.isEmpty()) {
                    char atual = pilha.pop();
                    switch (atual) {
                         case '(':
                              completar += ")";
                              break;
                         case '[':
                              completar += "]";
                              break;
                         case '{':
                              completar += "}";
                              break;
                         case '<':
                              completar += ">";
                              break;
                         default:
                              break;
                    }
               }

               char[] faltando = completar.toCharArray();

               long sum = 0;

               for (char d : faltando) {
                    sum *= 5;
                    switch (d) {
                         case ')':
                              sum += 1;
                              break;
                         case ']':
                              sum += 2;
                              break;
                         case '}':
                              sum += 3;
                              break;
                         case '>':
                              sum += 4;
                              break;
                         default:
                              break;
                    }
               }
               values.add(sum);
          }
          Collections.sort(values);

          System.out.println("Part 1 - " + total);
          System.out.println("Part 2 - " + values.get(values.size() / 2));

          reader.close();
     }
}
