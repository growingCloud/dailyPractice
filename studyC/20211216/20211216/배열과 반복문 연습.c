#include<stdio.h>
#define NUM 10

// 1. �л� 5���� ������ ������ �迭�� ����
	// 2. 1���� ������ �迭�� �ݺ��� �̿��ؼ� ������� �Է� �޴´�
	// 3. ������ ������ �Ϸķ� ����Ѵ�
	// 4. �л����� ������ �հ�� ����� ����Ѵ�
	// 5. 1��� �������� ������ ����Ѵ�
int main() {

	int scores[NUM];
	int sum = 0, max = 0, min = 99999;
	double avg;


	for (int i = 0; i < NUM; i++) {
		printf("%d��° �л� : ", i + 1);
		scanf_s("%d", &scores[i]);

		sum += scores[i];

		if (max < scores[i]) { max = scores[i]; }
		if (min > scores[i]) { min = scores[i]; }
	}


	printf("\n���� ���)\n");

	for (int i = 0; i < NUM; i++) {
		printf("%d�� ", scores[i]);
	}


	avg = sum / (double)NUM;

	printf("\n\n�հ� : %d�� (= %.2lf��)\n", sum, avg);


	printf("\n1�� : %d, %d�� : %d\n", max, NUM, min);
}