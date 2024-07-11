function updateCities() {
    const selectedCountryId = document.getElementById("country").value;
    const citiesDropdown = document.getElementById("city");

    citiesDropdown.innerHTML = "<option value='0' selected disabled>Select City</option>";
    const citiesData = JSON.parse(document.getElementById("city").getAttribute("data-cities"));

    citiesData.forEach(city => {
        if (city.country_id == selectedCountryId) {
            const option = document.createElement("option");
            option.value = city.id;
            option.text = city.name;
            citiesDropdown.add(option);
        }
    });
}

function confirmDelete() {
    const ok = confirm("Are you sure you want to delete this employee?")
    if(!ok) event.preventDefault();
}