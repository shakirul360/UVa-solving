import java.util.Scanner;

public class Divisor_Summation {

	public static void main(String[] args) {
		int tcase, t, n, i, j, total;
		
		Scanner input = new Scanner(System.in);
		
		tcase = input.nextInt();
		
		for (t = 0; t < tcase; t++) {
			n = input.nextInt();
			
			total = 0;
			
			for (i = 1; i * i <= n; i++) {
				if (n == 1)
					break;
				if (n % i == 0) {
					total += i;
					
					j = n / i;
					
					if (i != j && j != n)
						total += j;
				}
					
		
			}
			
			System.out.println(total);
		}

	}

}
