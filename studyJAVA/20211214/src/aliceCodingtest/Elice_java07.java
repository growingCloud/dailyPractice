package aliceCodingtest;

import java.util.*;

public class Elice_java07 {
	public static void main(String[] args) {

		// �䳢�� �޽Ľð� N�� �ź����� �޽Ľð� M�� �Ű� ������ �־�������, 
		// �䳢�� �ź��̰� ���ÿ� �޽��ϴ� ������ �ð��� ����ϴ� ���α׷��� �ۼ��غ��ô�. (�ּҰ����)
		
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
