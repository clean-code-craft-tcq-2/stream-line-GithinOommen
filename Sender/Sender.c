#include "Header.h"
void ReadFile(float *temp, float *soc, float * charge)
{

float parameter1, parameter2, parameter3;
   char *filename = "Sender.txt";
   FILE *fptr;

   if ((fptr = fopen(filename,"r")) == NULL){
       printf("\nError! opening file");

       // Program exits if the file pointer returns NULL.
       exit(1);
   }

   for(int i=0;fscanf(fptr,"%f\t%f\t%f", &parameter1,&parameter2,&parameter3)!=EOF;i++)
   {
        temp[i]=parameter1;
        soc[i]=parameter2;
        charge[i]=parameter3;     
   }

//printf("\nValue of parameter1=%f\tparameter2=%f\tparameter3=%f", temp[i],soc[i],charge[i]);
        
   //printf("\nValue of parameter1=%f\tparameter2=%f\tparameter3=%f", parameter1,parameter2,parameter3);
  // printf("\nValue of parameter1=%f\tparameter2=%f\tparameter3=%f", temp[0],soc[0],charge[0]);
   fclose(fptr); 
  
  // return 0;
}
