import java. util.Scanner;
import java.lang.Math;

class CircleinSquare {
    public static void main(String[] args) {

        int tcase;
        Scanner input = new Scanner(System.in);
        tcase = input.nextInt();

        Scanner d_input = new Scanner(System.in);


        for (int i = 0; i < tcase; i++){
            double r = d_input.nextDouble();

            double sq = Math.pow(r * 2, 2);
            double circ = r * r * 2 * Math.acos(0.0);

            double res = sq - circ;

            System.out.printf("Case %d: %.2f\n", i + 1, res);

        }


    }
}