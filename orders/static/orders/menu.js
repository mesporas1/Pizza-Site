document.addEventListener('DOMContentLoaded', () => {
    var itembutton = document.querySelectorAll('.add-item');
    itembutton.forEach(function(item){
        item.onclick = () => {alert("Item added to cart")};
    });

    // Select your input element.
    var number = document.querySelectorAll('.quantity');
    // Listen for input event on numInput.
    number.forEach(function(item){
        item.onkeydown = function(e) {
            if(!((e.keyCode > 95 && e.keyCode < 106)
            || (e.keyCode > 47 && e.keyCode < 58) 
            || e.keyCode == 8)) {
                return false;
            }
        };
    });
});

document.addEventListener('click', function(e) {
    e = e || window.event;
    var target = e.target || e.srcElement
    var text = target.textContent || target.innerText;
    var numTop = target.parentElement.getAttribute("data-numTop"); 
    var toppings = target.parentElement.children;
    var checker = 0;
    if (target.parentElement.getAttribute("name") == "topping"){
        for (var i = 0; i < toppings.length; i++){
            if (toppings[i].getAttribute("type") == "checkbox" && toppings[i].checked){
                checker += 1;
                if (checker > numTop){
                    alert("You can only select " + numTop + " toppings!");
                    e.preventDefault();
                }
            }
        }
    }

}, false);
