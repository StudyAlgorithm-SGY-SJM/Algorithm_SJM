package Implementation;

import java.util.Scanner;

public class q10871 {
	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		int n, k = sc.nextInt();
		int max = sc.nextInt();
		
		for(int i = 0; i< k;i++) {
			n = sc.nextInt();
			System.out.print((n<max)?n+" ":"");	
		}
	}
}
