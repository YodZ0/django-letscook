var idCounter = 2;

function addRow() {

    var clone = document.getElementById("recipe-step-1").cloneNode(true);
    var newRowId = "recipe-step-" + idCounter;
    var newTextInputId = "recipe-step-text-" + idCounter;

    clone.id = newRowId;
    clone.querySelector("textarea").id = newTextInputId;
    idCounter++;

    clone.querySelector("textarea").value = "";
    clone.querySelector("textarea").style.removeProperty('height');

    document.getElementById("recipe-steps-body").appendChild(clone);
    renumberRows();
}

function deleteRow(input) {
    var parent = input.parentNode.parentNode;

    if (parent.id === "recipe-step-1") {
      alert("Элемент нельзя удалить");
    } else {
      parent.remove();
      renumberRows();
    }
}

function getTableLen() {
  var table = document.getElementById("recipe_table");
  var rows = table.getElementsByClassName("recipeSteps__row").length;
  return rows;
}

function renumberRows() {
  var table = document.getElementById("recipe_table");
  var rows = table.getElementsByTagName("tbody")[0].getElementsByTagName("tr");

  for (var i = 0; i < rows.length; i++) {
    rows[i].getElementsByTagName("td")[0].innerText = (i + 1);
  }
}