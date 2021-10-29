import java.util.Scanner;

public class Primes {

	public static void main(String[] args) {
		long n, i, a = 0, b = 0;
		
		boolean found = false;
		Scanner input = new Scanner(System.in);
		n = input.nextLong();
		
		for (i = 0; i <= n / 2; i++) {
			a = i;
			b = n - i;
			if (prime(a)) {
				if (prime(b)) {
				found = true;
				break;
				}
			}
		}
		if (found){
			System.out.println(a + " " + b);
		} else {
			System.out.println(-1);
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
