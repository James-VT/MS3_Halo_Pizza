$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();

  });

var next_ingredient_button = document.getElementById('next-ingredient-button');
var ingredient_insert = document.getElementById('ingredient-insert')

/** The below code links to our add recipe page, and creates a new ingredient slot each time it is clicked
 * Below code heavily borrowed from: https://www.youtube.com/watch?v=MLBLsxcB3Dc
 */
next_ingredient_button.onclick = function(){
    var nextIngredient = document.createElement('input');
    nextIngredient.setAttribute('type', 'text');
    nextIngredient.setAttribute('id', 'ingredients');
    nextIngredient.setAttribute('name', 'ingredients');
    nextIngredient.setAttribute('minlength', '4');
    nextIngredient.setAttribute('required', 'true');
    ingredient_insert.appendChild(nextIngredient);
}