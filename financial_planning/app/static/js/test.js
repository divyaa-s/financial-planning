// Function to display the donut chart based on the data from the CSV file
function displayDonutChart() {
    const ctx = document.getElementById('spendingChart').getContext('2d');
    
    // Load the data from the CSV file
    fetch('financial_data.csv')
        .then(response => response.text())
        .then(data => {
            const rows = data.split('\n');
            let income = 0;
            let totalSpent = 0;

            // Parse the CSV data
            rows.forEach((row, index) => {
                if (index > 0 && row) {
                    const cols = row.split(',');
                    income = parseFloat(cols[1]);
                    totalSpent += parseFloat(cols[7]);
                }
            });

            // Calculate the available balance
            const availableBalance = income - totalSpent;

            // Create the donut chart
            new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Spent Money', 'Available Balance'],
                    datasets: [{
                        data: [totalSpent, availableBalance],
                        backgroundColor: ['#ff6384', '#36a2eb'],
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    legend: {
                        display: true
                    }
                }
            });
        })
        .catch(error => {
            console.error('Error loading CSV file:', error);
        });
}

// Call the function to display the donut chart
displayDonutChart();
