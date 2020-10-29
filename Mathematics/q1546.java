package Mathematics;

import java.util.Scanner;

public class q1546 {
	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		float [] arr = new float[n];
		float max = 0, sum = 0;		
		for(int i= 0; i<n; i++) {
			arr[i] = sc.nextFloat();
			if(max<arr[i])
				max = arr[i];
		}
		for(int i= 0; i<n; i++) {
			arr[i]=arr[i]/max*100f;
			sum+=arr[i];
		}
		System.out.println(sum/n);
	}
}
