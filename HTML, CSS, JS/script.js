// Digital Clock Functionality
function updateClock() { 
    const now = new Date();
    let hours = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();
    const isAm = hours < 12;

    // Format hours for 12-hour clock
    hours = hours % 12 || 12;

    const timeString = `${formatNumber(hours)}:${formatNumber(minutes)}:${formatNumber(seconds)}`;
    const period = isAm ? 'AM' : 'PM';
    const dateString = now.toLocaleDateString(undefined, {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });

    document.getElementById("time").textContent = timeString;
    document.getElementById("period").textContent = period;
    document.getElementById("date").textContent = dateString;
}

function formatNumber(number) {
    return number < 10 ? '0' + number : number;
}

// Update the clock every second
setInterval(updateClock, 1000);
updateClock(); // Initial call to display clock immediately

// Day-Night Toggle Functionality
const themeToggle = document.getElementById("themeToggle");

themeToggle.addEventListener("change", () => {
    if (themeToggle.checked) {
        document.body.classList.add("dark");
        document.body.classList.remove("light");
    } else {
        document.body.classList.add("light");
        document.body.classList.remove("dark");
    }
});

function toggleMenu() {
    const navLinks = document.getElementById('nav-links');
    const hamburger = document.querySelector('.hamburger');
    const bars = document.querySelectorAll('.hamburger .bar');

    navLinks.classList.toggle("active");
    hamburger.classList.toggle("active");

    if (hamburger.classList.contains("active")) {
        // Transform bars to form the "X"
        bars[0].style.transform = "rotate(45deg) translate(7.5px, 7.5px)"; // Adjusted for better visibility
        bars[0].style.backgroundColor = "white"; // Ensure visibility
        bars[1].style.opacity = "0";
        bars[2].style.transform = "rotate(-45deg) translate(7.5px, -7.5px)"; // Adjusted for better visibility
        bars[2].style.backgroundColor = "white"; // Ensure visibility
    } else {
        // Reset bars to their original state
        bars[0].style.transform = "none";
        bars[1].style.opacity = "1";
        bars[2].style.transform = "none";
    }
}


// Toggle dropdown visibility and hide arrow when open
const dropdowns = document.querySelectorAll('.dropdown > a');

dropdowns.forEach(dropdown => {
    dropdown.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default link behavior
        
        const parentDropdown = this.parentElement;
        const arrow = this.querySelector('.arrow');
        const isOpen = parentDropdown.classList.contains('open');
        
        // Close all dropdowns and reset arrows to visible ">"
        document.querySelectorAll('.dropdown').forEach(d => {
            d.classList.remove('open');
            d.querySelector('.arrow').style.visibility = 'visible'; // Ensure the arrow is visible
            d.querySelector('.arrow').textContent = '>'; // Reset arrow to ">"
        });
        
        // If it was not already open, open it and hide the arrow
        if (!isOpen) {
            parentDropdown.classList.add('open');
            arrow.style.visibility = 'hidden'; // Hide arrow when dropdown is open
        }
    });
});
