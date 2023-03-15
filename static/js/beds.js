const products=document.querySelectorAll('.bed_products');

//products.forEach(product => {
//    product.addEventListener('click', event =>{
//        const id=event.target.id;
//        console.log(id);
//    });
//});

products.forEach(product => {
  product.addEventListener('click', handleClick);
});

//function handleClick(event) {
//  fetch(`api/get_bed/${event.target.id.slice(-1)}`)
//    .then(response => response.json())
//    .then(data => {
//      console.log(data);
//    });
//}

function handleClick(event) {
  fetch(`api/get_bed/${event.target.id.slice(-1)}`)
    .then(response => response.json())
    .then(data => {
      window.location.href = `bed?button=${event.target.id.slice(-1)}`;
    });
}