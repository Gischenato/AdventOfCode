import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;

public class GenTree {
    int[] valores;
    TreeNode raiz;

    class TreeNode{
        TreeNode[] filhos;
        int[] dados;

        public TreeNode(int filhos, int metadados){
            this.filhos = new TreeNode[filhos];
            this.dados = new int[metadados];
        }

    }

    public GenTree(String arquivo){
        this.valores = leArquivo(arquivo);
        this.raiz = null;
    }


    public void leVetor(){

    }

    private int insert(int pos, int filhos, int dados){
        int qntFilhos = valores[pos++];
        int qntDados = valores[pos++];


        return 0;
    }

    public void insert(){
        int pos = 0;
        int qntFilhos = valores[pos++];
        int qntDados = valores[pos++];
        insert(0, qntFilhos, qntDados);
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
