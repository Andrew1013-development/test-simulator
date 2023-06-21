#include <iostream>
#include <iomanip>
#include <tuple>
#include <chrono>
#include <cmath>
#include <string>
#include "modules.hpp"
using namespace std;

int main(int argc, char** argv) {
    string test = "amogus";
    
    auto start = chrono::steady_clock::now();
    tuple<double, unsigned long> gay_tuple = file_cpp::generator_cpp("Z:\\test-simulator\\test",false,false,5);
    double gay1 = file_cpp::sorter_cpp("Z:\\test-simulator\\test",false,false);
    double gay2 = file_cpp::remover_cpp("Z:\\test-simulator\\test",false,false);
    auto end = chrono::steady_clock::now();
    auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);
    double duration_num = duration.count() / pow(10,9);

    // set number output mode to have actual decimal points (another fuck you C++)
    cout << fixed << setprecision(3);
    cout << get<0>(gay_tuple) << " " << gay1 << " " << gay2 << " " << get<1>(gay_tuple) << endl;
    cout << duration_num << endl;
    
    return 0;
}