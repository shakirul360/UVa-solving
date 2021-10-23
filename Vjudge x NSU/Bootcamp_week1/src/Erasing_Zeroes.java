import java.util.Scanner;

public class Erasing_Zeroes {

	public static void main(String[] args) {
		String s;
		int i, j, tcase, removed, x, y;
		
		Scanner input = new Scanner(System.in);
		
		tcase = input.nextInt();
		
		for (x = 0; x < tcase; x++) {
			s = input.next();
			removed = 0;
			
			for (i = 0; i < s.length() - 1; i++) {
				
				if (s.charAt(i) == '1') {
					j = i + 1;
					if (s.charAt(j) == '0') {
						y = j + 1;
						while (y <= (s.length() - 1) && s.charAt(y) != '1') {
							y++;
						}
						if (y <= (s.length() - 1) && s.charAt(y) == '1') {
							removed += y - i - 1;
						}
					}
				}
			}
			
			System.out.println(removed);
		}
		

	}

}
