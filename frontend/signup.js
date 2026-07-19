document.addEventListener("DOMContentLoaded", () =>  {
    const signupForm = document.getElementById("signup-form");

    signupForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const full_name = document.getElementById("full_name").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;
        const phone_number = document.getElementById("phone_number").value;
        const house_number = document.getElementById("house_number").value;
        const lease_start = document.getElementById("lease_start").value;
        const lease_end = document.getElementById("lease_end").value;
        const monthly_rent = document.getElementById("monthly_rent").value;

        try {
            const response = await fetch("http://127.0.0.1:8000/tenants", {
                method: "POST",
                headers: {"Content-Type": "application/json" },
                body: JSON.stringify({
                    full_name: full_name,
                    email:email,
                    password: password,
                    phone_number: phone_number,
                    house_number: house_number,
                    lease_start : lease_start,
                    lease_end : lease_end,
                    monthly_rent: parseFloat(monthly_rent)
                })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || "Registration failed");

            }

            const newTenant = await response.json();
            console.log("Registered tenant:", newTenant);
            alert("Ngodiso e atlehile! Registration is successful, you may log in.")
            signupForm.reset();


        }  catch (error) {
            console.error(error);
            alert("Ho nale phoso" + error.message);
        }
    });
});