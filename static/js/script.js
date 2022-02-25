(function($){
  $(function(){

    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown();
    $('select').formSelect();
    $('input#input_text, textarea#recipe_description').characterCounter();
    $('.carousel').carousel();

    // adds steps & ingredients on form

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
            <input id="recipe_method${stp}" name="recipe_method" type="text" class="validate" required>
            <label for="recipe_method${stp}">Recipe Step</label>
            <button type="button" class="btn remove-step">Delete</button></div>`);
    });
  
    $("body").on('click', ".remove-step", function () {
        $(this).parent('div').remove();
        stp--;
    });

    // validation of dropdown list on add recipe

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


  }); // end of document ready
})(jQuery); // end of jQuery name space

