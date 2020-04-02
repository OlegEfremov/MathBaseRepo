function find_task_by_source_and_number(page) {
    var source = document.getElementById('find_task_by_source_input').value;
    var tasknumber = document.getElementById('find_task_by_tasknumber_input').value;
    document.getElementById('table_of_tasks').innerHTML = 'Задачи загружаются...<br><img src="../../static/images/loader.gif">';
    console.log(source);
    $.ajax({
        url: "find_task_by_source_and_number",
        type: "POST",
        data: {'source': source, 'tasknumber': tasknumber, 'page': page, 'per_page': get_per_page()},
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

$(function() {
  var t = document.getElementById("all_sources").innerHTML;
  t = t.replace('\n','');
  t = t.replace('\r','');
  var s = t.split('@@');
  $("#find_task_by_source_input").autocomplete({source: s});
});