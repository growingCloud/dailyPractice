package aliceCodingtest;

import java.util.*;

public class Elice_java07 {
	public static void main(String[] args) {

		// 토끼의 휴식시간 N과 거북이의 휴식시간 M이 매게 변수로 주어졌을때, 
		// 토끼와 거북이가 동시에 휴식하는 최초의 시간을 출력하는 프로그램을 작성해봅시다. (최소공배수)
		
		int rabbit, turtle;
	    Scanner scan = new Scanner(System.in);
		        
		rabbit = scan.nextInt();
		turtle = scan.nextInt();
		        
		int max;
		int resMin = 0;
		        
		if (turtle >= rabbit) { max = turtle; }
		else {max = rabbit;}
		        
		for (int i = max; i >= max; i++) {
		    if (i % rabbit == 0 && i % turtle == 0) {
		         resMin = i;
		         break;}
		    }
		        
		System.out.println(resMin);
		
		scan.close();

	}
}
