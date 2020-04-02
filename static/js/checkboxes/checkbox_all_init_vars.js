var another_sols = '',

    all_tasks = [],
    all_sols = [],

    all_tasks_all_sols_json = {},
    all_tasks_another_sols_json = {},
    all_tasks_needed_sols_json = {},

    page_tasks = [],
    page_sols = [],
    page_tasks_all_sols_json = {},
    page_tasks_another_sols_json = {},
    page_tasks_needed_sols_json = {};

    init_all_tasks_all_sols_json();


function checkbox_all_init_vars() {
    another_sols = document.getElementById('another_sols').innerHTML.split(',');
    all_tasks = document.getElementById('all_tasks').innerHTML.split(',');
    all_sols = document.getElementById('all_sols').innerHTML.split(',');
    page_tasks = document.getElementById('page_tasks').innerHTML.split(',');
    page_sols = document.getElementById('page_sols').innerHTML.split(',');

    all_tasks_another_sols_json = {};
    all_tasks_needed_sols_json = {};
    page_tasks_all_sols_json = {};
    page_tasks_another_sols_json = {};
    page_tasks_needed_sols_json = {};

    let all_tasks_and_sols = document.getElementById('all_tasks_json').innerHTML.split(';');
    if (document.getElementById('all_tasks_json').innerHTML === ''){
        all_tasks_all_sols_json = {};
    }
    else{
        all_tasks_and_sols.forEach(function (value, index, array) {
            let task_and_sols = value.split(':');
            let task = task_and_sols[0],
                sols = task_and_sols[1].split(',');
            all_tasks_all_sols_json[task] = sols;
        });
    }

    for (let task in all_tasks_all_sols_json) {
        let task_another_sols = [], task_needed_sols = [];
        all_tasks_all_sols_json[task].forEach(function (value, index, array) {
            if (another_sols.includes(value)) {
                task_another_sols.push(value)
            }
            else {
                task_needed_sols.push(value)
            }
        });
        all_tasks_another_sols_json[task] = task_another_sols;
        all_tasks_needed_sols_json[task] = task_needed_sols;
    }

    let page_tasks_and_sols = document.getElementById('page_tasks_json').innerHTML.split(';');
    if (document.getElementById('page_tasks_json').innerHTML === ''){
        page_tasks_all_sols_json = {};
    }
    else {
        page_tasks_and_sols.forEach(function (value, index, array) {
            let task_and_sols = value.split(':');
            let task = task_and_sols[0],
                sols = task_and_sols[1].split(',');
            page_tasks_all_sols_json[task] = sols;
        });
    }

    for (let task in page_tasks_all_sols_json) {
        let task_another_sols = [], task_needed_sols = [];
        page_tasks_all_sols_json[task].forEach(function (value, index, array) {
            if (another_sols.includes(value)) {
                task_another_sols.push(value)
            }
            else {
                task_needed_sols.push(value)
            }
        });
        page_tasks_another_sols_json[task] = task_another_sols;
        page_tasks_needed_sols_json[task] = task_needed_sols;
    }

    write_all_tasks_all_sols_json();
}

function init_all_tasks_all_sols_json() {
    if (sessionStorage.getItem('all_tasks_all_sols_json') == null) {
        all_tasks_all_sols_json = {};
        write_all_tasks_all_sols_json();
    } else {
        read_all_tasks_all_sols_json();
    }
}

function read_all_tasks_all_sols_json() {
    all_tasks_all_sols_json =  JSON.parse(sessionStorage.getItem('all_tasks_all_sols_json'));
}

function write_all_tasks_all_sols_json() {
    sessionStorage.setItem('all_tasks_all_sols_json', JSON.stringify(all_tasks_all_sols_json));
}

function set_task_checkbox_by_sols(){
    for (let task_id in page_tasks_needed_sols_json){
        let task_state = true;
        for (let i in page_tasks_needed_sols_json[task_id]){
            let sol_id = page_tasks_needed_sols_json[task_id][i];
            task_state *= string_to_boolean(document.getElementById('checkbox_sol_'+sol_id).value)
        }
        if (task_state === 1){
            let task_node = document.getElementById('checkbox_task_'+task_id);
            set_node_state(task_node, true);
        }
    }
}

function set_sols_checkbox(){

    $.ajax({
        url: '../../read_checkbox_values',
        type: "POST",
        data: {},
        success: function(res) {
            var checkbox_values_t = res
            if (document.getElementById('page_sols').innerHTML !== "") {
                for (let i in page_sols) {
                    let sol_id = page_sols[i];
                    let sol_node = document.getElementById('checkbox_sol_' + sol_id);
                    if (checkbox_values_t[sol_node.id]) {
                        set_node_state(sol_node, true);
                    }
                }
            }
            set_task_checkbox_by_sols()
        },
        error: function(ts) {
            console.log(ts)
        }
    });
}