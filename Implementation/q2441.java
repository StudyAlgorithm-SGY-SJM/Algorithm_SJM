package Implementation;

import java.util.Scanner;

public class q2441 {

	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner s = new Scanner(System.in);
		int num = s.nextInt();
		for(int i = 0;i<num;i++) {
			for(int j = 0;j<i;j++)
				System.out.print(" ");
			for(int k = i;k<num;k++)
				System.out.print("*");
			System.out.println();			
		}
	}
}
