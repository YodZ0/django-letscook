function deleteRecipe() {
  if (confirm('Are you sure?')) {

    var slug = document.getElementById("slug").value;

    var formData = {
        slug: slug,
      };
    var jsonData = JSON.stringify(formData);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/cabinet/delete-recipe/" + slug, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    xhr.setRequestHeader('X-CSRFToken', csrfToken);

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
}