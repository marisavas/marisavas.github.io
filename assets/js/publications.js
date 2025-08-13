document.addEventListener("DOMContentLoaded", function() {

    const itemsPerPage = 4;

    // Mapeia listId para a classe singular usada no CSS
    const typeClassMap = {
      conferences: "conference",
      journals: "journal",
      patents: "patent"
  };

    function initPagination(listId, dataId) {
        const listElement = document.getElementById(`${listId}-list`);
        const data = JSON.parse(document.getElementById(`${dataId}-data`).textContent);
        let currentPage = 0;

        const nextButton = document.getElementById(`${listId}-next`);
        const prevButton = document.getElementById(`${listId}-prev`);

        // Evento Next
        nextButton.addEventListener("click", () => {
            currentPage++;
            if (currentPage * itemsPerPage >= data.length) {
                currentPage = 0; // volta para primeira página se passar do limite
            }
            renderPage();
        });

        // Evento Previous
        prevButton.addEventListener("click", () => {
            currentPage--;
            if (currentPage < 0) currentPage = 0;
            renderPage();
        });

        function renderPage() {
            listElement.innerHTML = "";
            const start = currentPage * itemsPerPage;
            const end = start + itemsPerPage;
            const pageItems = data.slice(start, end);

            pageItems.forEach(item => {
                const li = document.createElement("li");
                // li.classList.add("publication-item", listId); // adiciona classe para ícone
                li.classList.add("publication-item", typeClassMap[listId]);

                const authors = item.authors.filter(a => a.trim() !== "");
                const authorsHTML = authors.map(a => 
                    a === "Marisa Vasconcelos" ? `<strong>${a}</strong>` : a
                ).join(", ");

                const venue = item.venue || item.note || "";
                li.innerHTML = `${item.url ? `<a href="${item.url}" target="_blank">${item.title}</a>` : item.title}. ${authorsHTML}. <em>${venue}</em> (${item.year || ""})`;


                listElement.appendChild(li);
            });

            // botão Next sempre azul
            nextButton.classList.add("enabled");
            nextButton.disabled = false;

            // Mostrar ou esconder botão Previous
            if (currentPage === 0) {
                prevButton.style.display = "none";
            } else {
                prevButton.style.display = "inline-block";
            }
        }

        renderPage();
    }

    initPagination("conferences", "conferences");
    initPagination("journals", "journals");
    initPagination("patents", "patents");
});
