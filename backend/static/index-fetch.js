/************************
 js for index page only as it may cause a property of null error
 * 
 */



/**--------------------------Public record example-------------- */
document.addEventListener('DOMContentLoaded', () => {


    const prId = document.getElementById('PR-button').dataset.prid;// Get the prId from the button's data attribute

    // Function to fetch public record data
    function fetchPR() {
        // Construct the URL with the prId parameter
        const url = `/fetch/get-public-record/?prid=${prId}`;

        // Options for the fetch request
        const options = {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',   // Sending data as JSON
                'Accept': 'application/json',         // Accepting JSON in response
            },
            mode: 'same-origin',  // Ensures it works with same-origin policy
        };

        // Make the fetch request
        fetch(url, options)
            .then(response => response.json())  // Convert the response to JSON
            .then(data => {
                // Check if there's an error in the response
                if (data.error) {
                    document.getElementById('PR-container').innerHTML = `Error: ${data.error}`;
                } else {
                    // Format the citizen data into HTML and display it
                    const citizenInfo = `
                        <p><strong>Name:</strong> ${data.first_name} ${data.last_name}</p>
                        <p><strong>SSN:</strong> ${data.ssn}</p>
                        <p><strong>Date of Birth:</strong> ${data.date_of_birth}</p>
                    `;
                    document.getElementById('PR-container').innerHTML = citizenInfo;
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);  // Log any fetch errors
            });
    }

    // Call fetchPR when the form is submitted
    document.getElementById('PR-form').addEventListener('submit', function (event) {
        event.preventDefault();  // Prevent the form from actually submitting
        fetchPR();  // Call the fetchPR function
    });


    /*----------------------quote example--------------------------------------------*/
    function fetchQuote() {
        fetch('/fetch/random-quote/', {
            headers: { 'Accept': 'text/html' }
        })
            .then(response => response.text())
            .then(html => {
                document.getElementById("quote-container").innerHTML = html;
            })
            .catch(error => console.error('Error fetching quote:', error));
    }

    //bind the reference of the function to the button
    document.getElementById('quote-button').addEventListener('click', fetchQuote);



    /*------------------------------fake weather example--------------------------------------------*/
    document.getElementById("weather-form").addEventListener("submit", function (event) {
        event.preventDefault();  // Prevent page reload

        const city = document.getElementById("city-input").value;
        fetch(`/fetch/get-weather/?city=${encodeURIComponent(city)}`, {
            headers: { 'Accept': 'text/html' }
        })
            .then(response => response.text())
            .then(html => {
                document.getElementById("weather-container").innerHTML = html;
            })
            .catch(error => console.error('Error fetching weather:', error));
    });



    /*----------------------------- Time Zone Fetch Example*--------------------------*/
    document.getElementById("time-form").addEventListener("submit", function (event) {
        event.preventDefault();

        const city = document.getElementById("time-city-input").value;
        fetch(`/fetch/get-time/?city=${encodeURIComponent(city)}`, {
            headers: { 'Accept': 'text/html' }
        })
            .then(response => response.text())
            .then(html => {
                document.getElementById("time-container").innerHTML = html;
            })
            .catch(error => console.error('Error fetching time:', error));
    });



});



/***----------------------------------POST REQUEST fetch with csrf-------------------------- */
const formEl = document.getElementById('id_form_795');
formEl.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the input value
    const input_data = document.getElementById('id_input_795').value;
    const titleEl = document.getElementById('id_title_795');
    const url = "/fetch/add-something/";
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Prepare the request body
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        mode: 'same-origin',
        body: JSON.stringify({ input_data }),  // Send the input data as JSON
    };

    // Make the fetch request
    fetch(url, options)
        .then((response) => response.json())  // Parse JSON response
        .then((data) => {
            titleEl.style.display = 'block';  // Show the response title
            formEl.style.display = 'none';    // Hide the form
            titleEl.textContent = data.message;  // Display the message returned from Django
        })
        .catch((error) => console.error('Error:', error));  // Catch and log any errors
});


/**---------------------------------------------------- Same POST  request with jquery--------------------------*/
$(document).ready(function () {
    $('#id_form_254').on('submit', function (e) {
        e.preventDefault();

        // Get the input value
        var input_data = $('#id_input_254').val();
        var titleEl = $('#id_title_254');
        var url = "/fetch/add-something/";
        var csrfToken = $('[name=csrfmiddlewaretoken]').val();

        // Prepare the request body
        var options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({ input_data })  // Send the input data as JSON
        };

        // Make the AJAX request
        $.ajax({
            url: url,
            type: 'POST',
            headers: options.headers,
            contentType: 'application/json',
            dataType: 'json',
            data: options.body,
            success: function (data) {
                titleEl.show();  // Show the response title
                $('#id_form_254').hide();  // Hide the form
                titleEl.text(data.message);  // Display the message returned from Django
            },
            error: function (error) {
                console.error('Error:', error);  // Catch and log any errors
            }
        });
    });
});



