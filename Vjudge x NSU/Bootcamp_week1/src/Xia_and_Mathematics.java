import java.util.Scanner;

public class Xia_and_Mathematics {

	public static void main(String[] args) {
		char num;
		Scanner input = new Scanner(System.in);
		StringBuilder string = new StringBuilder(input.nextLine());
		
		num = string.charAt(string.length() - 1);
		
		if (num == '5' || num  == '0')
			System.out.println("YES");
		else
			System.out.println("NO");
		
	}
	
}
