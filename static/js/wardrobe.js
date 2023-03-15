const queryParams = new URLSearchParams(window.location.search);
    const button = queryParams.get('button');

    const data = (event) =>{
        fetch(`api/get_wardrobe/${button}`)
        .then(response => response.json())
        .then(data => {
            const element=$('#wardrobe_rating');
            document.getElementById("wardrobe_heading").innerHTML = data.name;
             document.getElementById("wardrobe_img").src = data.image;
             document.getElementById("wardrobe_category").innerHTML = `Category: ${data.category}`;
             document.getElementById("wardrobe_stock").innerHTML = `In stock: ${data.available}`;
             document.getElementById("wardrobe_price").innerHTML =  `Price: $${data.price}`;
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