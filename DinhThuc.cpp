// DinhThuc.cpp : Defines the entry point for the console application.
//


#include <iostream>
using namespace std;

float detA(int a[][100], int n)
{
	float det = 1;
	for (int i = 0; i < n - 1; i++)
	{
		//xet cac phan tu tren duong cheo chinh, neu co phan tu nao bang 0 thi doi cho hang do cho hang khac co phan tu tuong ung khac 0
		if (a[i][i] == 0)
		{
			int k = i + 1;
			while ((k < n) && a[k][i] == 0) k++; //tim dong k de doi cho
			if (k > n - 1) return 0;
			//doi cho dong i cho dong k
			det = -det;
			for (int j = i; j < n; j++) 
			{
				float temp = a[i][j];
				a[i][j] = a[k][j];
				a[k][j] = temp;
			}
		}
		for (int k = i + 1; k < n; k++) //dua ma tran ve dang tam giac tren
		{
			float d = -a[k][i] / a[i][i];
			for (int j = i; j < n; j++)
			{
				a[k][j] += d*a[i][j];
			}
		}
	}
	for (int i = 0; i < n; i++)
	{
		det *= a[i][i];
	}
	return det;
}
void nhap(int a[][100], int n)
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			cin >> a[i][j];
}
int main()
{
	int a[100][100];
	nhap(a, 3);
	int det = detA(a, 3);
	cout << det << endl;
	system("pause");
    return 0;
}

