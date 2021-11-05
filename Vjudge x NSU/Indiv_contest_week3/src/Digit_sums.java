import java.util.Scanner;

public class Digit_sums {

	public static void main(String[] args) {
		
		int n, sn;
		Scanner input = new Scanner(System.in);
		n = input.nextInt();
		sn = Sn(n);
		
		System.out.println((n % sn == 0) ? "Yes": "No");

	}
	public static int Sn(int n) {
		int sum = 0;
		while (n > 0) {
			sum += n % 10;
			n = n / 10;
		}
		
		return sum;
	}

}


