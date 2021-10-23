import java.util.Scanner;

public class Digits_Sequence {

	public static void main(String[] args) {
		
		
		int n;
		StringBuilder string = new StringBuilder();
		
		Scanner input = new Scanner(System.in);
		
		n = input.nextInt();
		
		for (int i = 1; i <= n; i++) {
			string.append(i);
		}
		
		System.out.println(string.charAt(n - 1));
		

	}

}
