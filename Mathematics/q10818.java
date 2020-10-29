package Mathematics;

import java.util.Scanner;

public class q10818 {
	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int [] arr = new int[n];
		int max = -1000001, min = 1000001;		
		for(int i= 0; i<n; i++) {
			arr[i] = sc.nextInt();
			if(max<arr[i])
				max = arr[i];
			if(min>arr[i])
				min = arr[i];
		}
		System.out.println(min+" "+max);
	}
}
