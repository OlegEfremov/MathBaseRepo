function get_per_page(){
    var e = document.getElementById('select_tasks_per_page');
    return e.options[e.selectedIndex].innerHTML;
}


function show_tasks(dbID, page, dbType){
    document.getElementById('table_of_tasks').innerHTML = 'Задачи загружаются...<br><img src="../../static/images/loader.gif">';
    $.ajax({
        url: 'show_tasks',
        type: "POST",
        data: {
            'dbID': dbID,
            'dbType': dbType,
            'page': page,
            'per_page': get_per_page(),
            'tasks_only_outside_catalog': document.getElementById('toggle_tasks_only_outside_catalog').checked
        },
        success: function(res) {
            MathJax.Hub.Startup.onload();
            document.getElementById('table_of_tasks').innerHTML = '';
            res = compile_img_in_show_tasks(res);
            document.getElementById('table_of_tasks').innerHTML = res;
            MathJax.Hub.Queue(["Typeset",MathJax.Hub]);

            init_checkbox_values();
            checkbox_all_init_vars(); //initialize vars for checkbox_all (file checkbox_all_init_vars)
            set_sols_checkbox();
            set_task_checkbox_by_sols();

            reset_square_values()
        },
        error: function(ts) {
            console.log(ts)
        }
    })
}