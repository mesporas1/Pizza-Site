document.addEventListener('DOMContentLoaded', () => {
    var itembutton = document.querySelectorAll('.add-item');
    itembutton.forEach(function(item){
        item.onclick = () => {alert("Item added to cart")};
    });
});
