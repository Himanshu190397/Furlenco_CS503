const products=document.querySelectorAll('.sofa_products');

products.forEach(product => {
  product.addEventListener('click', handleClick);
});

function handleClick(event) {
  fetch(`api/get_sofa/${event.target.id.slice(-1)}`)
    .then(response => response.json())
    .then(data => {
      window.location.href = `sofa?button=${event.target.id.slice(-1)}`;
    });
}