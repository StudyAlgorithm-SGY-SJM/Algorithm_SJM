package Implementation;

import java.util.Scanner;

public class q11022 {
	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner s = new Scanner(System.in);
		int a,b,num = s.nextInt();
			
		for(int i = 0; i< num; i++) {
			a = s.nextInt();
			b = s.nextInt();
			System.out.println("Case #"+(i+1)+": "+a+" + "+b+" = "+(a+b));
		}
	}
}
