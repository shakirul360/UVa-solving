import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Almost_All_Divisors {

	public static void main(String[] args) {
		
		int tcase, n, i;
		long j, min , max, res, d, d2;
		boolean flag;
		Scanner input = new Scanner(System.in);
		
		tcase = input.nextInt();
		
		for (int t = 0; t < tcase; t++) {
			ArrayList<Long> numbers = new ArrayList<Long>();
			ArrayList<Long> divisors = new ArrayList<Long>();
			
			n = input.nextInt();
			
			for (i = 0; i < n; i++) {
				j = input.nextLong();
				numbers.add(j);
			}
	
			Collections.sort(numbers);
			//System.out.println(numbers);
			min = numbers.get(0);
			max = numbers.get(n - 1);
			//System.out.println(min + " " + max);
			
			res = min * max;
			
			for (d = 2; d * d <= res; d++) {
				if (res % d == 0) {
					divisors.add(d);
				}
                d2 = res / d;
                if (res % d2 == 0 && d2 != d)
                	divisors.add(d2);
			}
			Collections.sort(divisors);
			//System.out.println(divisors);
			//System.out.println(numbers);
			
			flag = true;
			
			for (i = 0; i < n; i++) {
				if (divisors.get(i) != numbers.get(i)) {
					flag = false;
					break;
				}
			}
			
			if (flag == true)
				System.out.println(res);
			else 
				System.out.println(-1);
			
			
		}

	}

}
