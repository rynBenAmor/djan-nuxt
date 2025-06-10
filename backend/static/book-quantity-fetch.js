/*****-------------------------------------------------real-time data using fetch api(polling)--------------------- */
document.addEventListener("DOMContentLoaded", () => {
    function checkStock() {
        document.querySelectorAll("[id^='stock-js-']").forEach(stockSpan => {
            let bookId = stockSpan.getAttribute("data-book-id");  // Get book ID
            fetch(`/fetch/ajax/book/quantity/${bookId}/`)  // Dynamic URL
                .then(response => response.json())
                .then(data => {
                    document.getElementById(`stock-js-${bookId}`).innerText = data.quantity;
                    console.log(`*Fetch api* :Updated stock for Book ${bookId}: ${data.quantity}`);
                })
                .catch(error => console.error("Error fetching stock:", error));
        });
    }

    // Poll every second
    setInterval(checkStock, 3000);
});