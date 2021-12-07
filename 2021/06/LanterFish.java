public class LanterFish {
     public int timer;
     public boolean recemNascido;


     public LanterFish(int timer){
          this.timer = timer;
          this.recemNascido = true;
     }

     public LanterFish(int timer, boolean falso){
          this.timer = timer;
          this.recemNascido = false;
     }

     public void dia(){ timer--; }

     public void naoMais(){ recemNascido = false; }

     public boolean spawn(){
          if(timer == 0){
               timer = 6;
               return true;
          }
          return false;
     }
}
