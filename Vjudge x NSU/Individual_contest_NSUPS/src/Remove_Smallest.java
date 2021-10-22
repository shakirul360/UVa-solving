import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Remove_Smallest {

	public static void main(String[] args) {
		
		int tcase, n, i, j, temp, a, b;
		boolean flag;

		ArrayList<Integer> digits = new ArrayList<Integer>();
		Scanner input = new Scanner(System.in);
		
		tcase = input.nextInt();
		
		for (int t = 0; t < tcase; t++) {
			flag = true;
			n = input.nextInt();
			
			for (i = 0; i < n; i++) {
				temp = input.nextInt();
				digits.add(temp);
			}
			
			Collections.sort(digits);
			
			i = 0;
			j = 1;
			
			while (flag == true && j < n) {
				if (digits.get(j) - digits.get(i) == 1 || digits.get(j) - digits.get(i) == 0 || n == 1) {
					i++;
					j++;
				} else {
					flag = false;
					break;
					
				}
			}
			if (flag == true) {
				System.out.println("YES");
			} else {
				System.out.println("NO");
			}
			
		}

	}

}
