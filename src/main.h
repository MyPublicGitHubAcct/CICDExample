#pragma once

#include <iostream>
#include <string>
#include <sstream>

namespace patch
{
template <typename T>
std::string to_string(const T& n)
{
    std::ostringstream stm;
    stm << n;
    return stm.str();
}
} // namespace patch

struct SomeStruct
{
    std::string square(int x)
    {
        auto res = x * x;
        return patch::to_string(res); // g++ in Github does not have this in std!
    }
};

int main(int argc, const char* argv[]);