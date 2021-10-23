import java.util.Scanner;

public class CamelCase {

	public static void main(String[] args) {
		
		int count = 1;
		Scanner input = new Scanner(System.in);
		StringBuilder string = new StringBuilder(input.nextLine());
		
		for (int i = 0; i < string.length(); i++) {
			if ((int) string.charAt(i) < 97) {
				count++;
			}
		}
		
		
		System.out.println(count);
	}

}
