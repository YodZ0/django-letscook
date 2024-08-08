function AddToCart(btn) {
  var parent = btn.parentNode;
  var slug = parent.getElementsByTagName("input")[1].value;

  var formData = {
      slug: slug,
    };
  var jsonData = JSON.stringify(formData);

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/cart/add/" + slug, true);
  xhr.setRequestHeader("Content-Type", "application/json");

  var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
  xhr.setRequestHeader('X-CSRFToken', csrfToken);

  xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
        } else if (xhr.readyState === XMLHttpRequest.DONE) {
            console.error("Error sending data: " + xhr.status);
        }
    };
  xhr.send(jsonData);

  btn.style.backgroundColor = 'green';
  btn.innerText = 'In cart';
}

function DeleteFromCart(btn) {
  var parent = btn.parentNode;
  var slug = parent.getElementsByTagName("input")[1].value;

  var formData = {
      slug: slug,
    };
  var jsonData = JSON.stringify(formData);

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/cart/delete/" + slug, true);
  xhr.setRequestHeader("Content-Type", "application/json");

  var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
  xhr.setRequestHeader('X-CSRFToken', csrfToken);

  xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
        } else if (xhr.readyState === XMLHttpRequest.DONE) {
            console.error("Error sending data: " + xhr.status);
        }
    };
  xhr.send(jsonData);
  location.reload();
}