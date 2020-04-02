function show_tasks_without_solution(page = '1') {
    show_tasks_url = 'show_tasks_without_solution';
    $.ajax({
        url: "show_tasks_without_solution",
        type: "GET",
        data: {'page': page, 'per_page': get_per_page()},
        success: function (res) {
            MathJax.Hub.Startup.onload();
            document.getElementById('table_of_tasks').innerHTML = '';
            document.getElementById('table_of_tasks').innerHTML = res;
            MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        },
        error: function (ts) {
            alert('show_tasks_without_solution ERROR');
        }
    });
    return false;
}


function create_solution_for_empty_tasks(){
    $.ajax({
        url: "create_solution_for_empty_tasks",
        type: "GET",
        success: function (res) {
            MathJax.Hub.Startup.onload();
            document.getElementById('table_of_tasks').innerHTML = '';
            document.getElementById('table_of_tasks').innerHTML = res;
            MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        },
        error: function (ts) {
            alert('create_solution_for_empty_tasks ERROR');
        }
    });
    return false;
}

function show_tasks_outside_folders(page = '1'){
    show_tasks_url = 'show_tasks_outside_folders';
    $.ajax({
        url: "show_tasks_outside_folders",
        type: "GET",
        data: {'page': page, 'per_page': get_per_page()},
        success: function (res) {
            MathJax.Hub.Startup.onload();
            document.getElementById('table_of_tasks').innerHTML = '';
            document.getElementById('table_of_tasks').innerHTML = res;
            MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        },
        error: function (ts) {
            alert('show_tasks_outside_folders ERROR');
        }
    });
    return false;
}