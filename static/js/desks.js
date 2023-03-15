const products=document.querySelectorAll('.desk_products');

products.forEach(product => {
  product.addEventListener('click', handleClick);
});

function handleClick(event) {
  fetch(`api/get_desk/${event.target.id.slice(-1)}`)
    .then(response => response.json())
    .then(data => {
      console.log(data);
      window.location.href = `desk?button=${event.target.id.slice(-1)}`;
    });
}