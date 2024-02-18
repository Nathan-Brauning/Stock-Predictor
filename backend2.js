function sendData() {

    // Get the value entered by the user
    var inputData = document.getElementById("ticker").value;

    // Prepare the data
    var dataToSend = {
        input_data: inputData
    };

    // Making an AJAX POST request to the server
    var xhr = new XMLHttpRequest();
    xhr.open('POST', "/backend/", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status == 200) {
                console.log("Data send successfully");
            } else {
                console.error("Error: ", xhr.statusText);
            }
        }
    };
    xhr.send(JSON.stringify(dataToSend));
}

function fetchData() {
    fetch('/backend/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok')
        }
        return response.json();
    })
    .then(data => {

        // Use the data received from the server
        console.log(data);

        var stats = data;
        document.getElementId('receivedData').textContent = stats;
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}