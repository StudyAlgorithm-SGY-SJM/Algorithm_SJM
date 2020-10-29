package Implementation;

import java.util.Arrays;
import java.util.Scanner;

public class q10817 {

	public static void main(String[] args) {
		int [] arr = new int[3];
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		for(int i=0; i<3; i++)
			arr[i] = sc.nextInt();
		Arrays.sort(arr);
		System.out.println(arr[1]);
	}
}
