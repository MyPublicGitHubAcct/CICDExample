#include "catch2/catch.hpp"
#include "../src/main.h"

TEST_CASE("one is equal to one", "[dummy]")
{
    CHECK(1 == 1);
}

TEST_CASE("one is still equal to one", "[dummy2]")
{
    CHECK(1 == 1);
}

SomeStruct sstruct;

TEST_CASE("square is computed correctly", "[square]")
{
    REQUIRE(sstruct.square(5) == "25");
    REQUIRE(sstruct.square(6) == "36");
    REQUIRE(sstruct.square(7) == "40");
}
