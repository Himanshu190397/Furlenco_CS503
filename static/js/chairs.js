const products=document.querySelectorAll('.chair_products');

products.forEach(product => {
  product.addEventListener('click', handleClick);
});

function handleClick(event) {
  fetch(`api/get_chair/${event.target.id.slice(-1)}`)
    .then(response => response.json())
    .then(data => {
      window.location.href = `chair?button=${event.target.id.slice(-1)}`;
    });
}