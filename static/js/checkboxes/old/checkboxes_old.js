$(document).ready(function() {
    init_checkbox_values();
    write_checkbox_counter()
});

function init_checkbox_values() {
    if (sessionStorage.getItem('checkbox_values') == null) {
        checkbox_values = {};
        write_checkbox_values();
    } else {
        read_checkbox_values();
    }
}

function read_checkbox_values() {
    checkbox_values =  JSON.parse(sessionStorage.getItem('checkbox_values'));
}

function write_checkbox_values() {
    sessionStorage.setItem('checkbox_values', JSON.stringify(checkbox_values));
}

function write_checkbox_counter() {
    var sendData = checkbox_values;
    sendData = JSON.stringify(sendData);

    var counter_text = '';

    $.ajax({
        url: '../../count_checkboxes',
        type: "POST",
        data: {'checkbox_values': sendData},
        success: function(res) {
            document.getElementById('checkbox_counter').innerHTML = res
        },
        error: function(ts) {
            console.log(ts)
        }
    });
}

// function count_checkboxes(){
//     var sendData = checkbox_values;
//     sendData = JSON.stringify(sendData);
//
//     var counter_text = '';
//
//     $.ajax({
//         url: '../../count_checkboxes',
//         type: "POST",
//         data: {'checkbox_values': sendData},
//         success: function(res) {
//             counter_text = res
//         },
//         error: function(ts) {
//             console.log(ts)
//         }
//     });
//
//     return counter_text


    //     let sols=0, tasks=0, tasks_list={};
//     for (let item in checkbox_values){
//         if (checkbox_values[item]){
//             if (item.indexOf('sol') !== -1){
//                 sols += 1;
//                 //if one or more sols of this task checked then add true to task_list
//                 for (let task in all_tasks_all_sols_json){
//                     let sol_id = item.replace('checkbox_sol_', '');
//                     if (all_tasks_all_sols_json[task].includes(sol_id)) {tasks_list[task] = true}
//                 }
//             }
//         }
//     }
//     // count true in tasks_list
//     for (let item in tasks_list){
//         if (tasks_list[item]){tasks = tasks+1}
//     }
//     return '' +  tasks.toString() + ' (' + sols.toString()+')';
// }



function string_to_boolean(s){
    if (s==='false'){return false}
    if (s==='true'){return true}
}

function button_checkbox_page(node) {
    if (node.value === 'false'){node.value = 'true'}
    else {node.value = 'false'}

    // console.log('kggjg')
    //set state to checkbox_all
    let el = document.getElementById('checkbox_all');
    if (node.value === 'false'){
        el.value = 'false';
        $(el).find('svg').removeClass('fa-check-square');
        $(el).find('svg').addClass('fa-square');
    }


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
    // button_checkbox_page(node);

    if (node.value === 'false'){node.value = 'true'}
    else {node.value = 'false'}
    $(node).find('svg').toggleClass('fa-square fa-check-square');

    //set state to checkbox_page
    let el = document.getElementById('checkbox_page');
    if (node.value === 'false'){
        el.value = 'false';
        $(el).find('svg').removeClass('fa-check-square');
        $(el).find('svg').addClass('fa-square');
    }
    else {
        el.value = 'true';
        $(el).find('svg').removeClass('fa-square');
        $(el).find('svg').addClass('fa-check-square');
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

function change_node_icon(node){
    if ($(node).find('svg').length === 0){
        $(node).find('i').toggleClass('fa-square fa-check-square');
    }
    else {
        $(node).find('svg').toggleClass('fa-square fa-check-square');
        }
}

function button_checkbox_task(node) {
    change_node_icon(node)

    let task_id = node.id.replace('checkbox_task_','');

    //change state value
    if (node.value === 'false'){node.value = 'true'}
    else {node.value = 'false'}

    var el = document.getElementById('checkbox_all');
    if (node.value === 'false'){
        el.value = 'false';
        $(el).find('svg').removeClass('fa-check-square');
        $(el).find('svg').addClass('fa-square');
    }

    var el = document.getElementById('checkbox_page');
    if (node.value === 'false'){
        el.value = 'false';
        $(el).find('svg').removeClass('fa-check-square');
        $(el).find('svg').addClass('fa-square');
    }


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
                $('#checkbox_sol_'+item).find('svg').removeClass('fa-square');
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
    change_node_icon(node)

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

    if (!is_another_sol(sol_id)) {
        var el = document.getElementById('checkbox_all');
        if (node.value === 'false') {
            el.value = 'false';
            $(el).find('svg').removeClass('fa-check-square');
            $(el).find('svg').addClass('fa-square');
        }

        var el = document.getElementById('checkbox_page');
        if (node.value === 'false') {
            el.value = 'false';
            $(el).find('svg').removeClass('fa-check-square');
            $(el).find('svg').addClass('fa-square');
        }
    }


    //add state value to json
    checkbox_values[node.id] = string_to_boolean(node.value);
    write_checkbox_values();

    // set_task_state_by_solutions(task_id);
    write_checkbox_counter();
    set_task_checkbox_by_sols()
}

// function set_checkbox_values(res) {
// 	for (var x in checkbox_values){
//         if (checkbox_values[x] && x.indexOf('task') === -1) {
//             res = res.replace('value="false" id="'+x+'"><i class="fas fa-copy">', 'value="true" id="'+x+'"><i class="fas fa-check">')
//         }
//     }
//     return res
// }

function set_node_state(node, state){
    if (state) {
        node.value = 'true';
        $('#'+node.id).find('svg').removeClass('fa-square');
        $('#'+node.id).find('svg').addClass('fa-check-square');

        $('#'+node.id).find('i').removeClass('fa-square');
        $('#'+node.id).find('i').addClass('fa-check-square');

        checkbox_values[node.id] = true;
        write_checkbox_values()
    }
    else{
        node.value = 'false';
        $('#'+node.id).find('svg').removeClass('fa-check-square');
        $('#'+node.id).find('svg').addClass('fa-square');

        $('#'+node.id).find('i').removeClass('fa-check-square');
        $('#'+node.id).find('i').addClass('fa-square');

        checkbox_values[node.id] = false;
        write_checkbox_values()
    }
}

function is_another_sol(sol_id) {
    return another_sols.includes(sol_id)
}