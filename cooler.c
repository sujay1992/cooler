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
		fp=fopen("turnoff.txt","r");
		if(hr<8 && !fp)
		{
			fclose(fp);
			fp=fopen("turnoff.txt","w");
			fclose(fp);
			printf("Turning Off!\n");
			fp=fopen("output.txt","a");
			fprintf(fp,"Turning Off!\n");
			fclose(fp);
			system("soff >>output.txt");
			system("date >>output.txt");
			flag=0;
			system("poweroff &");
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
		fclose(fp);
	}
	system("rm turnoff.txt");
	float temp;
	fp=popen("vcgencmd measure_temp | cut -b 6,7,8,9","r");
	fscanf(fp,"%f",&temp);
	fclose(fp);
	fp=fopen("output.txt","a");
	printf("%2.1f %d ",temp,flag);
	fprintf(fp,"%2.1f %d ",temp,flag);
	fclose(fp);
	system("date >>output.txt");
	if(temp<mintemp)
	{
		printf("Too Cool!\n");
		system("echo 'Too Cool!' >>output.txt");
		if(flag>=0 || flag<=-20)
		{
			system("soff");
			system("echo 'soff' >>output.txt");
			flag=0;
		}
		system("sleep 60");
		flag--;
	}
	else if(temp>maxtemp)
	{
		printf("Too Hot!\n");
		system("echo 'Too Hot!' >>output.txt");
		if(flag<=0 || flag>=20)
		{
			system("son");
			system("echo 'son' >>output.txt");
			flag=0;
		}
		system("sleep 60");
		flag++;
	}
	else
	{
		printf("Temperature under control!\n");
		system("echo 'Temperature under control!' >>output.txt");
	}
	}while(1);
	return 0;
}
