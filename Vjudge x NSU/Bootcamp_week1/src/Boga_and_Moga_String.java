import java.util.Scanner;

public class Boga_and_Moga_String {

	public static void main(String[] args) {
		
		int size1, size2, i;
		Scanner input = new Scanner(System.in);
		
		StringBuilder string1= new StringBuilder(input.next());
		StringBuilder string2 = new StringBuilder(input.next());
		StringBuilder fin = new StringBuilder();
		
		size1= string1.length();
		size2 = string2.length();
		
		for(i = 0; i < size2; i++) {
			fin.append(string1.charAt(i));
			fin.append(string2.charAt(i));
		}
		
		if (size1 > size2) {
			fin.append(string1.charAt(size1 - 1));
		}
		System.out.println(fin);
	}

}
