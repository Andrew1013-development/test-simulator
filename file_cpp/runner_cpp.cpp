#include <iostream>
#include <iomanip>
#include <tuple>
#include <vector>
#include <chrono>
#include <cmath>
#include <string>
#include <csignal>
#include "modules.hpp"
#define VERSION "1.0.3"
using namespace std;

int main(int argc, char** argv) {
    signal(SIGINT, exit); //bind SIGINT (Ctrl-C) to exit
    string test_dir;
    bool dbg_flag = false;
    bool dbgfull_flag = false;
    bool file_output = true;
    unsigned long n_iters = 1;
    vector<double> time_results;

    // input (type-cast the hell outta this because C++ thinks an array of chars is different from a string)
    // also damn C++ finally being more accessible once you get to know the STL huh
    if (argc == 6) {
        test_dir = argv[1];
        if ((string)argv[2] == "-debug") {
            dbg_flag = true;
        } else {
            if ((string)argv[2] == "-nodebug") {
                dbg_flag = false;
            } else {
                cout << "invalid choice for debug flag." << endl;
            }
        }
        if ((string)argv[3] == "-fulldebug") {
            dbgfull_flag = true;
        } else {
            if ((string)argv[3] == "-nofulldebug") {
                dbgfull_flag = false;
            } else {
                cout << "invaild choice for full debug flag" << endl;
            }
        } 
        n_iters = stoul(argv[4]); //convert string to unsigned long
        if ((string)argv[5] == "-file") {
            file_output = true;
        } else {
            if ((string)argv[5] == "-nofile") {
                file_output = false;
            } else {
                cout << "invaild choice for file output flag" << endl;
            }
        }
        // main code
        auto start = chrono::high_resolution_clock::now();
        tuple<double, unsigned long, vector<string>> generator_result = file_cpp::generator_cpp(test_dir,dbg_flag,dbgfull_flag,n_iters);
        double sorter_time = file_cpp::sorter_cpp(test_dir,get<2>(generator_result),dbg_flag,dbgfull_flag);
        double remover_time = file_cpp::remover_cpp(test_dir,dbg_flag,dbgfull_flag);
        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);
        double duration_num = duration.count() / pow(10,9);
        double delta_time = duration_num - get<0>(generator_result) - sorter_time - remover_time; 
        
        // result collection
        time_results.push_back(n_iters);
        time_results.push_back(duration_num);
        time_results.push_back(get<0>(generator_result));
        time_results.push_back(sorter_time);
        time_results.push_back(remover_time);
        time_results.push_back(delta_time);
        time_results.push_back(get<1>(generator_result));
        
        // set number output mode to have actual decimal points (another fuck you C++)
        cout << fixed << setprecision(3);
        cout << "----------------------------EXECUTION INFORMATION (C++ REIMPLEMENTATION)---------------------------" << endl;
        cout << "Total time to execute all 3 functions (runner time): " << duration_num  << " seconds" << endl;
        cout << "Individual time of each segment (individual function time):" << endl;
        cout << "\tGenerator : " << get<0>(generator_result) << " seconds (" << get<0>(generator_result) / duration_num * 100 << "% of runtime)" << endl; 
        cout << "\tSorter : " << sorter_time << " seconds (" << sorter_time / duration_num * 100 << "% of runtime)" << endl;
        cout << "\tRemover : " << remover_time << " seconds (" << remover_time / duration_num * 100 << "% of runtime)" << endl;
        cout << "\tTime dilation (delta) : " << delta_time << " seconds (" << delta_time / duration_num * 100 << "% of runtime)" << endl; 
        cout << "Files sorted: " << get<1>(generator_result) << endl;

        if (file_output) {
            file_cpp::file_output(&time_results, "runtime_iterations_information.txt");
        }
        cout << endl;
    } else {
        cout << "no runner_cpp for you." << endl;
    }
    return 0;
}
