#include <iostream>
#include <iomanip>
#include <tuple>
#include <chrono>
#include <cmath>
#include <string>
#include <csignal>
#include "modules.hpp"
using namespace std;

const string version = "1.0.0-WIP7";

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
        auto start = chrono::high_resolution_clock::now();
        tuple<double, unsigned long> generator_result = file_cpp::generator_cpp(test_dir,dbg_flag,dbgfull_flag,n_iters);
        double sorter_time = file_cpp::sorter_cpp(test_dir,dbg_flag,dbgfull_flag);
        double remover_time = file_cpp::remover_cpp(test_dir,dbg_flag,dbgfull_flag);
        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);
        double duration_num = duration.count() / pow(10,9);

        // set number output mode to have actual decimal points (another fuck you C++)
        cout << fixed << setprecision(3);
        cout << get<0>(generator_result) << " " << sorter_time << " " << remover_time << " " << get<1>(generator_result) << endl;
        cout << duration_num << endl;
    } else {
        cout << "no runner_cpp for you." << endl;
    }
    return 0;
}
