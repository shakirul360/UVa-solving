import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class New_Year_Chaos {

	public static void main(String[] args) {
		
		int tcase, n, t, i, j, temp1, total, bribes;
		Scanner input = new Scanner(System.in);
		
		tcase = input.nextInt();
		
		for (t = 0; t < tcase; t++) {
			
			n = input.nextInt();
			boolean flag = false;
			ArrayList<Integer> numbers = new ArrayList<Integer>();
			ArrayList<Integer> check = new ArrayList<Integer>();
			
			
			for (i = 1; i <= n; i++) {
				check.add(i);
				
			}
			
			for (i = 0; i < n; i++) {
				numbers.add(input.nextInt());
			}
			temp1 = n;
			total = 0;
			while (numbers.equals(check) == false) {
				i = temp1 - 1;
				j = i - 1;
				temp1--;
				bribes = 0;
				if (flag == true)
					break;
				
				
				while (check.get(i) != numbers.get(i)) {
					
					Collections.swap(check, i, j);
					i--;
					j--;
					total++;
					bribes++;
					if(bribes > 2) {
						flag = true;
						break;
					}
					
					
				}
			}
			if (flag == true) {
				System.out.println("Too chaotic");
			} else {
				System.out.println(total);
			}
		}
			
		}
			
}
			
