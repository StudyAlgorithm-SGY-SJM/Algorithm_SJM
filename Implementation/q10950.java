package Implementation;

import java.util.Scanner;

public class q10950 {
	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner s = new Scanner(System.in);
		int num = s.nextInt();
			
		for(int i = 0; i< num; i++) {
			int a = s.nextInt();
			int b = s.nextInt();
			System.out.println(a+b);
		}
	}
}

