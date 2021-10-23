import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Vector_Sort {

	public static void main(String[] args) {
		int n, i;
		
		ArrayList<Integer> numbers = new ArrayList<Integer>();
		Scanner input = new Scanner(System.in);
		
		n = input.nextInt();
		
		for (i = 0; i < n; i++) {
			numbers.add(input.nextInt());
		}

		Collections.sort(numbers);
		
		for (i = 0; i < n; i++) {
			if (i == n - 1)
				System.out.print(numbers.get(i));
			else
				System.out.print(numbers.get(i) + " ");
		}
		
	}

}
