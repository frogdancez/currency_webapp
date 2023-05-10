function displayDate() {
  const dateHourElem = document.getElementById('date-hour');
  const now = new Date();
  const formattedDate = now.toLocaleDateString('pt-BR', {
    day: 'numeric',
    month: 'numeric',
    year: 'numeric'
  });
  const formattedTime = now.toLocaleTimeString('pt-BR', {
    hour: 'numeric',
    minute: 'numeric'
  });
  dateHourElem.textContent = `${formattedDate} and ${formattedTime}`;
}

fetchData();
setInterval(fetchData);
setInterval(displayDate);