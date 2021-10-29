import java.util.Scanner;

public class Echo {

	public static void main(String[] args) {
		
		int n, i;
		boolean flag = false;
		
		String str, sub;
		
		Scanner input = new Scanner(System.in);
		n = input.nextInt();
		str = input.next();
		
		for (i = 2; i <= n / 2; i++) {
			sub = str.substring(0, i);
			//System.out.println(sub);
			if (concat(str, sub) == true) {
				flag = true;
				break;
			}	
		}
		if (flag == true) {
			System.out.println("Yes");
		} else {
			System.out.println("No");
		}
		
	
	}
	
	static boolean concat(String str1, String str2) {

		int n = str1.length();

		int n2 = str2.length();
	
		if (n %  n2 != 0){
			return false;
		}
		
		for (int i = 0; i < n; i++){
			if (str1.charAt(i) != str2.charAt(i % n2)){
			return false;
			}
		}
		return true;
		}
}
