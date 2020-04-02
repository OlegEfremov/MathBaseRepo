function get_per_page(){
    var e = document.getElementById('select_tasks_per_page');
    return e.options[e.selectedIndex].innerHTML;
}