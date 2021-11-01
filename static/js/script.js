$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();

  });

let next_ingredient_button = document.getElementById('next-ingredient-button');

// The below code links to our add recipe page, and creates a new ingredient slot each time it is clicked
next_ingredient_button.onclick = function(){
    let nextIngredient = document.createElement('input');
    nextIngredient.setAttribute('type', 'text');
    nextIngredient.setAttribute('id', 'ingredients');
    nextIngredient.setAttribute('name', 'ingredients');
    nextIngredient.setAttribute('minlength', '4');
    nextIngredient.setAttribute('required');
}