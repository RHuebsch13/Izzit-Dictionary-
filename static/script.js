document.addEventListener('DOMContentLoaded', function() {
    const browseIcon = document.getElementById('browse-icon');
    const dropdownMenu = document.querySelector('.dropdown-menu');

    // Toggle dropdown on click
    browseIcon.addEventListener('click', function(event) {
        event.preventDefault();
        dropdownMenu.style.display = dropdownMenu.style.display === 'flex' ? 'none' : 'flex'; // Toggle visibility
    });

    // Close dropdown when clicking outside
    window.addEventListener('click', function(event) {
        if (!browseIcon.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.style.display = 'none'; // Hide dropdown
        }
    });
});







