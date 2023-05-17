function showDescription(id) {
    var descriptions = document.getElementsByClassName("description-text");

    // Hide all descriptions
    for (var i = 0; i < descriptions.length; i++) {
        descriptions[i].style.display = "none";
    }

    // Show the selected description with fade animation
    var selectedDescription = document.getElementById("description" + id);
    selectedDescription.style.display = "block";
    selectedDescription.classList.add("fade-in");

    // Remove fade animation after it completes
    setTimeout(function() {
        selectedDescription.classList.remove("fade-in");
    }, 900);
}
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    section.scrollIntoView({ behavior: 'smooth' });
}