package DynamicProgramming;

import java.util.Scanner;

public class q2193 {

	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		long [] arr = new long [n+1];
		arr[0] = 1;
		arr[1] = 1;
		
		for(int i = 2; i< n; i++)
			arr[i] = arr[i-2]+arr[i-1];
		System.out.println(arr[n-1]);
	}

}
