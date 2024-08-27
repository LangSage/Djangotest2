// myapp/static/myapp/live_search.js

document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("searchInput");
    const resultsDiv = document.getElementById("searchResults");

    searchInput.addEventListener("keyup", function() {
        const query = searchInput.value;

        if (query.length > 2) {
            fetch(`/live_search/?q=${encodeURIComponent(query)}`)
                .then(response => response.text())
                .then(html => {
                    resultsDiv.innerHTML = html;
                });
        } else {
            resultsDiv.innerHTML = "";  // Clear results if query is too short
        }
    });
});
