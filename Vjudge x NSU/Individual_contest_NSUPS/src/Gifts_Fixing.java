import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Gifts_Fixing {

	public static void main(String[] args) {
		int tcase, n, t, i, temp, ctotal, ototal, c, o, steps;
		
		ArrayList<Integer> chocs = new ArrayList<Integer>();
		ArrayList<Integer> oranges = new ArrayList<Integer>();
		Scanner input = new Scanner(System.in);
		tcase = input.nextInt();
		
		for (t = 0; t < tcase; i++) {
			steps = 0;
			ctotal = 0;
			ototal = 0;
			
			n = input.nextInt();
			
			for (i = 0; i < n; i++) {
				temp = input.nextInt();
				ctotal += temp;
				chocs.add(temp);
			}
			
			for (i = 0; i < n; i++) {
				temp = input.nextInt();
				ototal += temp;
				oranges.add(temp);
			}
			
			
			Collections.sort(chocs);
			Collections.sort(oranges);
			
			while ((ctotal / chocs.get(0) != chocs.get(0)) && ototal / oranges.get(0) != oranges.get(0)) {
				
				for (i = 0; i < 3; i++) {
					if (chocs.get(0) < chocs.get(i) && oranges.get(0) < oranges.get(1)) {
						ctotal -= chocs.get(i);
						ototal -= oranges.get(i);
						chocs.set(i, chocs.get(i) - 1);
						oranges.set(i, oranges.get(i) - 1);
					
						steps++;	
					}
					
					else if (chocs.get(0) < chocs.get(i)) {
						ctotal -= chocs.get(i);
						chocs.set(i, chocs.get(i) - 1);
						steps++;
					} else if (oranges.get(0) < oranges.get(i)) {
						ototal -= oranges.get(i);
						oranges.set(i, oranges.get(i) - 1);
						steps++;
					}
				}
			}
			
			System.out.println(steps);
			
		}

	}

}
