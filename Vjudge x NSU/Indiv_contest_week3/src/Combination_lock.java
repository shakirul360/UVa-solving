import java.util.Scanner;

public class Combination_lock {

	public static void main(String[] args) {
		
		int len, dig1, dig2, sum = 0, diff;
		String a, b;
		Scanner input = new Scanner(System.in);
		
		len = input.nextInt();

		a = input.next();
		b = input.next();
		
		for (int i = 0; i < len; i++) {
			dig1 = a.charAt(i) - '0';
			dig2 = b.charAt(i) - '0';
			//System.out.println(dig1 + " " + dig2);
			
			diff = dig2 - dig1;
			
			if (diff < 0) {
				diff = diff + 10;
			}
			
			if (diff > 5)
				diff = 10 - diff;
			
			sum += diff; 
		}
		System.out.println(sum);
		
	}

}
