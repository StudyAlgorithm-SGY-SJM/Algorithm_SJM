package Implementation;

import java.util.Scanner;

public class q2753 {
	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner s = new Scanner(System.in);
		int chk, year = s.nextInt();

		if((year%4==0&&year%100!=0)||year%400==0)  			chk = 1;
		else chk = 0;
		
		System.out.println(chk);
	}
}
