import java.util.Scanner;

public class Something_on_it {

	public static void main(String[] args) {
		
		String s;
		int res = 700;
		
		Scanner input = new Scanner(System.in);
		
		s = input.next();
		
		for (int i = 0; i < 3; i++) {
			if (s.charAt(i) == 'o') {
				res += 100;
			}
		}
		
		System.out.println(res);
		

	}

}
