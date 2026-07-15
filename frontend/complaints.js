document.addEventListener("DOMContentLoaded", () => {
    const complaintForm = document.getElementById("complaint-form");

    complaintForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const tenant_id = document.getElementById("tenant_id").value;
        const category = document.getElementById("category").value;
        const description = document.getElementById("description").value;

        if (!tenant_id || !category || !description) {
            alert("Please fill all fields to proceed. ");
            return;

        }

        try {
            const response = await fetch("http://127.0.0.1:8000/complaints", {
                method: "POST",
                headers: {"Content-Type": "application/json" },
                body: JSON.stringify({
                    tenant_id: parseInt(tenant_id),
                    category: category,
                    description: description
                })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || "Failed to submit a complaint");

            }

            const newComplaint = await response.json();
            alert("Complaint submitted successfully! We will contact you soon!")
            complaintForm.reset();

        } catch (error) {
            console.error(error);
            alert("Alert! Ho nale phoso" + error.message);
        }
    });
});