function find_task_by_id() {
    var task_id = document.getElementById('find_task_by_id_input').value;

    $.ajax({
        url: "find_task_by_id",
        type: "POST",
        data: {'task_id': task_id},
        success: function (res) {
            MathJax.Hub.Startup.onload();
            document.getElementById('table_of_tasks').innerHTML = '';
            res = compile_img_in_show_tasks(res);
            document.getElementById('table_of_tasks').innerHTML = res;
            MathJax.Hub.Queue(["Typeset", MathJax.Hub]);

            checkbox_all_init_vars(); //initialize vars for checkbox_all (file checkbox_all_init_vars)
            set_sols_checkbox();
            set_task_checkbox_by_sols();
        },
        error: function (ts) {
            console.log(ts)
        }
    });
    return false;

}