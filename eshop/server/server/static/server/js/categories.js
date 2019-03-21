const renderCategory = ({id, name}) => (
    `
     <li class="categories_item">
     <span class="categories__item-name">
                ${ name }
            </span>      
        <a href="/categories/${ id }">${ name }</a>
        </li> 
    `

)