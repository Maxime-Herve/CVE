const hostname = window.location.hostname;

const searchBar = document.querySelector("#searchBar");
const filterBar = document.querySelector("#filterBar");
const resultBar = document.querySelector("#resultBar");

const vendor = document.querySelector("#vendor");
const product = document.querySelector("#product");
const check = document.querySelector("#check");

const name = document.querySelector("#name");
const criticality = document.querySelector("#criticality");
const date = document.querySelector("#date");
let sortingType = "criticality";

[check, name, criticality, date].forEach(clickable => {
    clickable.addEventListener("click", () => {
    
        if (clickable.id != "check") sortingType = clickable.id;

        fetch(`http://${hostname}:10000/filtering/vendor/${vendor.value}/product/${product.value}/sorting/${sortingType}/`)
            .then(response => response.json())
            .then(data => {
                while (resultBar.firstChild) resultBar.removeChild(resultBar.firstChild);
                

                data.forEach(item => {
                    const row = document.createElement('tr');
                    ['name', 'title', 'criticality', 'date', 'description'].forEach(key => {
                        const cell = document.createElement('td');
                        cell.textContent = item[key];
                        row.appendChild(cell);
                    });
                    resultBar.appendChild(row);
                    });
            })
            .catch(error => console.error('Error fetching data:', error));
    });
});