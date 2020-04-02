function button_checkbox_page(node) {

    if (node.value === 'false'){node.value = 'true'}
    else {node.value = 'false'}

    $(node).find('svg').toggleClass('fa-square fa-check-square');
    // console.log(page_tasks);
    // console.log(page_tasks_needed_sols_json);

    for (let i in page_tasks){
        let task_id = page_tasks[i];
        let task_node = document.getElementById('checkbox_task_' + task_id);
        set_node_state(task_node, string_to_boolean(node.value));

        for (let ind in page_tasks_needed_sols_json[page_tasks[i]]){
            let sol_id = page_tasks_needed_sols_json[page_tasks[i]][ind];
            let sol_node = document.getElementById('checkbox_sol_' + sol_id);
            set_node_state(sol_node, string_to_boolean(node.value));

        }
    }
    write_checkbox_counter()
}

function button_checkbox_all(node) {
    button_checkbox_page(node);

    //set state to checbox_page
    let el = document.getElementById('checkbox_page');
    if (node.value === 'false'){
        el.value = 'false';
        $(el).find('svg').removeClass('fa-check');
        $(el).find('svg').addClass('fa-copy');
    }
    else {
        el.value = 'true';
        $(el).find('svg').removeClass('fa-copy');
        $(el).find('svg').addClass('fa-check');
    }

    for (let i in all_tasks){
        let task_id = all_tasks[i];
        checkbox_values['checkbox_task_' + task_id] = string_to_boolean(node.value);
        write_checkbox_values();

        for (let ind in all_tasks_needed_sols_json[all_tasks[i]]){
            let sol_id = all_tasks_needed_sols_json[all_tasks[i]][ind];
            checkbox_values['checkbox_sol_' + sol_id] = string_to_boolean(node.value);
            write_checkbox_values();
        }
    }
    write_checkbox_counter()
}

function button_checkbox_task(node) {
    //change icon on button
    $(node).find('svg').toggleClass('fa-square fa-check-square');

    let task_id = node.id.replace('checkbox_task_','');

    //change state value
    if (node.value === 'false'){node.value = 'true'}
    else {node.value = 'false'}

    //add state value to json
    checkbox_values[node.id] = string_to_boolean(node.value);
    write_checkbox_values();

    //select or deselect all needed solution checkbox
    page_tasks_needed_sols_json[task_id].forEach(
        function(item, i, arr) {
            document.getElementById('checkbox_sol_'+item).value = node.value;
            checkbox_values['checkbox_sol_'+item] = string_to_boolean(node.value);
            write_checkbox_values();
            if (node.value === 'true'){
                $('#checkbox_sol_'+item).find('svg').removeClass('fa-squre');
                $('#checkbox_sol_'+item).find('svg').addClass('fa-check-square')
                }
            else{
                $('#checkbox_sol_'+item).find('svg').removeClass('fa-check-square');
                $('#checkbox_sol_'+item).find('svg').addClass('fa-square')
            }
        });

    write_checkbox_counter()
}

function button_checkbox_sol(node) {
    //change icon on button
    $(node).find('svg').toggleClass('fa-copy fa-check');

    let sol_id = node.id.replace('checkbox_sol_','');

    let task_id = node.getAttribute('task');
    let task_node = document.getElementById('checkbox_task_' + task_id);

    //change state value
    if (node.value === 'false') {
        node.value = 'true'
    } else {
        node.value = 'false';
        if (!is_another_sol(sol_id)){set_node_state(task_node, false)}
    }

    //add state value to json
    checkbox_values[node.id] = string_to_boolean(node.value);
    write_checkbox_values();

    // set_task_state_by_solutions(task_id);
    write_checkbox_counter();
    set_task_checkbox_by_sols()
}

function set_node_state(node, state){
    if (state) {
        node.value = 'true';
        $('#'+node.id).find('svg').removeClass('fa-copy');
        $('#'+node.id).find('svg').addClass('fa-check');

        $('#'+node.id).find('i').removeClass('fa-copy');
        $('#'+node.id).find('i').addClass('fa-check');

        checkbox_values[node.id] = true;
        write_checkbox_values()
    }
    else{
        node.value = 'false';
        $('#'+node.id).find('svg').removeClass('fa-check');
        $('#'+node.id).find('svg').addClass('fa-copy');

        $('#'+node.id).find('i').removeClass('fa-check');
        $('#'+node.id).find('i').addClass('fa-copy');

        checkbox_values[node.id] = false;
        write_checkbox_values()
    }
}

function is_another_sol(sol_id) {
    return another_sols.includes(sol_id)
}