document.addEventListener('DOMContentLoaded', () => {
    const itemForm = document.getElementById('itemForm');
    const itemsList = document.getElementById('itemsList');
  
    // Fetch and display items
    fetch('/items')
      .then(response => response.json())
      .then(items => {
        itemsList.innerHTML = '';
        items.forEach(item => {
          const li = document.createElement('li');
          li.textContent = `${item.name}: ${item.value}`;
          itemsList.appendChild(li);
        });
      });
  
    // Add item
    itemForm.addEventListener('submit', (event) => {
      event.preventDefault();
      const name = document.getElementById('name').value;
      const value = document.getElementById('value').value;
  
      fetch('/items', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, value })
      })
      .then(response => response.text())
      .then(message => {
        console.log(message);
        location.reload(); // Refresh to show the new item
      });
    });
  });
  