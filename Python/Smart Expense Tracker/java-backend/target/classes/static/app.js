const API = "/api";
const money = (value) => new Intl.NumberFormat("en-IN", {
  style: "currency", currency: "INR", minimumFractionDigits: 2
}).format(Number(value || 0));

const form = document.querySelector("#transaction-form");
const typeInput = document.querySelector("#type");
const categoryInput = document.querySelector("#category");
const dateInput = document.querySelector("#transaction-date");
const monthInput = document.querySelector("#summary-month");
const message = document.querySelector("#form-message");
const tbody = document.querySelector("#transactions-body");

const today = new Date();
const localDate = `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, "0")}-${String(today.getDate()).padStart(2, "0")}`;
dateInput.value = localDate;
monthInput.value = localDate.slice(0, 7);

function showMessage(text, isError = false) {
  message.textContent = text;
  message.classList.toggle("error", isError);
}

async function request(url, options = {}) {
  const response = await fetch(url, {
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options
  });
  if (!response.ok) {
    let error = `Request failed (${response.status})`;
    try {
      const body = await response.json();
      error = body.error || error;
    } catch (_) { /* response was not JSON */ }
    throw new Error(error);
  }
  if (response.status === 204) return null;
  return response;
}

async function loadSummary() {
  const [year, month] = monthInput.value.split("-").map(Number);
  if (!year || !month) return;
  const response = await request(`${API}/summary?year=${year}&month=${month}`);
  const data = await response.json();
  document.querySelector("#total-income").textContent = money(data.income);
  document.querySelector("#total-expenses").textContent = money(data.expenses);
  document.querySelector("#total-savings").textContent = money(data.savings);
}

async function loadTransactions() {
  const response = await request(`${API}/transactions`);
  const transactions = await response.json();
  tbody.replaceChildren();

  if (transactions.length === 0) {
    const row = tbody.insertRow();
    const cell = row.insertCell();
    cell.colSpan = 4;
    cell.className = "empty-state";
    cell.textContent = "No transactions yet. Add your first entry.";
    return;
  }

  for (const item of transactions) {
    const row = tbody.insertRow();
    const details = row.insertCell();
    const title = document.createElement("span");
    title.className = "transaction-title";
    title.textContent = item.description || item.category;
    const category = document.createElement("span");
    category.className = "transaction-category";
    category.textContent = `${item.category} · ${item.type}`;
    details.append(title, category);

    row.insertCell().textContent = item.transactionDate;
    const amount = row.insertCell();
    amount.className = item.type === "income" ? "amount-income" : "amount-expense";
    amount.textContent = `${item.type === "income" ? "+" : "−"}${money(item.amount)}`;

    const action = row.insertCell();
    const button = document.createElement("button");
    button.type = "button";
    button.className = "delete-button";
    button.textContent = "×";
    button.title = "Delete transaction";
    button.setAttribute("aria-label", `Delete transaction ${item.id}`);
    button.addEventListener("click", async () => {
      if (!window.confirm("Delete this transaction?")) return;
      try {
        await request(`${API}/transactions/${item.id}`, { method: "DELETE" });
        await refresh();
      } catch (error) {
        window.alert(error.message);
      }
    });
    action.append(button);
  }
}

async function refresh() {
  try {
    await Promise.all([loadSummary(), loadTransactions()]);
  } catch (error) {
    showMessage(`Could not load data: ${error.message}`, true);
  }
}

typeInput.addEventListener("change", () => {
  const incomeCategories = ["Salary", "Freelance", "Business", "Investment", "Other"];
  const expenseCategories = ["Food", "Transport", "Shopping", "Bills", "Health", "Education", "Entertainment", "Rent", "Other"];
  const choices = typeInput.value === "income" ? incomeCategories : expenseCategories;
  categoryInput.replaceChildren(...choices.map((value) => {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = value;
    return option;
  }));
});

monthInput.addEventListener("change", refresh);

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  showMessage("");
  const payload = {
    type: typeInput.value,
    amount: Number(document.querySelector("#amount").value),
    category: categoryInput.value.trim(),
    description: document.querySelector("#description").value.trim(),
    transactionDate: dateInput.value
  };

  try {
    await request(`${API}/transactions`, {
      method: "POST",
      body: JSON.stringify(payload)
    });
    form.reset();
    dateInput.value = localDate;
    typeInput.dispatchEvent(new Event("change"));
    showMessage("Transaction added successfully.");
    await refresh();
  } catch (error) {
    showMessage(error.message, true);
  }
});

typeInput.dispatchEvent(new Event("change"));
refresh();
