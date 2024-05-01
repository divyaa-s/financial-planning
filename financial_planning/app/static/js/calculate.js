// Function to display financial summary
function displayFinancialSummary() {
    // Define the path to the CSV file
    const csvFilename = "financial_data.csv";

    // Create an instance of XMLHttpRequest
    const xhr = new XMLHttpRequest();

    // Load the CSV file
    xhr.open("GET", csvFilename, true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            // Parse CSV data
            const csvData = xhr.responseText;
            const rows = csvData.split('\n');
            const headers = rows[0].split(',');

            // Initialize variables
            let totalSpent = 0;
            let income = null;

            // Process each row
            for (let i = 1; i < rows.length; i++) {
                const row = rows[i];
                if (row.trim()) {
                    const columns = row.split(',');

                    // Get the income from the first row
                    if (income === null) {
                        income = parseFloat(columns[headers.indexOf('Income')]);
                    }

                    // Calculate the total spent
                    const dailyExpenses = parseFloat(columns[headers.indexOf('Daily Expenses')]);
                    totalSpent += dailyExpenses;
                }
            }

            // Calculate the available balance
            const availableBalance = income - totalSpent;

            // Display the total amount spent and available balance
            document.getElementById("total_spent").innerText = totalSpent.toFixed(2);
            document.getElementById("available_balance").innerText = availableBalance.toFixed(2);
        }
    };

    // Send the request
    xhr.send();
}

// Call the function to display financial summary on page load
window.onload = displayFinancialSummary;

