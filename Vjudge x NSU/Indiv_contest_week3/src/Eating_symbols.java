import java.util.Scanner;

public class Eating_symbols {

	public static void main(String[] args) {
		
		int n = 0;
		
		String str;
		
		Scanner input = new Scanner(System.in);
		str = input.next();
		
		for (int i = 0; i < 4; i++) {
			if (str.charAt(i) == '+')
				n+= 1;
			else
				n-= 1;
			
		}
		
		System.out.println(n);

	}

}
