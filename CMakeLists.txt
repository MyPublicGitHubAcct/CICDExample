cmake_minimum_required(VERSION 3.18.4)

set (BaseTargetName HelloWorld)

project(${BaseTargetName} VERSION 1.0.0)

Include(FetchContent)
FetchContent_Declare(
    Catch2
    GIT_REPOSITORY https://github.com/catchorg/Catch2.git
    GIT_TAG        v2.13.8)
FetchContent_MakeAvailable(Catch2)

set(CMAKE_CXX_STANDARD 17)

# build a library from the application code
add_library(${BaseTargetName} src/main.h src/main.cpp)

# build the executable from the library
add_executable(say_${BaseTargetName} src/main.cpp)
target_link_libraries(say_${BaseTargetName} PRIVATE ${BaseTargetName})
set_property(TARGET say_${BaseTargetName} PROPERTY ENABLE_EXPORTS 1) # to link from tests

# build a test runner application
enable_testing()
add_executable("${BaseTargetName}_tests" tests/Main.cpp tests/tests.cpp)
target_include_directories("${BaseTargetName}_tests" PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/src)
target_link_libraries("${BaseTargetName}_tests" PRIVATE Catch2::Catch2 ${BaseTargetName})
source_group(TREE ${CMAKE_CURRENT_SOURCE_DIR}/tests PREFIX "" FILES ${TestFiles})
include(${Catch2_SOURCE_DIR}/contrib/Catch.cmake)
catch_discover_tests("${BaseTargetName}_tests")
