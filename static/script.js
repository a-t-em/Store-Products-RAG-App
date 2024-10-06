document.getElementById('requestForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const inputData = document.getElementById('inputData').value;
    const data = {"query": inputData};

    fetch('http://localhost:5000/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('jsonResponse').textContent = data["response"];
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('jsonResponse').textContent = 'An error occurred';
    });
});
