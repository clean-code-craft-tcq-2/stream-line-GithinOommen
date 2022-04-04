#define CATCH_CONFIG_MAIN 

#include "test/catch.hpp"
#include "Sender/Header.h"

TEST_CASE("Test for read of data from file ") 
{
  float Temperature[SAMPLES] = {0};
  float SoC[SAMPLES] = {0};
  float ChargeRate[SAMPLES] = {0};
  ReadFile( Temperature,SoC,ChargeRate);
  
}
