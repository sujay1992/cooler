#include<stdlib.h>
#include<stdio.h>
#include<time.h>

float getmax()
{
	FILE *fp=fopen("maxtemp.txt","r");
	float temp;
	fscanf(fp,"%f",&temp);
	fclose(fp);
	/*if(temp<20 || temp>50)
		return 42.5;*/
	return temp;
}

float getmin()
{
	FILE *fp=fopen("mintemp.txt","r");
	float temp;
	fscanf(fp,"%f",&temp);
	fclose(fp);
	/*if(temp<20 || temp>50)
		return 42.5;*/
	return temp;
}

int main(int argc, char* argv[])
{
	FILE *fp;
	int flag=0;
	do{
	float mintemp=getmin(),maxtemp=getmax();
	system("sleep 5");
	time_t now;
	time(&now);
	struct tm *local=localtime(&now);
	int hr=local->tm_hour;
	/*if(hr<1)
	{
		printf("Time < 0100\n");
		fp=fopen("output.txt","a");
		fprintf(fp,"Time < 0100\n");
		fclose(fp);
		system("date >>output.txt");
		system("sleep 300");
		return 1;
	}
	else*/ if(hr>=7)
	{
		if(hr<8)
		{
			printf("Turning Off!\n");
			fp=fopen("output.txt","a");
			fprintf(fp,"Turning Off!\n");
			fclose(fp);
			system("soff >>output.txt");
			system("date >>output.txt");
			flag=0;
			system("sudo poweroff");
			return 1;
		}
		else if(hr<=23)
		{
			printf("Time <= 2300\n");
			fp=fopen("output.txt","a");
			fprintf(fp,"Time <= 2300\n");
			fclose(fp);
			system("date >>output.txt");
			system("sleep 300");
			return 1;
		}
	}
	float temp;
	fp=popen("sudo vcgencmd measure_temp | cut -b 6,7,8,9","r");
	fscanf(fp,"%f",&temp);
	fclose(fp);
	printf("%2.1f %d ",temp,flag);
	system("date");
	if(temp<mintemp)
	{
		printf("Too Cool!\n");
		if(flag>=0 || flag<=-20)
		{
			system("soff");
			flag=0;
		}
		system("sleep 60");
		flag--;
	}
	else if(temp>maxtemp)
	{
		printf("Too Hot!\n");
		if(flag<=0 || flag>=20)
		{
			system("son");
			flag=0;
		}
		system("sleep 60");
		flag++;
	}
	else
	{
		printf("Temperature under control!\n");
	}
	}while(1);
	return 0;
}
