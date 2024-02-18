function sendData() {

    // Get the value entered by the user
    var inputData = document.getElementById("ticker").value;

    // Prepare the data
    var dataToSend = {
        input_data: inputData
    };

    // Making an AJAX POST request to the server
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/Users/james/Documents/GitHub/dataproj/backend.py", true);
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