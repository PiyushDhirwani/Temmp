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



    // Suface tension
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

    int Nv=local_maxima[0].first, Nmin=local_minima[0].first, Nl=local_maxima[1].first, boxlenght=10;

    double Surfacetension =(0.5*(local_maxima[0].second+local_maxima[1].second)-local_minima[0].second)/(2*boxlenght*boxlenght);

    cout<<"surface tension: "<<Surfacetension<<endl;
    // Density


    double rohv=0, rohl=0, lnpiavg=0;
    for (int i = 0; i < dataMap["y0"].size(); i++){
        double lnpi=exp(stod(dataMap["y0"][i]));
        if (i<=Nmin){
            rohv+=(i*lnpi);
        }
        else{
            rohl+=(i*lnpi);
        }
        lnpiavg+=lnpi;
    }

    rohv/=lnpiavg;
    rohl/=lnpiavg;
    cout<<"rohv: "<<rohv<<endl;
    cout<<"rohl: "<<rohl<<endl;


    // Density with area
    // double rohv_area=0, rohl_area=0;
    // for (size_t i = 1; i < dataMap["y0"].size(); ++i) {
    //     double deltaX = stod(dataMap["x"][i]) - stod(dataMap["x"][i-1]);
    //     double avgY = (stod(dataMap["y0"][i]) + stod(dataMap["y0"][i-1])) / 2.0;
    //     if (i<=Nmin){
    //         rohv_area += (deltaX * avgY);
    //     }
    //     else{
    //         rohl_area += (deltaX * avgY);
    //     }
    // }

    // cout<<"rohv_area: "<<rohv_area<<endl;
    // cout<<"rohl_area: "<<rohl_area<<endl;
    // Weighted Density

    double rohv_=0, rohl_=0;
    for (int i = 0; i < dataMap["y0"].size(); i++){
        double lnpi=exp(stod(dataMap["y0"][i]));
        if (i<=Nmin){
            rohv_+=(i*i*lnpi);
        }
        else{
            rohl_+=(i*i*lnpi);
        }
    }

    rohv_-=(rohv*rohv);
    rohl_-=(rohl*rohl);

    cout<<"rohv_: "<<rohv_<<endl;
    cout<<"rohl_: "<<rohl_<<endl;




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
