// Read more button functionality for the index page of the website.
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

// Create a script element for the Mapbox GL JS script
mapboxgl.accessToken =
  "pk.eyJ1IjoibGFieWtyZWF0aXZlIiwiYSI6ImNsOHUxa3JpYzBjd3Ezdm1kd3l4eHo2ZXcifQ.g5sskeC-FvlEFsZErNtIpA";
var map = new mapboxgl.Map({
  container: "map",
  style: "mapbox://styles/mapbox/streets-v11",
  center: [6.509779, 3.387539],
  zoom: 4,
});
