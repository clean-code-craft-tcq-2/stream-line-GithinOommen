#define CATCH_CONFIG_MAIN 

#include "test/catch.hpp"
#include "Header.h"

TEST_CASE("Test for read of data from file ") 
{
  float Temperature[SAMPLES] = {0};
  float SoC[SAMPLES] = {0};
  float ChargeRate[SAMPLES] = {0};
  ReadFile( Temperature,SoC,ChargeRate);
  DispReadData( Temperature,SoC,ChargeRate);
  
  float expectedoutput[3] = {10,65,0.010};
  
  REQUIRE(Temperature[0] == expectedoutput[0]);
  REQUIRE(StateOfCharge[0] == expectedoutput[1]);
  REQUIRE(ChargeRate[0] == expectedoutput[2]);
  
}
