import java.util.Scanner;

public class Garden {

	public static void main(String[] args) {
		int a, b, res, c;
		
		Scanner input = new Scanner(System.in);
		
		a = input.nextInt();
		b = input.nextInt();
		
		res = (a * b) - (a + b) + 1;
		
		System.out.println(res);

	}

}
