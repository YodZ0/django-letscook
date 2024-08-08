function submitForm() {
  var checked_tags_data = [];
  var checked_tags_inputs = document.querySelectorAll('input[name="recipe__tags"]:checked');
  checked_tags_inputs.forEach(function(input) {
    checked_tags_data.push(input.value);
  });

  var ingredients = {};
  var ingredients_table = document.querySelectorAll('#ingredients-body tr');
  ingredients_table.forEach(function(row) {
    var ingredient = row.querySelector('select[name="ingredients"]').value;
    var count = row.querySelector('input[name="ingredient__count"]').value;

    if ((ingredient !== '')) {
    console.log('INGR = ' + ingredient);
      if (count !== '') {
        console.log('COUNT = ' + count);
        ingredients[ingredient] = count;
      };
    };
  });


  var steps = [];
  var steps_table = document.querySelectorAll('#recipe-steps-body textarea[name="recipe__steps"]');
  steps_table.forEach(function(textarea) {
    if (textarea.value) {
      steps.push(textarea.value);
    }
  });

  if (steps.length === 0 ) {
    alert('Write cooking steps!');
  };
  console.log('STEPS = ' + steps.length);

  var formData = {
    title: document.querySelector('input[name="recipe__title"]').value,
    video_url: document.querySelector('input[name="recipe__video_url"]').value,
    description: document.querySelector('textarea[name="recipe__description"]').value,
    tags: checked_tags_data,
    ingredients: ingredients,
    steps: steps,
  };
  var jsonData = JSON.stringify(formData);

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/cabinet/add-recipe/", true);
  xhr.setRequestHeader("Content-Type", "application/json");

  var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
  xhr.setRequestHeader("X-CSRFToken", csrfToken);

  xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.redirect_url) {
              window.location.href = response.redirect_url;
            }
        } else if (xhr.readyState === XMLHttpRequest.DONE) {
            console.error("Error sending data: " + xhr.status);
        }
    };
    xhr.send(jsonData);
}