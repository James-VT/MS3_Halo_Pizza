$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.modal').modal();

    /**The below code was taken from CodeInstitute's source code for their Task Manager project.
     * It sorts out Materialize's interpretation of what a <select> element should be, and
     * allows us to perform proper validation upon it.
     */
    
     validateMaterializeSelect();
     function validateMaterializeSelect() {
         let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
         let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
         if ($("select.validate").prop("required")) {
             $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
         }
         $(".select-wrapper input.select-dropdown").on("focusin", function () {
             $(this).parent(".select-wrapper").on("change", function () {
                 if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                     $(this).children("input").css(classValid);
                 }
             });
         }).on("click", function () {
             if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                 $(this).parent(".select-wrapper").children("input").css(classValid);
             } else {
                 $(".select-wrapper input.select-dropdown").on("focusout", function () {
                     if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                         if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                             $(this).parent(".select-wrapper").children("input").css(classInvalid);
                         }
                     }
                 });
             }
         });
     }
  });

/**Below is the functionality for adding additional ingredient fields to the add_recipe page */
var next_ingredient_button = document.getElementById('next-ingredient-button');
var ingredient_insert = document.getElementById('ingredient-insert');
var delete_ingredient_button = document.getElementById('delete-ingredient-button');
var ingredient_section = document.getElementById('ingredient-section');

/** The below code links to our add recipe page, and creates a new ingredient slot each time it is clicked
 * Below code heavily borrowed from: https://www.youtube.com/watch?v=MLBLsxcB3Dc
 */
 next_ingredient_button.onclick = function(){
    var nextIngredient = document.createElement('input');
    nextIngredient.setAttribute('type', 'text');
    nextIngredient.setAttribute('id', 'ingredients');
    nextIngredient.setAttribute('name', 'ingredients');
    nextIngredient.setAttribute('class', 'ingredient-input');
    nextIngredient.setAttribute('minlength', '4');
    nextIngredient.setAttribute('required', 'true');
    nextIngredient.setAttribute('placeholder', 'Another ingredient');
    ingredient_section.appendChild(nextIngredient);
}

delete_ingredient_button.onclick = function(){
    var ingredient_fields = document.getElementsByClassName('ingredient-input');
    if(ingredient_fields.length > 1) {
        ingredient_section.removeChild(ingredient_fields[(ingredient_fields.length) - 1]);
    }
}

/**Below is the functionality for adding additional cooking step fields to the add_recipe page */
var next_step_button = document.getElementById('next-step-button');
var step_insert = document.getElementById('step-insert');
var delete_step_button = document.getElementById('delete-step-button');
var cooking_steps_section = document.getElementById('cooking-steps-section');

/** The below code links to our add recipe page, and creates a new cooking step slot each time it is clicked
 * Below code heavily borrowed from: https://www.youtube.com/watch?v=MLBLsxcB3Dc
 */
 next_step_button.onclick = function(){
    var nextStep = document.createElement('input');
    nextStep.setAttribute('type', 'text');
    nextStep.setAttribute('id', 'cooking_steps');
    nextStep.setAttribute('name', 'cooking_steps');
    nextStep.setAttribute('class', 'cooking_steps');
    nextStep.setAttribute('minlength', '4');
    nextStep.setAttribute('required', 'true');
    nextStep.setAttribute('placeholder', 'Another step');
    cooking_steps_section.appendChild(nextStep);
}

delete_step_button.onclick = function(){
    var step_fields = document.getElementsByClassName('cooking_steps');
    if(step_fields.length > 1) {
        cooking_steps_section.removeChild(step_fields[(step_fields.length) - 1]);
    }
}