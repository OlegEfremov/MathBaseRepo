var square_values={};

$(document).ready(function() {});

function reset_square_values(){
    square_values = {};
    write_square_counter()
}

function change_node_icon_square(node){
    if ($(node).find('svg').length === 0){
        $(node).find('i').toggleClass('fa-square fa-check-square');
    }
    else {
        $(node).find('svg').toggleClass('fa-square fa-check-square');
        }
}

function set_node_icon_square(node, state){
    var old_class='', new_class='';
    if (state){
        old_class='fa-square';
        new_class='fa-check-square'

    } else{
        old_class='fa-check-square';
        new_class='fa-square'
    }

    if ($(node).find('svg').length === 0){
        $(node).find('i').removeClass(old_class);
        $(node).find('i').addClass(new_class);
    }
    else {
        $(node).find('svg').removeClass(old_class);
        $(node).find('svg').addClass(new_class);
        }
}

function set_node_state_square(node, state){
    if (state) {
        node.value = 'true';
        set_node_icon_square(node, true);
        square_values[node.id] = true;
    }
    else{
        node.value = 'false';
        set_node_icon_square(node, false);
        square_values[node.id] = false;
    }
}

function button_square_task(node) {


    let task_id = node.id.replace('square_task_','');

    //change state value
    set_node_state_square(node, !string_to_boolean(node.value));

    var el = document.getElementById('square_all');
    if (node.value === 'false'){
        el.value = 'false';
        set_node_icon_square(el,false)
    }

    var el = document.getElementById('square_page');
    if (node.value === 'false'){
        el.value = 'false';
        set_node_icon_square(el,false)
    }


    //add state value to json
    square_values[node.id] = string_to_boolean(node.value);

    //select or deselect all needed solution checkbox
    page_tasks_needed_sols_json[task_id].forEach(
        function(item, i, arr) {
            var el = document.getElementById('square_sol_'+item)
            el.value = node.value;
            square_values['square_sol_'+item] = string_to_boolean(node.value);
            if (node.value === 'true'){
                set_node_icon_square(el, true)
                }
            else{
                set_node_icon_square(el, false)
            }
        });
    write_square_counter()
}

function button_square_sol(node) {
    //change icon on button
    change_node_icon_square(node)

    let sol_id = node.id.replace('square_sol_','');

    let task_id = node.getAttribute('task');
    let task_node = document.getElementById('square_task_' + task_id);

    //change state value
    if (node.value === 'false') {
        node.value = 'true'
    } else {
        node.value = 'false';
        if (!is_another_sol(sol_id)){set_node_state_square(task_node, false)}
    }

    if (!is_another_sol(sol_id)) {
        var el = document.getElementById('square_all');
        if (node.value === 'false') {
            el.value = 'false';
            set_node_icon_square(el, false)
        }

        var el = document.getElementById('square_page');
        if (node.value === 'false') {
            el.value = 'false';
            set_node_icon_square(el, false)
        }
    }


    //add state value to json
    square_values[node.id] = string_to_boolean(node.value);

    set_task_checkbox_by_sols_square()
}

function set_task_checkbox_by_sols_square(){
    for (let task_id in page_tasks_needed_sols_json){
        let task_state = true;
        for (let i in page_tasks_needed_sols_json[task_id]){
            let sol_id = page_tasks_needed_sols_json[task_id][i];
            task_state *= string_to_boolean(document.getElementById('square_sol_'+sol_id).value)
        }
        if (task_state === 1){
            let task_node = document.getElementById('square_task_'+task_id);
            set_node_state_square(task_node, true);
        }
    }
    write_square_counter()
}

function button_square_page(node) {
    if (node.value === 'false'){node.value = 'true'}
    else {node.value = 'false'}

    //set state to checkbox_all
    let el = document.getElementById('square_all');
    if (node.value === 'false'){
        el.value = 'false';
        set_node_icon_square(el, false)
    }

    change_node_icon_square(node)

    for (let i in page_tasks){
        let task_id = page_tasks[i];
        let task_node = document.getElementById('square_task_' + task_id);
        set_node_state_square(task_node, string_to_boolean(node.value));

        for (let ind in page_tasks_needed_sols_json[page_tasks[i]]){
            let sol_id = page_tasks_needed_sols_json[page_tasks[i]][ind];
            let sol_node = document.getElementById('square_sol_' + sol_id);
            set_node_state_square(sol_node, string_to_boolean(node.value));

        }
    }
    write_square_counter()
}

function button_square_all(node) {

    if (node.value === 'false'){node.value = 'true'}
    else {node.value = 'false'}
    change_node_icon_square(node)

    //set state to checkbox_page
    let el = document.getElementById('square_page');
    if (node.value === 'false'){
        el.value = 'false';
        set_node_icon_square(el, false)
    }
    else {
        el.value = 'true';
        set_node_icon_square(el, true)
    }

    for (let i in all_tasks){
        let task_id = all_tasks[i];
        square_values['square_task_' + task_id] = string_to_boolean(node.value);

        for (let ind in all_tasks_needed_sols_json[all_tasks[i]]){
            let sol_id = all_tasks_needed_sols_json[all_tasks[i]][ind];
            square_values['square_sol_' + sol_id] = string_to_boolean(node.value);
        }
    }

    for (let i in page_tasks){
        let task_id = page_tasks[i];
        let task_node = document.getElementById('square_task_' + task_id);
        set_node_state_square(task_node, string_to_boolean(node.value));

        for (let ind in page_tasks_needed_sols_json[page_tasks[i]]){
            let sol_id = page_tasks_needed_sols_json[page_tasks[i]][ind];
            let sol_node = document.getElementById('square_sol_' + sol_id);
            set_node_state_square(sol_node, string_to_boolean(node.value));

        }
    }
    write_square_counter()
}

function write_square_counter() {
    var sendData = square_values;
    sendData = JSON.stringify(sendData);

    $.ajax({
        url: '../../count_squares',
        type: "POST",
        data: {'square_values': sendData},
        success: function(res) {
            document.getElementById('square_counter').innerHTML = res
            console.log(res)
        },
        error: function(ts) {
            console.log(ts)
        }
    });
}