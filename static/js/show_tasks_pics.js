function show_tasks_pics(is_checked){
    var index = 2;
    if (is_checked) {
        $('#task_body_table th:nth-child(' + index + ')').show();
        $('#task_body_table td:nth-child(' + index + ')').show();
    } else {
        $('#task_body_table th:nth-child(' + index + ')').hide();
        $('#task_body_table td:nth-child(' + index + ')').hide();
    }
}