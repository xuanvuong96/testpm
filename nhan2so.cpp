// nhan2so.cpp : Defines the entry point for the console application.
//


#include <stdio.h>
#include <iostream>

using namespace std;

void cong(char a[], char b[], int m, int n, int k)
{
	char tong[100];
	int min = m;
	int nho = 0;
	if (m>n + k) min = n + k;
	for (int i = 0; i<k; i++)
		tong[i] = a[i];
	for (int i = k; i<min; i++)
	{
		tong[i] = (a[i] + b[i - k] + nho) % 10;
		nho = (a[i] + b[i - k] + nho) / 10;
	}
	for (int i = min; i<m; i++)
	{
		tong[i] = (a[i] + nho) % 10;
		nho = (a[i] + nho) / 10;
	}
	for (int i = min; i<n + k; i++)
	{
		tong[i] = (b[i - k] + nho) % 10;
		nho = (b[i - k] + nho) / 10;
	}
	int max = m;
	if (max<n + k) max = n + k;
	if (nho>0) tong[max] = nho;
	for (int i = 0; i <= max; i++) a[i] = tong[i];
}

void nhan(char a[], char b, char tich[], int m)
{
	int nho = 0;
	for (int i = 0; i < m; i++)
	{
		tich[i] = (a[i] * b + nho) % 10;
		nho = (a[i] * b + nho) / 10;
	}
	if (nho > 0)
	{
		tich[m] = nho;
	}
}
void nhan(char a[], char b[], char kq[], int m, int n)
{
	for (int i = 0; i < n; i++)
	{
		char tich[100];
		for (int i = 0; i < 100; i++) tich[i] = 0;
		nhan(a, b[i], tich, m);
		cong(kq, tich, m+i, m+i+1, i);
	}
}
int main()
{
	char a[] = { 9,9,9,9,9 };
	char b[] = { 9,9,9,9,9 };
	char kq[100];
	for (int i = 0; i < 100; i++) kq[i] = 0;
	nhan(a, b, kq, 5, 5);
	for (int i = 5 + 5 - 1; i >= 0; i--) cout << (int)kq[i];
	cout << endl;
	system("pause");
	return 0;
}
