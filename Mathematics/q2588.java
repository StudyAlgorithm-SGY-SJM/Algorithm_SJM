package Mathematics;

import java.util.Scanner;

public class q2588 {

	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(), b = sc.nextInt();
		int [] n = new int[3];
		int ans = a*b;
		for(int i = 0; i<3; i++) {
			n[i]=a*(b%10);
			b/=10;
		}
		System.out.println(n[0]+"\n"+n[1]+"\n"+n[2]+"\n"+ans);

	}

}
