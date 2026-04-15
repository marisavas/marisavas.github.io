document.addEventListener("DOMContentLoaded", () => {
  const sections = [
    { id: "conferences", page: 1 },
    { id: "journals", page: 1 },
    { id: "patents", page: 1 }
  ];

  const ITEMS_PER_PAGE = 4;

  sections.forEach(section => {
    const listElement = document.getElementById(`${section.id}-list`);
    const dataElement = document.getElementById(`${section.id}-data`);
    const prevBtn = document.getElementById(`${section.id}-prev`);
    const nextBtn = document.getElementById(`${section.id}-next`);

    if (!listElement || !dataElement) return;

    const data = JSON.parse(dataElement.textContent) || [];

    const renderPage = () => {
      listElement.innerHTML = "";

      const start = (section.page - 1) * ITEMS_PER_PAGE;
      const end = start + ITEMS_PER_PAGE;
      const pageItems = data.slice(start, end);

      pageItems.forEach(item => {
        const li = document.createElement("li");
        li.innerHTML = formatPublication(item);
        listElement.appendChild(li);
      });

      // Controle de botões
      prevBtn.style.display = section.page > 1 ? "inline-block" : "none";
      nextBtn.style.display = end < data.length ? "inline-block" : "none";
    };

    // Eventos de paginação
    prevBtn.addEventListener("click", () => {
      if (section.page > 1) {
        section.page--;
        renderPage();
      }
    });

    nextBtn.addEventListener("click", () => {
      if ((section.page * ITEMS_PER_PAGE) < data.length) {
        section.page++;
        renderPage();
      }
    });

    // Primeira renderização
    renderPage();
  });

  function formatPublication(pub) {
    // Ajusta conforme sua estrutura de dados
    if (typeof pub === "string") return pub;
    if (pub.title && pub.year) return `<strong>${pub.title}</strong> (${pub.year})`;
    return JSON.stringify(pub);
  }
});
