#include<stdio.h>

int str_join(char *a,  const char *b) {
   int sz =0; 
   while(*a++) sz++;  
   char *st = a -1, c;  
   *st = (char) 32;
   while((c = *b++)) *++st = c;  
   *++st = 0;
   return sz;
}

int main(){
	char a[] = "StringA"; 
    printf("string-1 length = %d, String a = %s\n", str_join(&a[0],"StringB"), a); 
}
