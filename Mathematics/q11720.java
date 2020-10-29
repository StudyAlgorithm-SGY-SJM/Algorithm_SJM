package Mathematics;

import java.util.Scanner;

public class q11720 {
	
	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		int sum = 0, k = sc.nextInt();
		String n = sc.next();
		for(int i = 0; i<k; i++) {
			sum+=(n.charAt(i)-48);
		}
		System.out.println(sum);
	}

}
