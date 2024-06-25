// scripts.js

function browseTerms(letter) {
    // Logic to filter terms by selected letter and update word list
    // You may use AJAX to fetch and update the word list dynamically
    alert('Browse terms starting with: ' + letter);
}

function searchTerms() {
    // Logic to filter terms by search input and update word list
    // You may use AJAX to fetch and update the word list dynamically
    let searchQuery = document.getElementById('search').value;
    alert('Search for: ' + searchQuery);
}
