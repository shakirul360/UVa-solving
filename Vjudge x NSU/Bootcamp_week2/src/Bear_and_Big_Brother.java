import java.util.Scanner;

public class Bear_and_Big_Brother {

	public static void main(String[] args) {
		int n, a,b, year = 0;
		
		Scanner input = new Scanner (System.in);
		
		a = input.nextInt();
		b = input.nextInt();
		
		while (a <= b) {
			a *= 3;
			b *= 2;
			year++;
		}
		System.out.println(year);
	}

}
