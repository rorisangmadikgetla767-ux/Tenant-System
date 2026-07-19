// Hardcoded list of locations - I am going to replace with backend later
const locations = [
    "Rocklands,Mokgami street 4928",
    "Bloemside 2 Z street 4928"
];

const searchInput = document.getElementById('location-search')
const suggestionsBox = document.getElementById('search-suggestions');

searchInput.addEventListener('input', () => {
    const query = searchInput.value.trim().toLowerCase()
    suggestionsBox.innerHTML = '';

    if (query === '') {
        suggestionsBox.style.display = 'none';
        return;
    }
    const matches = locations.filter(loc => loc.toLowerCase().includes(query));

    matches.forEach(match => {
        const item = document.createElement('div');
        item.textContent = match
        item.addEventListener('click', () => {
            searchInput.value = match;
            suggestionsBox.style.display = 'none';
        });

        
        suggestionsBox.appendChild(item);

    });
    suggestionsBox.style.display = 'block';

});

// Hide the suggestion when clicking outside
document.addEventListener('click', (e) => {
    if (!searchInput.contains(e.target) && !suggestionsBox.contains(e.target)) {
        suggestionsBox.style.display = 'none';
    }
});
