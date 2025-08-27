const API_URL = "http://localhost:5000/alfajores";

// detectar si es admin (?admin=true en la URL)
const urlParams = new URLSearchParams(window.location.search);
const isAdmin = urlParams.get("admin") === "true";

async function fetchAlfajores() {
  const res = await fetch(API_URL);
  const data = await res.json();
  renderAlfajores(data);
}

async function votar(id) {
  await fetch(`${API_URL}/${id}/votar`, { method: "POST" });
  fetchAlfajores();
}

async function borrar(id) {
  if (!isAdmin) return alert("Solo el administrador puede borrar");
  await fetch(`${API_URL}/${id}`, {
    method: "DELETE",
    headers: { "X-Admin": "true" }
  });
  fetchAlfajores();
}

function renderAlfajores(alfajores) {
  const tbody = document.querySelector("#tabla-alfajores tbody");
  tbody.innerHTML = "";

  alfajores.forEach((a) => {
    const row = document.createElement("tr");

    row.innerHTML = `
      <td><img src="${a.imagen}" alt="${a.nombre}" width="80" height="80"></td>
      <td>${a.nombre}</td>
      <td>${a.tipo || "-"}</td>
      <td>${a.descripcion}</td>
      <td>${a.votos}</td>
      <td>
        <button onclick="votar(${a.id})">Votar</button>
        ${isAdmin ? `<button onclick="borrar(${a.id})">Borrar</button>` : ""}
      </td>
    `;

    tbody.appendChild(row);
  });
}


// inicializar
fetchAlfajores();
