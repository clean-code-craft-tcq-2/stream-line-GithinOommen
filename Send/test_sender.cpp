#define CATCH_CONFIG_MAIN 

#include "test/catch.hpp"
#include "Header.h"


  char *filename = "./Send/Sender.txt";
        int SampleCount;
  float Temperature[] = { 0 };
  float StateOfCharge[] = { 0 };
  float ChargeRate[] = { 0 };
TEST_CASE("Test for read of data from file ") 
{

  ReadFile( &SampleCount,filename,Temperature,SoC,ChargeRate);
  DispReadData( Temperature,SoC,ChargeRate);
  
  float expectedoutput[3] = {10,65,0.010};
  
  REQUIRE(Temperature[0] == expectedoutput[0]);
  REQUIRE(SoC[0] == expectedoutput[1]);
  REQUIRE(ChargeRate[0] == expectedoutput[2]);
  
}
TEST_CASE("Check the count of Samples read "){

  ReadFile( &SampleCount,filename,Temperature,SoC,ChargeRate);
  REQUIRE(SampleCount== 50);
  }
