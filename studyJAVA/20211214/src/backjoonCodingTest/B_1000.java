package backjoonCodingTest;

import java.util.Scanner;

public class B_1000 {
	public static void main(String[] args) {
					
			Scanner scan = new Scanner(System.in);
			
			int a, b;

			System.out.print("정수 입력 : ");
			a = scan.nextInt();
			b = scan.nextInt();
			
			System.out.println("a + b = " + (a + b));
			
			scan.close();		
	}
}

