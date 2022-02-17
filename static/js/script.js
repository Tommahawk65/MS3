(function($){
  $(function(){

    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown();
    $('select').formSelect();
    $('input#input_text, textarea#recipe_description').characterCounter();

    let ing = 1;

    $(".add-ingredient").click(function (e) {
        e.preventDefault();
            ing++;
            $(".ing-new").append(`
            <div class="input-field">
            <input id="recipe_ingredients${ing}" name="recipe_ingredients" type="text" class="validate" required>
            <label for="recipe_ingredients${ing}">Recipe Ingredient</label>
            <button type="button" class="btn remove-ingredient">Delete</button></div>`);
    });
  
    $("body").on('click', ".remove-ingredient", function () {
        $(this).parent('div').remove();
        ing--;
    });


    let stp = 1;

    $(".add-step").click(function (e) {
        e.preventDefault();
            stp++;
            $(".step-new").append(`
            <div class="input-field">
            <input id="recipe_steps${stp}" name="recipe_steps" type="text" class="validate" required>
            <label for="recipe_steps${stp}">Recipe Step</label>
            <button type="button" class="btn remove-step">Delete</button></div>`);
    });
  
    $("body").on('click', ".remove-step", function () {
        $(this).parent('div').remove();
        stp--;
    });

  }); // end of document ready
})(jQuery); // end of jQuery name space

