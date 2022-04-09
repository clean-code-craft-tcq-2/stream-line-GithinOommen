#ifndef SENDER_H
#define SENDER_H
#include "Header.h"

void ReadFile(char * filename,float *temp, float *soc, float *charge);
void DispReadData(float *temp, float *soc, float *charge);
#endif
