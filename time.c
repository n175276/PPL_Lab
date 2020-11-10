#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

pthread_mutex_t lock;

int hrs = 0,min = 0,sec = 0;

pthread_t t1,t2,t3;

void *second(){
	
	while(1){
		printf("%d:%d:%d\n",hrs,min,sec);
		sleep(1);
		fflush(stdout);
		pthread_mutex_lock(&lock);
		sec++;
		pthread_mutex_unlock(&lock);
	}
	
}

void *minute(){
	
	while(1){
		if(sec == 60){
			sec = 0;
			pthread_mutex_lock(&lock);
			min++;
			pthread_mutex_unlock(&lock);
		}
	}
}
void *hour(){
	
	while(1){
		if(min == 60){
			min = 0;
			pthread_mutex_lock(&lock);
			hrs++;
			pthread_mutex_unlock(&lock);
		}
	}

}
int main(){
	pthread_mutex_init(&lock, NULL);
	
	pthread_create(&t1, NULL, second,NULL);
	pthread_create(&t2, NULL, minute,NULL);
	pthread_create(&t3, NULL, hour,NULL);
	pthread_join(t1,NULL);
	pthread_join(t2,NULL);
	pthread_join(t3,NULL);
	pthread_mutex_destroy(&lock);
	return 0;
}
