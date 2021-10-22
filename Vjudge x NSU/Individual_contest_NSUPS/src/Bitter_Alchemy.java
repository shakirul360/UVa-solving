import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Bitter_Alchemy {

	public static void main(String[] args) {
		
		int n, x, temp, total = 0, count = 0, lowest;
		ArrayList<Integer> donuts = new ArrayList<Integer>();
		
		Scanner input = new Scanner(System.in);
		n = input.nextInt();
		x = input.nextInt();
		
	
		
		for (int i = 0; i < n; i++) {
			temp = input.nextInt();
			donuts.add(temp);
			total += temp;
			count++;
		}
		
		Collections.sort(donuts);
		
		lowest = donuts.get(0);
		
		x = x - total;
		
		count += x / lowest;
		count = (int) count;
		
		System.out.println(count);
		
		
	}

}
