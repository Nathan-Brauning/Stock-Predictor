var statistics = require('simple-statistics');
var vantage = require('alphavantage')

var shouldInvest = true;

async function fetchData(symbol, start_date, end_date) {
    const apiKey = "59ZBUCT8RM3A1WZW";
    const url = `https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=${symbol}&apikey=${apiKey}&start_date=${start_date}&end_date=${end_date}`;
    console.log(url);

    try{
        const response = await fetch(url);
        const data = await response.json();

        console.log(data);
        return data;
    } catch (error) {
        console.error('Error fetching data: ', error);
    }
}

function parseData(data) {
    const dates = Object.keys(data['Time Series (Daily)']).reverse();
    const prices = dates.map(date => data['Time Series Daily)'][date]['4. close']);
    return {dates, prices}
}

// Function to create chart using Chart.js
function createChart(labels, data) {

    var shouldInvest = false;

    var color = null;
    if (shouldInvest) {
        color = rgba(0, 204, 0)
    } else {
        color = rgba(204, 0, 0)
    }

    const ctx = document.getElementById('graph').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Stock Price',
                data: data,
                borderColor: color,
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    type: 'time',
                    time: {
                        unit: 'day'
                    }
                }],
                yAxis: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'Price (USD)'
                    }
                }]
            }
        }
    });
}

async function main() {
    const symbol = 'APPL';

    var days = 14;

    const currentDate = new Date();
    const timeElapsed = currentDate.getTime() - (days * 24 * 60 * 60 * 1000);
    const twoWeeksBefore = new Date(timeElapsed);

    const data = await fetchData(symbol, twoWeeksBefore, currentDate);
    const parsedData = parseData(data);
    createChart(parsedData.dates, parsedData.prices)
}

main()

