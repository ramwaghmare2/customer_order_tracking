document.getElementById('orderForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const customerId = document.getElementById('customerId').value;
    const itemId = document.getElementById('itemId').value;
    const itemName = document.getElementById('itemName').value;
    const address = document.getElementById('address').value;

    // Simulate coordinates; in production, you'd get this from geocoding
    const coordinates = { lat: 18.51654159030422, lng: 73.8561114372481 };

    fetch('/send_order', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            customerId: customerId,
            itemId: itemId,
            itemName: itemName,
            address: address,
            coordinates: coordinates
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = '/order_status';
        } else {
            alert('Error submitting order');
        }
    })
    .catch(error => {
        console.error('Error submitting order:', error);
    });
});
