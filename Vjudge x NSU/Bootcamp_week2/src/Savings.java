import java.util.Scanner;

public class Savings {

	public static void main(String[] args) {
		long n, count;
		int i;
		
		Scanner input = new Scanner(System.in);
		n = input.nextLong();
		i = 0;
		count = 0;
		while (count < n) {
			i++;
			count += i;
			//System.out.println(count);
		}
		System.out.println(i);

	}

}
