const queryParams = new URLSearchParams(window.location.search);
    const button = queryParams.get('button');

    const data = (event) =>{
        fetch(`api/get_chair/${button}`)
        .then(response => response.json())
        .then(data => {
            const element=$('#chair_rating');
            document.getElementById("chair_heading").innerHTML = data.name;
             document.getElementById("chair_img").src = data.image;
             document.getElementById("chair_material").innerHTML = `Material: ${data.material}`;
             document.getElementById("chair_stock").innerHTML = `In stock: ${data.available}`;
             document.getElementById("chair_price").innerHTML =  `Price: $${data.price}`;
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