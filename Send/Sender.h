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
extern int SampleCount;
extern float Temperature[50];
extern  float StateOfCharge[50];
extern  float ChargeRate[50]
#endif
