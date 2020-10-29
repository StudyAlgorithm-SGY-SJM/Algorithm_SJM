package Implementation;

import java.util.Scanner;

public class q8393 {
	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner s = new Scanner(System.in);
		int num = s.nextInt();
		int sum = 0;
		for(int i = 1; i<=num; i++)
			sum += i;
		System.out.println(sum);
	}
}
