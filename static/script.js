document.getElementById('requestForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const inputData = document.getElementById('inputData').value;
  
    fetch('http://127.0.0.1:5000/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            "query": inputData 
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('jsonResponse').textContent = data["response"];
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('jsonResponse').textContent = error;
    });
});
