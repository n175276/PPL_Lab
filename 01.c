#include<stdio.h>
int main(){
	char a[100] ;
	gets(a);
	char b[5];
	int i;
	for (i=0 ; i<100 ; i++)
	{
		b[i]=a[i];
		
	}
	for (i=0 ; i<6 ; i++){
		printf("%s",b[i]);
	}
}
