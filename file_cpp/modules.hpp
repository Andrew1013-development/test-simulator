#pragma once
#include <string>
#include <tuple>
#include <vector>

namespace file_cpp {
    void version();
    void file_output(std::vector<double>* time_vec, std::string filename);
    std::tuple<double, std::vector<std::string>, unsigned long> seeker_cpp(std::string directory, bool debug_short, bool debug_full);
    double copier_cpp(std::string directory1, std::string directory2, bool debug_short, bool debug_full);
    std::tuple<double, unsigned long, std::vector<std::string>> generator_cpp(std::string directory, bool debug_short, bool debug_full, unsigned long dates);
    double sorter_cpp(std::string directory, std::vector<std::string> filename_list, bool debug_short, bool debug_full);
    double remover_cpp(std::string directory, bool debug_short, bool debug_full);
}