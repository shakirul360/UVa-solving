import java.util.Scanner;

public class Sherlock_and_Divisors {

	public static void main(String[] args) {
		
		int tcase, n, t, i, j, div_count;
		Scanner input = new Scanner(System.in);
		
		tcase = input.nextInt();
		
		for (t = 0; t < tcase; t++) {
			div_count = 0;
			
			n = input.nextInt();
			
			  for(i = 1; i * i <= n; i++){
			        if (n % i == 0) {
			            if (i % 2 == 0) {
			            	div_count++;
			            }
			            j = n / i;
			            if(i != j && j % 2 == 0) {
			            	div_count++;
			            }
			            
			            
			        }
			    }

			
			System.out.println(div_count);
		}

	}

}
