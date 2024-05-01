// Get current date
const currentDate = new Date();

// Display current month and year
document.getElementById('current-date').textContent = currentDate.toLocaleString('default', { month: 'long', year: 'numeric' });

// Render calendar grid
renderCalendar(currentDate.getFullYear(), currentDate.getMonth());

// Previous month button event listener
document.getElementById('prev-month').addEventListener('click', () => {
    const currentMonth = currentDate.getMonth();
    const currentYear = currentDate.getFullYear();
    const prevMonth = currentMonth === 0 ? 11 : currentMonth - 1;
    const prevYear = currentMonth === 0 ? currentYear - 1 : currentYear;

    // Update current date and render calendar
    currentDate.setFullYear(prevYear, prevMonth);
    document.getElementById('current-date').textContent = currentDate.toLocaleString('default', { month: 'long', year: 'numeric' });
    renderCalendar(prevYear, prevMonth);
});

// Next month button event listener
document.getElementById('next-month').addEventListener('click', () => {
    const currentMonth = currentDate.getMonth();
    const currentYear = currentDate.getFullYear();
    const nextMonth = currentMonth === 11 ? 0 : currentMonth + 1;
    const nextYear = currentMonth === 11 ? currentYear + 1 : currentYear;

    // Update current date and render calendar
    currentDate.setFullYear(nextYear, nextMonth);
    document.getElementById('current-date').textContent = currentDate.toLocaleString('default', { month: 'long', year: 'numeric' });
    renderCalendar(nextYear, nextMonth);
});

// Function to render calendar grid for a given year and month
function renderCalendar(year, month) {
    const calendarGrid = document.getElementById('calendar-grid');
    calendarGrid.innerHTML = ''; // Clear previous calendar

    // Get the first day of the month and the total number of days
    const firstDayOfMonth = new Date(year, month, 1).getDay(); // 0 = Sunday, 1 = Monday, ..., 6 = Saturday
    const totalDaysInMonth = new Date(year, month + 1, 0).getDate();

    // Create empty cells for days before the first day of the month
    for (let i = 0; i < firstDayOfMonth; i++) {
        const cell = document.createElement('div');
        cell.classList.add('calendar-cell');
        calendarGrid.appendChild(cell);
    }

    // Create cells for each day of the month
    for (let day = 1; day <= totalDaysInMonth; day++) {
        const cell = document.createElement('div');
        cell.classList.add('calendar-cell');
        cell.textContent = day;
        calendarGrid.appendChild(cell);
    }
}
