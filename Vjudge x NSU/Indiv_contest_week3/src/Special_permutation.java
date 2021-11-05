import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Special_permutation {

	public static void main(String[] args) {
		
		int tcase, n;
		
		
		Scanner input = new Scanner(System.in);
		tcase = input.nextInt();
		
		for (int t = 0; t< tcase; t++) {
			ArrayList<Integer> nums = new ArrayList<Integer>();
			n = input.nextInt();
			
			for (int i = 1; i <= n; i++) {
				nums.add(i);
			}
			
			nums.sort(Collections.reverseOrder());
			if (n % 2 != 0 && n > 1) {

				int a = nums.get((n / 2) - 1);
				int b = nums.get((n / 2));
				nums.set((n / 2) - 1, b);
				nums.set(n / 2, a);
			}
			
			for (int i = 0; i < n; i++) {
				if (i == n - 1)
					System.out.println(nums.get(i));
				else
					System.out.print(nums.get(i) + " ");
					
			}
		}
		
		

	}

}
