package Mathematics;

import java.util.Scanner;
public class q2292 {
	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		int i, j, n = sc.nextInt();
		int [] arr = new int [19000];
		
		for(arr[0] = 1,i = 1;arr[i-1]<=n;i++) 
			arr[i] = arr[i-1]+(i*6);
			
		for(j = 0;j<i;j++) {
			if(n>arr[j]) continue;
			break;
		}
		System.out.println(j+1);
	}
}
