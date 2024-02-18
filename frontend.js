var statistics = require('simple-statistics');

var vantage = require('alphavantage')

function stockStats(daysAgo, ticker) {
    //Imports
    var endDate = Date.now();
    var startDate = Date.now() - daysAgo;

    var stock = vantage()
}


