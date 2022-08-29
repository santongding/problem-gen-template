cmake_minimum_required(VERSION 3.21)
project(problem_gen_template)

set(CMAKE_CXX_STANDARD 14)
set(CUR_PROB $ENV{CUR_PROB})

message("${CUR_PROB}")



aux_source_directory(./problems/${CUR_PROB}/std stds)

foreach(std ${stds})
    string(REGEX MATCHALL "[0-9A-Za-z_]*.cpp" tmp1 ${std})
    string(REGEX REPLACE ".cpp" "" tmp2 ${tmp1})
    add_executable(${tmp2} ${std})
endforeach()

