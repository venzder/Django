const renderProduct = ({id, name, image, alt, title, description, coast}) => (
    `
    <div class="cat_product">
            <img
                src="${ image ? image : 'static/products/images/empty.png' }"
                alt="${ alt }"
                title="${ title }"
            >

            <p>${ description }</p>
            <a href="/products/${ id }">${ name }</a>
            <span>
                ${ coast ? coast : 'Значение отсутствует' }
            </span>
            </div>
    `

)