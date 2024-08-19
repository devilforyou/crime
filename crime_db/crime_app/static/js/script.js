// Add any JavaScript functionality you need here 
// Example: Add a search icon next to the search box
const searchIcon = document.createElement("i");
searchIcon.classList.add("fas", "fa-search");
const searchInput = document.querySelector(".search-form input[type='text']");
searchInput.parentNode.insertBefore(searchIcon, searchInput.nextSibling);