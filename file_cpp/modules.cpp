#include <filesystem>
#include <fstream>
#include <iostream>
#include <chrono>
#include <random>
#include <string>
#include <tuple>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include "modules.hpp"
using namespace std;

namespace file_cpp {
    void version() {
        const string lib_version = "1.3.0";
        cout << "Library version: " << lib_version << endl; 
    }
    
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
    /*
    string path_extractor(string basepath) {
        string filename = filename_extractor(basepath);
        string path = basepath - filename;
        return path;
    }
    */

    void copy_file(string path1, string path2) {
        string buffer;
        ifstream old_f(path1);
        ofstream new_f(path2);
        while (!old_f.eof()) {
            old_f >> buffer;
        }
        old_f.close();
        new_f << buffer;
        new_f.close();
    }

    void move_file(string path1, string path2) {
        copy_file(path1, path2);
        //filesystem::remove(path1_1); problematic code somehow
    }

    double copier_cpp(string directory1, string directory2, bool debug_short, bool debug_full) {
        string filename = "";
        filesystem::path converted_directory1 = directory1;
        filesystem::path converted_directory2 = directory2;
        
        auto start = chrono::high_resolution_clock::now();

        cout << "Creating copy folder...." << endl;
        filesystem::create_directories(directory2);

        cout << "Fetching and copying files....." << endl;
        for (auto const& dir_entry : filesystem::directory_iterator(converted_directory1)) {
            filename = filename_extractor(dir_entry.path().string());
            filesystem::path src = converted_directory1 / filename;
            filesystem::path dst = converted_directory2 / filename;
            copy_file(src.string(),dst.string());
        }
        auto end = chrono::high_resolution_clock::now();
        
        auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);
        double duration_num = duration.count() / pow(10,9);
        
        return duration_num;
    }

    tuple<double, unsigned long, vector<string>> generator_cpp(string directory, bool debug_short, bool debug_full, unsigned long dates) {
        vector<string> dates_vec;
        unsigned long total_files = 0;
        vector<string> file_check;
        random_device generator;
        ofstream fout;
        filesystem::path converted_directory = directory;
        
        // create test folder
        cout << "Creating test folder...." << endl;
        filesystem::create_directories(directory);

        // generating dates
        cout << "Creating test files....." << endl;
        auto start = chrono::high_resolution_clock::now();
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
            for (unsigned long j = 0; j < files; j++) {
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

                for (long long unsigned int e = 0; e < file_check.size(); e++) {
                    if (file_check.at(e) == filename) {
                        uniform_int_distribution<unsigned long> more_name_distribution(1,25);
                        unsigned long length = more_name_distribution(generator);
                        filename += random_string(length);
                    }
                }
                filename += ".txt";
                file_check.push_back(filename);
                
                // string -> path
                filesystem::path converted_filename = filename;
                filesystem::path file_dir = converted_directory / converted_filename;

                // write files
                fout.open(file_dir);
                fout << dates_vec.at(i);
                fout.close();
            }
            total_files += files;
        }
        // create test files
        auto end = chrono::high_resolution_clock::now();
        
        // convert time object to actual numbers
        auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);
        double duration_num = duration.count() / pow(10,9);
        return make_tuple(duration_num,total_files,file_check);
    }

    double sorter_cpp(string directory, vector<string> filename_list, bool debug_short, bool debug_full) {
        string datename = "";
        string folder_name = "";
        string folder_name_prev = "";
        vector<string>::iterator filename_iter;
        filesystem::path converted_directory = directory;
        
        cout << "Fetching and sorting files...." << endl;
        auto start = chrono::high_resolution_clock::now();
        
        for (long long unsigned int i = 0; i < filename_list.size(); i++) {
            datename = filename_list.at(i).substr(0,8); // get a 8 characters long of year-month-day
		    folder_name = datename.substr(0,4) + "-" + datename.substr(4,2) + "-" + datename.substr(6,2);
			
            filesystem::path converted_folder_name = folder_name;
            filesystem::path converted_folder_name_prev = folder_name_prev;
            filesystem::path converted_filename = (filename_list.at(i));
            filesystem::path converted_folder_path = converted_directory / converted_filename;

            // move files into folders
            if (folder_name != folder_name_prev) {
                filesystem::path converted_folder_path_new_1 = converted_directory / converted_folder_name;
                filesystem::create_directory(converted_folder_path_new_1);
                filesystem::path converted_folder_path_new_2 = converted_folder_path_new_1 / converted_filename;
                move_file(converted_folder_path.string(), converted_folder_path_new_2.string());
                folder_name_prev = folder_name;
            } else {
                filesystem::path converted_folder_path_old = converted_directory / converted_folder_name_prev / converted_filename;
                move_file(converted_folder_path.string(), converted_folder_path_old.string());
            }
        }
        auto end = chrono::high_resolution_clock::now();
        
        auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);
        double duration_num = duration.count() / pow(10,9);
        return duration_num;
    }

    double remover_cpp(string directory, bool debug_short, bool debug_full) {
        cout << "Fetching and removing files...." << endl;
        auto start = chrono::high_resolution_clock::now();
        for (auto const& dir_entry : filesystem::recursive_directory_iterator(directory)) {
            if (filesystem::is_regular_file(dir_entry)) {
                filesystem::remove(dir_entry);
            }
        }
        for (auto const& dir_entry : filesystem::directory_iterator(directory)) {
            filesystem::remove(dir_entry);
        }
        filesystem::remove(directory);
        auto end = chrono::high_resolution_clock::now();
        
        auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);
        double duration_num = duration.count() / pow(10,9);
        
        return duration_num;
    }
}
