$(document).ready(function() {
    init_all_tasks_all_sols_json();
});

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