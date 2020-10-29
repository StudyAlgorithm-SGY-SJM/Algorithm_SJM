package Mathematics;

import java.util.Scanner;

public class q2577 {

	public static void main(String[] args) {

		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
		String str = ""+ a*b*c;
		int [] cnt = new int [10];
		
		for(int i = 0; i<str.length(); i++) 
			cnt[str.charAt(i)-48]++ ;
		for(int i = 0; i<10; i++)
			System.out.println(cnt[i]);
	}
}

