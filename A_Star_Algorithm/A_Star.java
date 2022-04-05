import java.util.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

public class C14190226_Astar {
    static class Node implements Comparable {
        Node parent;
        double temp;
        double temp2;
        int x, y;
        Node(Node parent, int x, int y, double temp, double temp2){
            this.parent = parent;
            this.x = x;
            this.y = y;
            this.temp = temp;
            this.temp2 = temp2;
        }
        public int compareTo(Object obj){
            Node counter = (Node) obj;
            return (int)((this.temp + this.temp2) - (counter.temp + counter.temp2));
        }
    }
    private Node nodeMaze;
    private int[][] maze;
    private List<Node> path;
    private List<Node> start;
    private List<Node> end;
    private int xStart, yStart;
    private int xEnd, yEnd;
    private boolean counter;

    C14190226_Astar(int[][] maze, int xStart, int yStart, boolean counter){
        this.nodeMaze = new Node(null,xStart,yStart,0,0);
        this.path = new ArrayList<>();
        this.start = new ArrayList<>();
        this.end = new ArrayList<>();
        this.maze = maze;
        this.xStart = xStart;
        this.yStart = yStart;
        this.counter = counter;
    }

    static boolean findList(List<Node> tempArr, Node tempp){
        return tempArr.stream().anyMatch((counterr) -> (counterr.x == tempp.x && counterr.y == tempp.y));
    }

    double range(int x, int y){
        if (this.counter){
            return Math.hypot(this.nodeMaze.x + x - this.xEnd,this.nodeMaze.y + y - this.yEnd);
        }
        else{
            return Math.abs(this.nodeMaze.x + x - this.xEnd) + Math.abs(this.nodeMaze.y + y - this.yEnd);
        }
    }

    void addToList(){
        Node TempNode;
        int cekX = -1;
        while (cekX <= 1){
            int cekY = -1;
            while (cekY <= 1){
                if (!this.counter && cekX != 0 && cekY != 0){
                    continue;
                }
                TempNode = new Node(this.nodeMaze,this.nodeMaze.x + cekX,this.nodeMaze.y + cekY,this.nodeMaze.temp,range(cekX,cekY));
                if ((cekX != 0 || cekY != 0) && this.nodeMaze.x + cekX >= 0 && this.nodeMaze.x + cekX < this.maze[0].length
                        && this.nodeMaze.y + cekY >= 0 && this.nodeMaze.y + cekY < this.maze.length
                        && !findList(this.start,TempNode) && !findList(this.end,TempNode)){
                    TempNode.temp = TempNode.temp + 1;
                    TempNode.temp += this.maze[this.nodeMaze.x + cekX][this.nodeMaze.y + cekY];
                    this.start.add(TempNode);
                }
                cekY++;
            }
            cekX++;
        }
        Collections.sort(this.start);
    }

    public List<Node> findPath(int xEnd, int yEnd){
        this.end.add(this.nodeMaze);
        this.xEnd = xEnd;
        this.yEnd = yEnd;
        addToList();
        while (this.nodeMaze.x != this.xEnd || this.nodeMaze.y != this.yEnd){
            if (this.start.isEmpty()){ //Tidak ada yang diperiksa
                return null;
            }
            this.nodeMaze = this.start.get(0); //Mengambil node pertama
            this.start.remove(0);
            this.end.add(this.nodeMaze);
            addToList();
        }
        this.path.add(0,this.nodeMaze);
        while (this.nodeMaze.x != this.xStart || this.nodeMaze.y != this.yStart){
            this.nodeMaze = this.nodeMaze.parent;
            this.path.add(0,this.nodeMaze);
        }
        return this.path;
    }

    public static void main(String[] args){
        int[][] maze = {
                { 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 1, 0, 1, 1, 0, 1, 0 },
                { 0, 1, 1, 0, 0, 1, 1, 0 },
                { 0, 1, 1, 0, 1, 1, 1, 0 },
                { 0, 1, 0, 1, 0, 0, 1, 0 },
                { 0, 1, 0, 1, 0, 1, 1, 0 },
                { 0, 1, 0, 1, 1, 0, 1, 0 },
                { 0, 0, 1, 1, 1, 1, 0, 0 }
        };
        C14190226_Astar aStarr = new C14190226_Astar(maze,0,0,true);
        List<Node> path = aStarr.findPath(7,7);
        if (path != null){
            System.out.println("\n-- A* Algorithm --");
            System.out.println("Note !! \n-> Angka 0 = Jalan \n-> Angka 1 = Tembok");
            System.out.println("Start : {0,0}\nGoal  : {7,7}");
            System.out.print("-> Path : ");
            path.forEach((counter) -> { System.out.print("{" + counter.x + "," + counter.y + "} ");
            });
        }
        else {
            System.out.print("Path not found !!");
        }
    }
}