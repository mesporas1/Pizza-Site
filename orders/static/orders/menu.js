document.addEventListener('DOMContentLoaded', () => {
    var itembutton = document.querySelectorAll('.add-item');
    itembutton.forEach(function(item){
        item.onclick = () => {alert("Item added to cart")};
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