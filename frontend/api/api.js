async function getOrderStatus(orderId) {
    const response = await fetch(`/order_status/${orderId}`);
    const data = await response.json();
    return data.order_status;
}
