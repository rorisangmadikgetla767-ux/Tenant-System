document.addEventListener("DOMContentLoaded", () => {
    const paymentForm = document.querySelector("#payment-panel form");
    
    if (paymentForm) {

    
    paymentForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const amount = document.getElementById("amount").value;
        const toAccount = document.getElementById("account").value;
        const reference = document.getElementById("ref").value;

        if (!amount || !reference) {
            alert("Please fill in amount and reference.");
            return;

        }

        try {
            const response = await fetch("http://127.0.0.1:8000/api/payments", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({
                    amount: parseFloat(amount),
                    to_account: toAccount,
                    reference: reference
                })
            });

            if (!response.ok) {
                throw new Error("Payment failed to save!")
            }

            const savedPayment = await response.json();
            console.log("Saved payment", savedPayment);
            alert("Tjhelete e bolokehile ka katleho.  Payment has been saved successfully");
            paymentForm.reset();

        } catch (error) {
            console.error(error);
            alert("Ho nale phoso ka tjhelete ea hao, warning there is something wrong with your payment!!");
        }
    });
}
    loadPayments(); // load the table once when the page 1st opens
});

async function loadPayments() {
    const response = await fetch("http://127.0.0.1:8000/api/payments");
    const payments = await response.json();

    
    const tbody = document.getElementById("payments-table-body");
    tbody.innerHTML = ""; // clear old rows first

    payments.forEach(payment => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>R${payment.amount.toFixed(2)}</td>
            <td>${payment.to_account}</td>
            <td>${payment.reference}</td>
            <td>${new Date(payment.created_at).toLocaleDateString()}</td>

        `;
        tbody.appendChild(row)
            
    })
}
