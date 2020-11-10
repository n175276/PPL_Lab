#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
int hour, minute, second;

void *secondFun(void *vargs){
	while(1){
		if(second != 60){
			sleep(1);
			second++;
		}
	}
	return NULL;
}

void *minuteFun(void *vargs){
	while(1){
		if(second == 60){
			minute++;
			second = 0;
		}
	}
	return NULL;
}

void *hourFun(void *vargs){
	while(1){
		if(minute == 60){
			minute = 0;
			second = 0;
			if(hour == 24){
				hour = 0;
			}
			else{
				hour++;
			}	
		}
		
	}
}

void *display(void *vargs){
	while(1){
		printf("\r %02d : %02d : %02d", hour, minute, second);
	}
	return NULL;	
}

int main(){
	time_t mytime;
	time(&mytime);
	struct tm *local_time = localtime(&mytime);
	hour = local_time -> tm_hour;
	minute = local_time -> tm_min;
	second = local_time -> tm_sec; 	
	pthread_t thread_s, thread_m, thread_h, thread_print;
	
	pthread_mutex_init(&lock, NULL);

	pthread_create(&thread_s, NULL, secondFun , NULL);
	pthread_create(&thread_m, NULL, minuteFun , NULL);
	pthread_create(&thread_h, NULL, hourFun , NULL);
	pthread_create(&thread_print, NULL, display , NULL);
	
	pthread_join(thread_s, NULL);
	pthread_join(thread_m, NULL);
	pthread_join(thread_h, NULL);
	pthread_join(thread_print, NULL);		
	pthread_mutex_destroy(&lock);
	return 0;
}
