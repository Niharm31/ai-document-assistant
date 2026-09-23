const docs = document.querySelector("#documents");
const scopeSelect = document.querySelector("#scopeSelect");
const messages = document.querySelector("#messages");
const sessionId = crypto.randomUUID();
let selectedDocument = null;

document.querySelector("#sessionLabel").textContent =
  `Conversation: ${sessionId.slice(0, 8)}`;

function addMessage(text, role, sources = []) {
  const el = document.createElement("div");
  el.className = `message ${role}`;
  const content = document.createElement("div");
  content.textContent = text || "No answer was returned.";
  el.appendChild(content);

  if (sources.length) {
    const sourceBox = document.createElement("div");
    sourceBox.className = "sources";
    sourceBox.textContent = "Sources: " + sources.map(
      s => `${s.document} — page ${s.page} — score ${s.score}`
    ).join(" • ");
    el.appendChild(sourceBox);
  }

  messages.appendChild(el);
  messages.scrollTop = messages.scrollHeight;
  return el;
}

async function loadDocuments() {
  const response = await fetch("/api/documents");
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const data = await response.json();

  docs.innerHTML = "";
  scopeSelect.innerHTML = '<option value="">All documents</option>';

  data.forEach(doc => {
    const option = document.createElement("option");
    option.value = doc.id;
    option.textContent = doc.filename;
    scopeSelect.appendChild(option);

    const el = document.createElement("div");
    el.className = "doc" + (selectedDocument === doc.id ? " selected" : "");

    const title = document.createElement("strong");
    title.textContent = doc.filename;

    const info = document.createElement("small");
    info.textContent = `${doc.page_count} pages · ${doc.chunk_count} chunks · ${doc.status}`;

    const del = document.createElement("button");
    del.className = "delete";
    del.textContent = "Delete";
    del.onclick = async (event) => {
      event.stopPropagation();
      if (!confirm(`Delete ${doc.filename}? This also removes its vectors.`)) return;
      const response = await fetch(`/api/documents/${doc.id}`, { method: "DELETE" });
      if (!response.ok) {
        addMessage("Could not delete the document.", "assistant");
        return;
      }
      if (selectedDocument === doc.id) selectedDocument = null;
      await loadDocuments();
    };

    el.append(title, document.createElement("br"), info, del);
    el.onclick = () => {
      selectedDocument = doc.id;
      scopeSelect.value = doc.id;
      loadDocuments();
    };
    docs.appendChild(el);
  });
}

scopeSelect.addEventListener("change", () => {
  selectedDocument = scopeSelect.value || null;
  loadDocuments();
});

document.querySelector("#refresh").onclick = () => loadDocuments();

document.querySelector("#uploadForm").addEventListener("submit", async event => {
  event.preventDefault();
  const file = document.querySelector("#file").files[0];
  if (!file) return;

  const formData = new FormData();
  formData.append("file", file);

  const button = document.querySelector("#uploadForm button");
  button.disabled = true;
  button.textContent = "Processing...";

  try {
    const response = await fetch("/api/documents/upload", {
      method: "POST",
      body: formData
    });
    const raw = await response.text();
    const data = JSON.parse(raw);
    if (!response.ok) throw new Error(data.detail || "Upload failed.");

    selectedDocument = data.id;
    scopeSelect.value = data.id;
    addMessage(`Indexed ${data.filename} successfully.`, "assistant");
    await loadDocuments();
  } catch (error) {
    addMessage(`Upload failed: ${error.message}`, "assistant");
  } finally {
    button.disabled = false;
    button.textContent = "Upload PDF";
  }
});

document.querySelector("#chatForm").addEventListener("submit", async event => {
  event.preventDefault();

  const input = document.querySelector("#question");
  const question = input.value.trim();
  if (!question) return;
  input.value = "";

  addMessage(question, "user");
  const thinking = addMessage("Searching the document...", "assistant");

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        question,
        document_id: selectedDocument,
        session_id: sessionId
      })
    });

    const raw = await response.text();
    const data = JSON.parse(raw);
    if (!response.ok) throw new Error(data.detail || `HTTP ${response.status}`);

    thinking.remove();
    addMessage(data.answer, "assistant", data.sources || []);
  } catch (error) {
    thinking.remove();
    addMessage(`Error: ${error.message}`, "assistant");
  }
});

document.querySelector("#clearHistory").onclick = async () => {
  await fetch(`/api/chat/${sessionId}/history`, { method: "DELETE" });
  messages.innerHTML = "";
  addMessage("Conversation cleared.", "assistant");
};

async function checkHealth() {
  try {
    const response = await fetch("/health");
    document.querySelector("#health").textContent = response.ok ? "Online" : "Offline";
  } catch {
    document.querySelector("#health").textContent = "Offline";
  }
}

loadDocuments().catch(console.error);
checkHealth();
