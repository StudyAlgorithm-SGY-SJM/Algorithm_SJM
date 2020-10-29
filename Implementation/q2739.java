package Implementation;

import java.util.Scanner;

public class q2739 {

	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner s = new Scanner(System.in);
		int num = s.nextInt();
		for(int i = 1; i< 10; i++)
			System.out.println(num+" * "+i+" = "+(i*num));
		
	}

}
