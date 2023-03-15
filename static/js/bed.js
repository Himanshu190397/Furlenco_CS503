const queryParams = new URLSearchParams(window.location.search);
    const button = queryParams.get('button');

    const data = (event) =>{
        fetch(`api/get_bed/${button}`)
        .then(response => response.json())
        .then(data => {
             const element=$('#bed_rating');
             document.getElementById("bed_heading").innerHTML = data.name;
             document.getElementById("bed_img").src = data.image;
             document.getElementById("bed_size").innerHTML = `Size: ${data.size}`;
             document.getElementById("bed_stock").innerHTML = `In stock: ${data.available}`;
             document.getElementById("bed_price").innerHTML =  `Price: $${data.price}`;
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
//    const dataJSON = JSON.stringify(data());
//    document.getElementById("demo").innerHTML = dataJSON;


