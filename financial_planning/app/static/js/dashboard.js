// Function to fetch and parse the CSV file
async function fetchDataFromCSV(csvFilename) {
    const response = await fetch(csvFilename);
    const text = await response.text();
    
    const rows = text.split('\n');
    let totalSpent = 0;
    let totalIncome = 0;

    // Parse each row of the CSV file
    rows.forEach((row, index) => {
        // Skip the header row
        if (index === 0) {
            return;
        }
        
        const columns = row.split(',');
        if (columns.length >= 2) {
            const income = parseFloat(columns[1]);
            const dailyExpenses = parseFloat(columns[7]);

            totalIncome += income;
            totalSpent += dailyExpenses;
        }
    });

    // Calculate unspent amount
    const unspent = totalIncome - totalSpent;

    return { totalSpent, unspent };
}

// Function to create the donut chart
function createDonutChart(spent, unspent) {
    const ctx = document.getElementById('donutChart').getContext('2d');
    const donutChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Spent', 'Unspent'],
            datasets: [{
                data: [spent, unspent],
                backgroundColor: ['#FF6384', '#36A2EB'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

// Main function to initialize the dashboard
async function initDashboard() {
    const csvFilename = 'financial_data.csv';
    
    // Fetch data from the CSV file and create the donut chart
    const { totalSpent, unspent } = await fetchDataFromCSV(csvFilename);
    createDonutChart(totalSpent, unspent);
}

// Initialize the dashboard when the document is loaded
document.addEventListener('DOMContentLoaded', initDashboard);
