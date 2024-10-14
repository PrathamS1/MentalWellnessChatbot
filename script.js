function showDescription(id) {
    var cards = document.getElementsByClassName("card");

    // Hide all cards
    for (var i = 0; i < cards.length; i++) {
        cards[i].classList.remove("show");
    }

    // Show the selected card
    var selectedCard = document.getElementById("description" + id);
    selectedCard.classList.add("show");
}

function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    section.scrollIntoView({ behavior: 'smooth' });
}
