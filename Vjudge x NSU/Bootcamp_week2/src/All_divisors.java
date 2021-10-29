import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class All_divisors {

	public static void main(String[] args) {
		
		long n, j;
		Scanner input = new Scanner(System.in);
		n = input.nextLong();
		ArrayList<Long> divisors = new ArrayList<Long>();
		
		for (long i = 1; i * i <= n; i++) {
			if (n % i == 0) {
				divisors.add(i);
				
				j = n / i;
				if (j != i)
					divisors.add(j);
			}
		}
		Collections.sort(divisors);
		
		for (int x = 0; x < divisors.size(); x++) {
			System.out.print(divisors.get(x) + " ");
		}

	}

}
