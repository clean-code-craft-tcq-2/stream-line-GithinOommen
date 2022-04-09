#define CATCH_CONFIG_MAIN 

#include "test/catch.hpp"
#include "Header.h"

TEST_CASE("Test for read of data from file ") 
{
  int SampleCount;
  float Temperature[SAMPLES] = {0};
  float SoC[SAMPLES] = {0};
  float ChargeRate[SAMPLES] = {0};
  char *filename = "./Send/Sender.txt";
  ReadFile( &SampleCount,filename,Temperature,SoC,ChargeRate);
  DispReadData( Temperature,SoC,ChargeRate);
  
  float expectedoutput[3] = {10,65,0.010};
  
  REQUIRE(Temperature[0] == expectedoutput[0]);
  REQUIRE(SoC[0] == expectedoutput[1]);
  REQUIRE(ChargeRate[0] == expectedoutput[2]);
  
}
TEST_CASE("Check the count of Samples read "){
  int SampleCount;
   float Temperature[SAMPLES] = {0};
  float SoC[SAMPLES] = {0};
  float ChargeRate[SAMPLES] = {0};
  char *filename = "./Send/Sender.txt";
  ReadFile( &SampleCount,filename,Temperature,SoC,ChargeRate);
  REQUIRE(SampleCount== 50);
  }
