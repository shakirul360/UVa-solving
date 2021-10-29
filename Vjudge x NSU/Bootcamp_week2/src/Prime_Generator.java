import java.util.Scanner;

public class Prime_Generator {

	public static void main(String[] args) {
		int tcase;
		long min, max;
		Scanner input = new Scanner(System.in);
		tcase = input.nextInt();
		
		for (int t = 0; t < tcase; t++) {
			min = input.nextLong();
			max = input.nextLong();
			
			for (long i = min; i <= max; i++) {
				if (prime(i) == true)
					System.out.println(i);
			}
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
