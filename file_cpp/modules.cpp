#include <filesystem>
#include <fstream>
#include <iostream>
#include <chrono>
#include <random>
#include <string>
#include <map>
#include <tuple>
#include <vector>
#include <format>
#include <cmath>
#include <iomanip>
#include "modules.hpp"
using namespace std;

namespace file_cpp {
    string random_string(unsigned long length) {
    string rnd_str = "";
    random_device string_generator;
    uniform_int_distribution string_distributor(65,122);

    for (int i = 0; i < length; i++) {
        rnd_str += (char)string_distributor(string_generator);
    }

    return rnd_str;
}

    string filename_extractor(string basepath) {
        // get substring from the last position of the path delimiters
        string filename = basepath.substr(basepath.find_last_of("/\\") + 1);
        return filename;
    }

    void copy_file(string path1, string path2) {
        string buffer;
        ifstream old_f(path1);
        ofstream new_f(path2);
        while (!old_f.eof()) {
            old_f >> buffer;
        }
        new_f << buffer;
        old_f.close();
        new_f.close();
    }

    void move_file(string path1, string path2) {
        copy_file(path1, path2);
        filesystem::remove(path1);
    }

    tuple<double, unsigned long> generator_cpp(string directory, bool debug_short, bool debug_full, unsigned long dates) {
        map<string, unsigned long> table;
        vector<string> dates_vec;
        vector<unsigned long> file_nums;
        unsigned long total_files = 0;
        vector<string> file_check;
        random_device generator;
        ofstream fout;
        
        // create test folder
        cout << "Creating test folder...." << endl;
        filesystem::create_directories(directory);

        // generating dates
        cout << "Creating test files....." << endl;
        auto start = chrono::steady_clock::now();
        for (unsigned long i = 0; i < dates; i++) {
            string datename = "";

            // create random distributors
            uniform_int_distribution<unsigned long> year_distribution(2010,2023);
            uniform_int_distribution<unsigned long> month_distribution(1,12);
            uniform_int_distribution<unsigned long> day_distribution(1,28);

            // run distributors on generators to get random number
            unsigned long year = year_distribution(generator);
            unsigned long month = month_distribution(generator);     
            unsigned long day = day_distribution(generator);       
            
            // string formatting (fuck you C++ for no Python combined string formatting bru)
            datename += to_string(year);
            datename += to_string(month).insert(0,2 - to_string(month).length(),'0');
            datename += to_string(day).insert(0,2 - to_string(day).length(),'0');
            
            uniform_int_distribution<unsigned long> files_distribution(10,1000);
            unsigned long files = files_distribution(generator);       
            
            dates_vec.push_back(datename);
            file_nums.push_back(files);
            total_files += files;
        }

        // create test files
        for (unsigned long i = 0; i < dates; i++) {
            for (unsigned long j = 0; j < file_nums.at(i); j++) {
                string filename = "";
                
                // more generation
                uniform_int_distribution<unsigned long> hour_distribution(0,23);
                uniform_int_distribution<unsigned long> minute_distribution(0,59);
                uniform_int_distribution<unsigned long> second_distribution(0,59);

                unsigned long hour = hour_distribution(generator);
                unsigned long minute = minute_distribution(generator);     
                unsigned long second = second_distribution(generator);

                // more string formatting
                filename += dates_vec.at(i);
                filename += '_';
                filename += to_string(hour).insert(0,2 - to_string(hour).length(),'0');
                filename += to_string(minute).insert(0,2 - to_string(minute).length(),'0');
                filename += to_string(second).insert(0,2 - to_string(second).length(),'0');

                for (int e = 0; e < file_check.size(); e++) {
                    if (file_check.at(e) == filename) {
                        uniform_int_distribution<unsigned long> more_name_distribution(1,25);
                        unsigned long length = more_name_distribution(generator);
                        filename += random_string(length);
                    }
                }


                file_check.push_back(filename);
                
                // string -> path
                filename += ".txt";
                filesystem::path converted_directory = directory;
                filesystem::path converted_filename = filename;
                filesystem::path file_dir = converted_directory / converted_filename;
                
                // write files
                fout.open(file_dir);
                fout << dates_vec.at(i);
                fout.close();
            }
        }
        auto end = chrono::steady_clock::now();
        
        // convert time object to actual numbers
        auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);
        double duration_num = duration.count() / pow(10,9);
        
        return make_tuple(duration_num,total_files);
    }

    double sorter_cpp(string directory, bool debug_short, bool debug_full) {
        string filename = "";
        string datename = "";
        string folder_name = "";
        string folder_name_prev = "";
        cout << "Fetching and sorting files...." << endl;
        auto start = chrono::steady_clock::now();
        for (auto const& dir_entry : filesystem::directory_iterator(directory)) {
            // generate folder name
            if (filesystem::is_regular_file(dir_entry)) {
                filename = filename_extractor(dir_entry.path().string());
                datename = filename.substr(0,8); // get a 8 characters long of year-month-day
                folder_name = datename.substr(0,4) + "-" + datename.substr(4,2) + "-" + datename.substr(6,2);
                
                filesystem::path converted_directory = directory;
                filesystem::path converted_folder_name = folder_name;
                filesystem::path converted_folder_name_prev = folder_name_prev;
                filesystem::path converted_filename = filename;

                // move files into folders
                if (folder_name != folder_name_prev) {
                    filesystem::path converted_folder_path_new_1 = directory / converted_folder_name;
                    filesystem::create_directory(converted_folder_path_new_1);
                    filesystem::path converted_folder_path_new_2 = converted_folder_path_new_1 / filename;
                    move_file(dir_entry.path().string(), converted_folder_path_new_2.string());
                    folder_name_prev = folder_name;
                } else {
                    filesystem::path converted_folder_path_old = directory / converted_folder_name_prev / filename;
                    move_file(dir_entry.path().string(), converted_folder_path_old.string());
                }
            }   
        }
        auto end = chrono::steady_clock::now();
        auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);
        double duration_num = duration.count() / pow(10,9);
        return duration_num;
    }

    double remover_cpp(string directory, bool debug_short, bool debug_full) {
        cout << "Fetching and removing files...." << endl;
        auto start = chrono::steady_clock::now();
        for (auto const& dir_entry : filesystem::recursive_directory_iterator(directory)) {
            if (filesystem::is_regular_file(dir_entry)) {
                filesystem::remove(dir_entry);
            }
        }
        for (auto const& dir_entry : filesystem::directory_iterator(directory)) {
            filesystem::remove(dir_entry);
        }
        filesystem::remove(directory);
        auto end = chrono::steady_clock::now();
        auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);
        double duration_num = duration.count() / pow(10,9);
        return duration_num;
    }
}