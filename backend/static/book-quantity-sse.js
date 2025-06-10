
/*--------------------------Real-time data using sse (GET requests only)-----------------------*/
document.querySelectorAll("[id^='stock-sse-']").forEach(stockSpan => {
    let bookId = stockSpan.getAttribute("data-book-id");

    // Create SSE connection to Django endpoint
    const eventSource = new EventSource(`/fetch/ajax/book/stock-stream/${bookId}/`);

    eventSource.onmessage = function(event) {
        document.getElementById(`stock-sse-${bookId}`).innerText = event.data;
        console.log(`*SSE* Updated stock for Book ${bookId}: ${event.data}`);
    };

    eventSource.onerror = function() {
        console.error("SSE connection failed.");
        eventSource.close(); // Stop retrying on failure
    };
});