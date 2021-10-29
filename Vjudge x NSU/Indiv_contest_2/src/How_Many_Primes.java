import java.util.Scanner;

public class How_Many_Primes {

	public static void main(String[] args) {
		int tcase;
		int a, b, count;
		
		Scanner input = new Scanner(System.in);
		
		tcase = input.nextInt();
		
		for (int t = 0; t < tcase; t++) {
			a = input.nextInt();
			b = input.nextInt();
			
			count = 0;
			for (int i = a; i <= b; i++) {
				if (prime(i) == true) {
					count++;
				}
			}
			
			System.out.printf("Case %d: %d\n", t + 1, count);
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
