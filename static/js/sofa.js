const queryParams = new URLSearchParams(window.location.search);
    const button = queryParams.get('button');

    const data = (event) =>{
        fetch(`api/get_sofa/${button}`)
        .then(response => response.json())
        .then(data => {
            const element=$('#sofa_rating');
            document.getElementById("sofa_heading").innerHTML = data.name;
             document.getElementById("sofa_img").src = data.image;
             document.getElementById("sofa_material").innerHTML = `Material: ${data.material}`;
             document.getElementById("sofa_seats").innerHTML = `${data.no_seats} seater`;
             document.getElementById("sofa_stock").innerHTML = `In stock: ${data.available}`;
             document.getElementById("sofa_price").innerHTML =  `Price: $${data.price}`;
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