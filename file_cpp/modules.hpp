#pragma once

namespace file_cpp {
    void version();
    std::tuple<double, unsigned long, std::vector<std::string>> generator_cpp(std::string directory, bool debug_short, bool debug_full, unsigned long dates);
    double sorter_cpp(std::string directory, std::vector<std::string> filename_list, bool debug_short, bool debug_full);
    double remover_cpp(std::string directory, bool debug_short, bool debug_full);
}