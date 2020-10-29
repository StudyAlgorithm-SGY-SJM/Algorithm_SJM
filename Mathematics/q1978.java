package Mathematics;

import java.util.Scanner;

public class q1978 {
	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		int cnt = 0, n = sc.nextInt();	
		int [] arr = new int[n];
		boolean prime = true;
		
		for(int i= 0; i<n; i++) {
			arr[i] = sc.nextInt();
			if(arr[i]==1)
				prime = false;
			else if(arr[i]==2)
				prime = true;
			else {
				prime = true;
				for(int j=2; j<arr[i]; j++)
					if(arr[i]%j==0) {
						prime = false;
						break;
					}
			}
			if(prime == true) cnt++;		
		}
		System.out.println(cnt);
	}
}
