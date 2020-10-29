package Mathematics;

import java.util.Scanner;

public class q4344 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int i, j, n, k = sc.nextInt();
		float aver, sum, count;
		float [][] student = new float[k][];
		
		for(i = 0; i<k; i++) {
			sum = 0;
			count = 0;
			n = sc.nextInt();
			student[i] = new float[n];
			
			for(j = 0; j<n; j++) {
				student[i][j] = sc.nextFloat();
				sum += student[i][j];
			}
			aver = sum/n;

			for(j = 0; j<n; j++) 
				if(student[i][j]>aver)
					count++;
			
			System.out.printf("%.3f%%\n",count/n*100f);
		}
	}
}
