/*
* 1396. Design Underground System
*/
#include <iostream>
#include <string>
#include <unordered_map>
#include <utility>

using std::string;
using std::unordered_map;
using std::pair;

class UndergroundSystem {
public:
    UndergroundSystem() {}
    
    void checkIn(int id, string stationName, int t) {
        // Store the starting point and time
        checkIns[id] = {stationName, t};
    }
    
    void checkOut(int id, string stationName, int t) {
        pair<string, int> startingPoint = checkIns[id];
        // Use the fullTrip as the key i.e. Paradise->Cambridge
        string fullTrip = startingPoint.first + "->" + stationName;
        // Find how long it took for this trip
        checkOuts[fullTrip].first += t - startingPoint.second;
        checkOuts[fullTrip].second++;
    }
    
    double getAverageTime(string startStation, string endStation) {
        string fullTrip = startStation + "->" + endStation;
        pair<int, int> totalStats = checkOuts[fullTrip];
        return static_cast<double>(totalStats.first / totalStats.second);
    }

private:
    // {id, <stationName, t>}
    unordered_map<int, pair<string, int>> checkIns;
    // {startStation->endStation, <total time, number of travels>}
    unordered_map<string, pair<int, int>> checkOuts;
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */