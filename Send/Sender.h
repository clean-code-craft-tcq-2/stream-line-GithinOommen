#ifndef SENDER_H
#define SENDER_H
#include "Header.h"
#include <stdio.h>

typedef enum
{
        NOK,
        OK
}FileStatus;

FileStatus ReadFile(int *SampleCount,char * filename,float *temp, float *soc, float *charge);
void DispReadData(float *temp, float *soc, float *charge);
FileStatus FileOpenStatus (char *filepath);
#endif
