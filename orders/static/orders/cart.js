document.addEventListener('DOMContentLoaded', () => {
    var itembutton = document.querySelectorAll('.remove-item');
    itembutton.forEach(function(item){
        item.onclick = () => {alert("Item removed from cart")};
    });
});
