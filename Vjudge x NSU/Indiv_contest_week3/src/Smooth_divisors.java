import java.util.Scanner;

public class Smooth_divisors {

	public static void main(String[] args) {
		
		int n, divs, quotient, rem, count = 0;
		
		Scanner input = new Scanner(System.in);
		n = input.nextInt();
		
		for (int i = 1; i < n; i++) {
			quotient = n / i;
			rem = n % i;
			//System.out.println(quotient + " " + rem);
			if (quotient == rem)
				count++;
		}
		System.out.println(count);

	}

}
