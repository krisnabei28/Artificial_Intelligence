import java.util.Stack;

class Iterative_Deepening_Search {
    private Stack<Integer> stck;
    private int node;
    private int maxDepth;
    private int depth;
    private boolean goal = false;

    Iterative_Deepening_Search(){
        stck = new Stack<Integer>();
    }

    public void IDS(int adjMatrix[][], int goalss){
        node = adjMatrix[1].length - 1;
        while (!goal){
            DLS(adjMatrix,1,goalss);
            maxDepth++;
        }
        System.out.print("\nGoal ditemukan di depth(level) " + depth);
    }

    public void DLS(int adjMatrix[][], int counter, int goalss){
        int ctr, tempGoal;
        int[] temp = new  int[node + 1];
        tempGoal = 1;
        stck.push(counter);
        depth = 0;
        System.out.print("\n-> Depth(level) " + maxDepth + " : " + counter + "\t");
        while (!stck.isEmpty()){
            ctr = stck.peek();
            while (tempGoal <= node){
                if(depth < maxDepth){
                    if(adjMatrix[ctr][tempGoal] == 1){
                        stck.push(tempGoal);
                        temp[tempGoal] = 1;
                        System.out.print(tempGoal + "\t");
                        depth++;
                        if(goalss == tempGoal){
                            goal = true;
                            return;
                        }
                        ctr = tempGoal;
                        tempGoal = 1;
                        continue;
                    }
                }
                else {
                    break;
                }
                tempGoal++;
            }
            tempGoal = stck.pop() + 1;
            depth--;
        }
    }

}

public class C14190226_IDS {
    public static void main(String[] args) {
        int n = 15, co = 0, ct = 1, t = 0, goal;
        goal = 12; //Untuk ganti goal (goal hanya bisa dinput dari 1 - 15 karena sesuai ukuran adjacency_matrix)
        System.out.print("\nGoal yang di cari = " + goal);
        int adjacency_matrix[][] = new int[n + 1][n + 1];
        //Isi adjacency_matrix 15 x 15
        //0 1 1 0 0 0 0 0 0 0 0 0 0 0 0
        //0 0 0 1 1 0 0 0 0 0 0 0 0 0 0
        //0 0 0 0 0 1 1 0 0 0 0 0 0 0 0
        //0 0 0 0 0 0 0 1 1 0 0 0 0 0 0
        //0 0 0 0 0 0 0 0 0 1 1 0 0 0 0
        //0 0 0 0 0 0 0 0 0 0 0 1 1 0 0
        //0 0 0 0 0 0 0 0 0 0 0 0 0 1 1
        //0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        //0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        //0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        //0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        //0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        //0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        //0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        //0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

        for (int i = 1; i <= n; i++){ //Mengisi adjacency_matrix 15 x 15
            co = 0;
            for (int j = 1; j <= n; j++)
                if(j > i+t && co != 2 && ct <= 7){
                    adjacency_matrix[i][j] = 1;
                    co++;
                    if(co == 2){
                        ct++;
                    }
                }else{
                    adjacency_matrix[i][j] = 0;
                }
            t++;
        }

        //Gambar graph
        //           1
        //           /\
        //      2          3
        //     /\          /\
        //    4  5        6   7
        //   /\   /\     /\   /\
        //  8  9 10 11 12 13 14 15
        Iterative_Deepening_Search iterativeDeepening = new Iterative_Deepening_Search();
        iterativeDeepening.IDS(adjacency_matrix, goal);
    }

}
