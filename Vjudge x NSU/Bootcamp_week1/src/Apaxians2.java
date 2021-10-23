import java.util.Scanner;

public class Apaxians2 {
	
	public static void main(String[] args) {
		String s;
		
		Scanner input = new Scanner(System.in);
		s = input.next();
		
		s = consec_remove(s);
		System.out.println(s);

	}
	public static String consec_remove(String s) {
		if (s.length() <= 1) {
			return s;
		} else if (s.charAt(0) == s.charAt(1)){
			return consec_remove(s.substring(1));
		} else {
			return s.charAt(0) + consec_remove(s.substring(1));
		}
	}
	
}
