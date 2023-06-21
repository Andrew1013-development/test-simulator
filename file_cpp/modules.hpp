#pragma once

namespace file_cpp {
    void version();
    std::tuple<double, unsigned long> generator_cpp(std::string directory, bool debug_short, bool debug_full, unsigned long dates);
    double sorter_cpp(std::string directory, bool debug_short, bool debug_full);
    double remover_cpp(std::string directory, bool debug_short, bool debug_full);
}