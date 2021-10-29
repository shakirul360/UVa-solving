import java.util.Scanner;

public class Game {

	public static void main(String[] args) {
		
		int n1, n2, k1, k2;
		int winner = 1;
		Scanner input = new Scanner(System.in);
		n1 = input.nextInt();
		n2 = input.nextInt();
		k1 = input.nextInt();
		k2 = input.nextInt();
		
		while (n1 != 0 && n2 != 0) {
			n1--;
			if (n2 == 0) {
				winner = 1;
				break;
			}
			n2--;
		}
		
		if (n1 == 0) {
			winner = 2;
		} 
		//System.out.println(n1 +  " " + n2);
		if (winner == 1) {
			System.out.println("First");
		} else {
			System.out.println("Second");
		}
	}

}
