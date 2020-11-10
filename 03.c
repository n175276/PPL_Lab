#include<stdio.h>
void get_name(){
  char buffer[10];
  gets(buffer);
}
int main() {
    printf("Please enter your name.");
    get_name();
    return 0;
}
