// Read more button functionality for the index page (index.html) of the website.
document
  .getElementById("readMoreButton")
  .addEventListener("click", function () {
    var firstParagraph = document.getElementById("firstParagraph");
    var secondParagraph = document.getElementById("secondParagraph");

    if (secondParagraph.style.display === "none") {
      secondParagraph.style.display = "block";
      this.innerHTML = '<i class="bi bi-chevron-down"></i>Read Less';
    } else {
      secondParagraph.style.display = "none";
      this.innerHTML = '<i class="bi bi-chevron-right"></i>Read More';
    }
  });
