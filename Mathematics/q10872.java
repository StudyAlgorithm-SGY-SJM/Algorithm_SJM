package Mathematics;

import java.util.Scanner;

public class q10872 {
	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();	
		long result = 1;
		for(int i= 1; i<=n; i++)
			result*=i;
		System.out.println(result);
	}
}
