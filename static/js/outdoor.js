const products=document.querySelectorAll('.outdoor_products');

products.forEach(product => {
  product.addEventListener('click', handleClick);
});

function handleClick(event) {
  fetch(`api/get_outdoor/${event.target.id.slice(-1)}`)
    .then(response => response.json())
    .then(data => {
      window.location.href = `outdoors?button=${event.target.id.slice(-1)}`;
    });
}