function clear_cart(){
    checkbox_values = {};
    write_checkbox_values();

    var el = document.getElementById('tasks_cart');
    if (el != null){
        document.getElementById('tasks_cart').innerHTML = ''
    }
}