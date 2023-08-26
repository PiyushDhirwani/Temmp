#include <bits/stdc++.h>
using namespace std;

int main() {
    // Open the input CSV file
    ifstream input("output.csv");
    if (!input.is_open()) {
        cerr << "Failed to open input file." << endl;
        return 1;
    }

    map<string, vector<string> > dataMap; // Store values as strings

    string headerLine;
    if (getline(input, headerLine)) {
        istringstream headerStream(headerLine);
        string column;
        getline(headerStream, column, ','); // Skip the first column
        dataMap["x"].push_back(column);     // Initialize 'x'
        int columnIndex = 0;
        while (getline(headerStream, column, ',')) {
            dataMap["y" + to_string(columnIndex)].push_back(column); // Initialize 'y0', 'y1', 'y2', ...
            columnIndex++;
        }
    }

    string line;
    while (getline(input, line)) {
        istringstream lineStream(line);
        string cell;
        getline(lineStream, cell, ','); // Read the first column ('x')
        dataMap["x"].push_back(cell);
        int columnIndex = 0;
        while (getline(lineStream, cell, ',')) {
            dataMap["y" + to_string(columnIndex)].push_back(cell);
            columnIndex++;
        }
    }


    vector<pair<double, double> > local_maxima;
    vector<pair<double, double> > local_minima;

    for (int i = 1; i < dataMap["y0"].size() - 1; i++) {
        if (stod(dataMap["y0"][i]) > stod(dataMap["y0"][i - 1]) && stod(dataMap["y0"][i]) > stod(dataMap["y0"][i + 1])) {
            local_maxima.push_back(make_pair(stod(dataMap["x"][i]), stod(dataMap["y0"][i])));
        }
        if (stod(dataMap["y0"][i]) < stod(dataMap["y0"][i - 1]) && stod(dataMap["y0"][i]) < stod(dataMap["y0"][i + 1])) {
            local_minima.push_back(make_pair(stod(dataMap["x"][i]), stod(dataMap["y0"][i])));
        }
    }

    for (int i = 0; i < local_maxima.size(); i++) {
        cout << local_maxima[i].first << " " << local_maxima[i].second << endl;
    }
    cout<<"cccccc"<<endl;

    for (int i = 0; i < local_minima.size(); i++) {
        cout << local_minima[i].first << " " << local_minima[i].second << endl;
    }
    // Print the map content
    for (const auto &entry : dataMap) {
        cout << "Column: " << entry.first << ", Values: ";
        for (const string &value : entry.second) {
            cout << value << " ";
        }
        cout << endl;
    }

    // Close the input file
    input.close();

    return 0;
}
