#include<stdio.h>
#define NUM 10

// 1. 학생 5명의 점수를 저장할 배열를 선언
	// 2. 1번에 선언한 배열에 반복을 이용해서 순서대로 입력 받는다
	// 3. 저장한 점수를 일렬로 출력한다
	// 4. 학생들의 점수의 합계와 평균을 출력한다
	// 5. 1등과 마지막의 점수를 출력한다
int main() {

	int scores[NUM];
	int sum = 0, max = 0, min = 99999;
	double avg;


	for (int i = 0; i < NUM; i++) {
		printf("%d번째 학생 : ", i + 1);
		scanf_s("%d", &scores[i]);

		sum += scores[i];

		if (max < scores[i]) { max = scores[i]; }
		if (min > scores[i]) { min = scores[i]; }
	}


	printf("\n점수 목록)\n");

	for (int i = 0; i < NUM; i++) {
		printf("%d점 ", scores[i]);
	}


	avg = sum / (double)NUM;

	printf("\n\n합계 : %d점 (= %.2lf점)\n", sum, avg);


	printf("\n1등 : %d, %d등 : %d\n", max, NUM, min);
}