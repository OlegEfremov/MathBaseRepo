function get_per_page(){
    var e = document.getElementById('select_tasks_per_page');
    return e.options[e.selectedIndex].innerHTML;
}


// Показывает задания, соответствующие текущему фильтру
// Привязана к кнопке в Расширенном фильтре
function show_tasks(page) {
    get_mathattr_in_filter_json();
    var sendData = $('#filter_tree').jstree('get_json', "#");
    sendData = JSON.stringify(sendData);
    document.getElementById('table_of_tasks').innerHTML = 'Задачи загружаются...<br><img src="../../static/images/loader.gif">';
    $.ajax({
        url: "show_tasks",
        type: "POST",
        data: {'json_tree': sendData, 'page': page, 'per_page': get_per_page()},
        success: function(res) {
            MathJax.Hub.Startup.onload();
            document.getElementById('table_of_tasks').innerHTML = '';
            // document.getElementById('table_of_tasks').innerHTML = set_checkbox_values(res);
            res = compile_img_in_show_tasks(res);
            document.getElementById('table_of_tasks').innerHTML = res;
            MathJax.Hub.Queue(["Typeset",MathJax.Hub]);

            checkbox_all_init_vars(); //initialize vars for checkbox_all (file checkbox_all_init_vars)
            set_sols_checkbox();
            set_task_checkbox_by_sols();

            reset_square_values()
        },
        error: function(ts) {
            console.log(ts)
        }
    });
    return false;
}
