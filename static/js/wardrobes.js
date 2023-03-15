const products=document.querySelectorAll('.wardrobe_products');

products.forEach(product => {
  product.addEventListener('click', handleClick);
});

function handleClick(event) {
  fetch(`api/get_wardrobe/${event.target.id.slice(-1)}`)
    .then(response => response.json())
    .then(data => {
      window.location.href = `wardrobe?button=${event.target.id.slice(-1)}`;
    });
}