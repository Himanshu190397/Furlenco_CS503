const queryParams = new URLSearchParams(window.location.search);
    const button = queryParams.get('button');

    const data = (event) =>{
        fetch(`api/get_desk/${button}`)
        .then(response => response.json())
        .then(data => {
            const element=$('#desk_rating');
            document.getElementById("desk_heading").innerHTML = data.name;
             document.getElementById("desk_img").src = data.image;
             document.getElementById("desk_material").innerHTML = `Material: ${data.material}`;
             document.getElementById("desk_stock").innerHTML = `In stock: ${data.available}`;
             document.getElementById("desk_price").innerHTML =  `Price: $${data.price}`;
             for(let i=1; i<=5; i++){
                   if(i<=data.user_rating){
                        element.append('<i class="fa-solid fa-star"></i>');
                    } else {
                        element.append('<i class="fa-regular fa-star"></i>');
                    }
             }
        })
        .catch(error => {
        console.error('Error:', error);
        });
    }

    data();