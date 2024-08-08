var idCounter = 2;

function add() {

    var clone = document.getElementById("ingredient-row-1").cloneNode(true);
    var newRowId = "ingredient-row-" + idCounter;
    var newSelectorInputId = "ingredient-selector-" + idCounter;

    clone.id = newRowId;
    clone.querySelector("select").id = newSelectorInputId;
    clone.querySelector("input").value = "";
    idCounter++;

    document.getElementById("ingredients-body").appendChild(clone);
}

function del(input) {
    var parent = input.parentNode.parentNode;
    console.log(parent);

    if (parent.id === "ingredient-row-1") {
      alert("Элемент нельзя удалить");
    } else {
      parent.remove();
    }
}