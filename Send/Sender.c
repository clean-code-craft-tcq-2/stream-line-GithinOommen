#include "Header.h"

FileStatus StatusData;
FileStatus ReadFile (int *SampleCount,char * filename,float *temp, float *soc, float *charge)
{
int i;
float parameter1, parameter2, parameter3;
   
   FILE *fptr;
   StatusData = OK;
   StatusData = FileOpenStatus (filename);
   if (StatusData)
    {
      fptr = fopen (filename, "r");
   
   for(i=0;fscanf(fptr,"%f\t%f\t%f", &parameter1,&parameter2,&parameter3)!=EOF;i++)
   {
        temp[i]=parameter1;
        soc[i]=parameter2;
        charge[i]=parameter3;     
   }
   *SampleCount=i;
   fclose(fptr); 
   }
   else
   {
   }
   
  return StatusData;
}
void DispReadData(float *temp, float *soc, float * charge)
{
        for(int i=0; i<SAMPLES;++i)
        {
                printf("%f\s%f\s%f", temp[i],soc[i],charge[i]);    
        }
        
}
FileStatus FileOpenStatus (char *filepath)
{
  int count = 0;
  char c;
  FILE *Pathfptr;
  char fileName[100];
  strcpy (fileName, filepath);
  Pathfptr = fopen (fileName, "r");
  // Extract characters from file
  // and store in character c
  if (Pathfptr != NULL)
  {
      for (c = getc (Pathfptr); c != EOF; c = getc (Pathfptr))

	// Increment count for this character
	count = count + 1;

      // Close the file
      fclose (Pathfptr);
    }
  return (count == 0) ? NOK : OK;
}
