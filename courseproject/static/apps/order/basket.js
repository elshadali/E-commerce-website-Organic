function removeRow(rowID, orderID) {
    $(rowID).remove();
    deleteOrder(orderID);
    let count = document.getElementById('basket-order-count');
    count.innerHTML -= 1;
}



function calcPlusTotal(ID) {
  let price = document.getElementById(`price-${ID}`).innerText;
  let quantity = parseInt(document.getElementById(`qty-${ID}`).value);
  document.getElementById(`qty-${ID}`).value = quantity+1
  quantity += 1;
  let result = document.getElementById(`total-${ID}`).innerHTML = parseFloat((parseFloat(price) * parseFloat(quantity)).toFixed(2));
  btn = document.getElementById(`minus-button-${ID}`);
  btn.disabled = false
  calcTotal();
}



function calcMinusTotal(ID) {
  let price = document.getElementById(`price-${ID}`).innerText;
  let quantity = document.getElementById(`qty-${ID}`).value;
  document.getElementById(`qty-${ID}`).value = quantity-1
  quantity -= 1;
  document.getElementById(`total-${ID}`).innerHTML = parseFloat((parseFloat(price) * parseFloat(quantity)).toFixed(2));
  if (parseInt(quantity) === 1) {
      btn = document.getElementById(`minus-button-${ID}`);
      btn.disabled = true
  }
  calcTotal();
}




function deleteOrder(orderID) {
    request_url = order_delete_url.replace('1', orderID);
    $.ajax({
      method: "DELETE",
      url: request_url, 
      headers: { "X-CSRFToken": csrftoken_ },
      dataType: "json",
      success: function () {
        calcTotal();
        manageCheckoutButton();
      },
      error: function(data) {
        console.log('error cixdi', data);
      }
    });
  }


function calcTotal() {
  let totals = document.getElementsByName('order-total');
  let result = 0.00;
  for (i of totals) {
    result += parseFloat(i.innerHTML);
  }
  let shipping = result * 5 / 100
  document.getElementById('sub-total').innerHTML = parseFloat(result.toFixed(2));
  document.getElementById('shipping').innerHTML = parseFloat(shipping.toFixed(2));
  document.getElementById('final-total').innerHTML = parseFloat((shipping + result).toFixed(2));
  }



function getItems() {
  data = []
  let items = document.getElementsByTagName('tr');
  for (let i of items) {
    data.push(i.getAttribute('id'))
  }
  return JSON.stringify(data)
}  


function createMainOrder() {
  $.ajax({
    method: "POST",
    url: main_order_create_url,
    headers: { "X-CSRFToken": csrftoken_ },
    data: {
      subtotal: document.getElementById('sub-total').innerText,
      total: document.getElementById("final-total").innerText,
      shipping: document.getElementById("shipping").innerText,
      items: getItems(),
    },
    dataType: "json",
    success: function (resp) {
      window.location.href = resp.data['absolute_url'];
    },
    error: function(data) {
    }
  });
}

function manageCheckoutButton() {
  let items = document.getElementsByName('order-items');
  let checkoutButton = document.getElementById('checkout-btn');
  if (items.length === 0) {
    checkoutButton.setAttribute('disabled', 'disabled');
  } else {
    checkoutButton.removeAttribute('disabled');
  }
}