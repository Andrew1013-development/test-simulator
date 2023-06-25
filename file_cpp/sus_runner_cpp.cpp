#include <iostream>
#include <iomanip>
#include <tuple>
#include <vector>
#include <chrono>
#include <cmath>
#include <string>
#include <csignal>
#include "modules.hpp"
using namespace std;

const string version = "1.1.2";

int main(int argc, char** argv) {
    signal(SIGINT, exit); //bind SIGINT (Ctrl-C) to exit
    string test_dir;
    bool dbg_flag = false;
    bool dbgfull_flag = false;
    unsigned long n_iters = 1;

    // input (type-cast the hell outta this because C++ thinks an array of chars is different from a string)
    // also damn C++ finally being more accessible once you get to know the STL huh
    if (argc == 5) {
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

        // main code
        tuple<double, unsigned long, vector<string>> generator_result = file_cpp::generator_cpp(test_dir,dbg_flag,dbgfull_flag,n_iters);
        auto start = chrono::high_resolution_clock::now();
        //double copier_time = file_cpp::copier_cpp(test_dir,test_dir2,dbg_flag,dbgfull_flag);
        double sorter_time = file_cpp::sorter_cpp(test_dir,get<2>(generator_result),dbg_flag,dbgfull_flag);
        double remover_time = file_cpp::remover_cpp(test_dir,dbg_flag,dbgfull_flag);
        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);
        double duration_num = duration.count() / pow(10,9);
        //file_cpp::remover_cpp(test_dir2,dbg_flag,dbgfull_flag);

        // set number output mode to have actual decimal points (another fuck you C++)
        cout << fixed << setprecision(3);
        cout << "----------------------------EXECUTION INFORMATION (C++ REIMPLEMENTATION)---------------------------" << endl;
        cout << "Total time to execute all 2 functions (runner time): " << duration_num  << " seconds" << endl;
        cout << "Individual time of each segment (individual function time):" << endl;
        //cout << "\tGenerator : " << get<0>(generator_result) << " seconds (" << get<0>(generator_result) / duration_num * 100 << "% of runtime)" << endl; 
        //cout << "\t Copier : " << copier_time << " seconds (" << copier_time / duration_num * 100 << "% of runtime)" << endl;
        cout << "\tSorter : " << sorter_time << " seconds (" << sorter_time / duration_num * 100 << "% of runtime)" << endl;
        cout << "\tRemover : " << remover_time << " seconds (" << remover_time / duration_num * 100 << "% of runtime)" << endl;
        cout << "Files sorted: " << get<1>(generator_result) << endl;
        cout << endl;
    } else {
        cout << "no runner_cpp for you." << endl;
    }
    return 0;
}
