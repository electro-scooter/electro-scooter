#include <iostream>
//#include <windows.h>
using namespace std;
int main()
{


int day = 1;
int year = 1;
char month [10];
printf("Программа работает \n"); //вывод на экран
scanf("%d %d", &day, &year); // первая часть - форматная строка, вторая часть - параметры ввода с клавиатуры
scanf("%s", month);
printf("Сегодня %d %s %d\n", day, month, year);

//system("pause");
}