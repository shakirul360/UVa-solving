import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class kth_divisor {

public static void main(String[] args) {
		
		long n, j, index;
		Scanner input = new Scanner(System.in);
		n = input.nextLong();
		index = input.nextInt();
		
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
		
		//System.out.println(divisors);
		if (index > divisors.size() -1)
			System.out.println(-1);
		//else
			//System.out.println(divisors.get(index));

	}

}
