package Mathematics;

import java.util.Scanner;
public class q2884 {
	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		int h = sc.nextInt(), m = sc.nextInt();
		if(m-45<0) {
			m+=15;
			h = h<1? h+23: h-1;
		}
		else
			m-=45;
		System.out.println(h+" "+m);
	}
}
