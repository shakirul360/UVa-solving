import java.util.Scanner;

public class Primality_Test {

	public static void main(String[] args) {
		int tcase, n;
		
		Scanner input = new Scanner(System.in);
		tcase = input.nextInt();
		
		for (int t = 0; t < tcase; t++) {
			n = input.nextInt();
			
			if (prime(n) == true)
				System.out.println("yes");
			else
				System.out.println("no");
	}

	}
	
	public static boolean prime(long n) {
		
		if (n <= 1)
			return false;
		for (int i = 2; i * i <= n; i++) {
			if (n % i == 0)
				return false;
		}
		
		return true;
		
	}
}
