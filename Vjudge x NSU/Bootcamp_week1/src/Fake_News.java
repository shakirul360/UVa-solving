import java.util.Scanner;

public class Fake_News {
	
	public static void main(String[] args) {
		
		String check = "heidi", s;
		int i, count = 0, current = 0;
		
		Scanner input = new Scanner(System.in);
		s = input.next();
		
		for (i = 0; i < s.length(); i++) {
			if (s.charAt(i) == check.charAt(current)) {
				count++;
				current++;
				if(count == 5) {
					break;
				}
			}
		}
		if (count == 5) {
			System.out.println("YES");
		} else {
			System.out.println("NO");
		}

	}

}
