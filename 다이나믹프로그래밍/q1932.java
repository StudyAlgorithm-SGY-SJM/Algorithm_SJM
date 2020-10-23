package DynamicProgramming;

import java.util.Scanner;

public class q1932 {

	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		int k = sc.nextInt();
		int [][] arr = new int [k+1][k+1];
		for(int i = 0; i<k; i++)
			for (int j = 0; j<=i; j++)
			{
				arr[i][j] += sc.nextInt();
				if(i != k-1)
				{
					arr[i+1][j] = Math.max(arr[i][j], arr[i+1][j]);
					arr[i+1][j+1] = Math.max(arr[i][j], arr[i+1][j+1]);		
				}
			}	
		int max = 0;
		for(int i=0;i<k;i++)
			if(max < arr[k-1][i])
				max = arr[k-1][i];
		System.out.println(max);
	}
}
