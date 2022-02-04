package lectureStudy;

public class operator {
		public static void main(String[] args) {
			// 증감연산자와 전치, 후치의 차이점 비교
			// 증감 연산자 : 피연산자를 1 증가 혹은 1 감소 시키는 연산자
			
			int n = 10;
			
			n++;	// 후치 : 연산자가 뒤에 붙은 경우
			System.out.println("n = " + n);
			
			n--;
			System.out.println("n = " + n);
			
			++n;	// 전치 : 연산자가 앞에 붙은 경우
			System.out.println("n = " + n);
			
			--n;
			System.out.println("n = " + n + "\n");
			
			// 기본적으로 전치나 후치는 차이가 없지만,  다른 연산자와 섞어서 사용하면 차이가 나타난다
			
			int n1 = 10, n2, n3;
			
			n2 = ++n1;		// 전치 : 증감 후 다른 연산
			System.out.println("n1 = " + n1 + ", n2 = " + n2);
			
			n1 = 10;
			
			n3 = n1++;		// 후치 : 다른 연산 후 증감
			System.out.println("n1 = " + n1 + ", n3 = " + n3 + "\n");
			
			
			int a = 7, b = 3, c = 1, d = 5, e;
			
			e = ++a + b-- + --c + d++;
//			e =  8  +  3  +  0  +  5 = 16
//			           2           6
			
			System.out.println("a = " + a);		// a = 8
			System.out.println("b = " + b);		// b = 2
			System.out.println("c = " + c); 	// c = 0
			System.out.println("d = " + d);		// d = 6
			System.out.println("e = " + e);		// e = 16
			
		}
	}
