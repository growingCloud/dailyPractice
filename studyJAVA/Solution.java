// 프로그래머스 Lv.1 약수의 개수와 덧셈

// 두 정수 left와 right가 매개변수로 주어집니다. 
// left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 
// 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

// 입출력 예시 (1) : left = 13, right = 17 = 43
// 입출력 예시 (2) : left = 13, right = 17 = 43

class Solution {
    public int divisorNum(int num) {  // 약수의 개수를 구하는 메소드
        int count = 0;
        
        for (int divisor = 1; divisor <= num; divisor++) {
            if (num % divisor == 0) {
                count++;              // 나누어 떨어질때 마다 count를 하나씩 올려 반환
            }
        }
        return count;
    }
    
    public int solution(int left, int right) {
        int answer = 0;
        int i;
        
        for (i = left; i <= right; i++) {
            if(divisorNum(i) % 2 == 0) {
                answer += i;          // 약수의 개수 메서드를 반복문으로 활용
            }    
            else {
                answer -= i;          // 짝수이면 더하고, 홀수이면 빼는 방식으로 answer 반환
            }
        }
                
        return answer;
    }
}
