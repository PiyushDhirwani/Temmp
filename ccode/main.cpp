#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

int main() {
    // Open the input .dat file
    std::ifstream input("gnn.dat");
    if (!input.is_open()) {
        std::cerr << "Failed to open input file." << std::endl;
        return 1;
    }

    // Open the output CSV file
    std::ofstream output("output.csv");
    if (!output.is_open()) {
        std::cerr << "Failed to open output file." << std::endl;
        return 1;
    }

    std::string line;
    while (std::getline(input, line)) {
        std::istringstream iss(line);
        std::vector<std::string> tokens;

        std::string token;
        while (iss >> token) {
            tokens.push_back(token);
        }

        // Write CSV row
        for (size_t i = 0; i < tokens.size(); ++i) {
            output << tokens[i];
            if (i != tokens.size() - 1) {
                output << ",";
            }
        }
        output << std::endl;
    }

    // Close the files
    input.close();
    output.close();

    std::cout << "Conversion complete." << std::endl;

    return 0;
}
