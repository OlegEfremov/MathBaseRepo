function task_copy(task_id){
    action_data['action_type'] = 'task_copy';
    action_data['element_id'] = task_id;

    document.getElementById('confirm_button').innerHTML = 'Копировать';
    document.getElementById('choose_target_folder_ModalLabel').innerHTML = 'В какую папку копировать задачу?'

    enable_disable_start_action_button_in_modal();
    $('#choose_target_folder_modal').modal('show');
}


function task_move(task_id){
    action_data['action_type'] = 'task_move';
    action_data['element_id'] = task_id;

    document.getElementById('confirm_button').innerHTML = 'Переместить';
    document.getElementById('choose_target_folder_ModalLabel').innerHTML = 'В какую папку переместить задачу?'

    enable_disable_start_action_button_in_modal();
    $('#choose_target_folder_modal').modal('show');
}

function task_remove(task_id){
    action_data['action_type'] = 'task_remove';
    action_data['element_id'] = task_id;

    document.getElementById('remove_modal_text').innerHTML = 'Удалить задачу?'

    $('#remove_task_from_folder_modal').modal('show')
}

function solution_copy(sol_id){
    action_data['action_type'] = 'solution_copy';
    action_data['element_id'] = sol_id;

    document.getElementById('confirm_button').innerHTML = 'Копировать';
    document.getElementById('choose_target_folder_ModalLabel').innerHTML = 'В какую папку копировать решение?'

    enable_disable_start_action_button_in_modal();
    $('#choose_target_folder_modal').modal('show');
}

function solution_move(sol_id){
    action_data['action_type'] = 'solution_move';
    action_data['element_id'] = sol_id;

    document.getElementById('confirm_button').innerHTML = 'Переместить';
    document.getElementById('choose_target_folder_ModalLabel').innerHTML = 'В какую папку переместить решение?'

    enable_disable_start_action_button_in_modal();
    $('#choose_target_folder_modal').modal('show');
}

function solution_remove(sol_id){
    action_data['action_type'] = 'solution_remove';
    action_data['element_id'] = sol_id;

    document.getElementById('remove_modal_text').innerHTML = 'Удалить решение?';

    $('#remove_task_from_folder_modal').modal('show')
}


function add_attribute_to_solution(sol_id){
    action_data['action_type'] = 'add_attribute_to_solution';
    action_data['element_id'] = sol_id;

    document.getElementById('add_attribute_ModalLabel').innerHTML = 'Выберите атрибуты, которые нужно добавить к решению?';
    $('#add_attribute_modal').modal('show')
}


function massive_action() {
    action_data['action_type'] = document.getElementById("select_massive_action").value;
    action_data['element_type'] = 'checkboxes';
    action_data['element_id'] = 'checkboxes';
    action_data['checkbox_values'] = checkbox_values;
    enable_disable_start_action_button_in_modal();

    if (action_data['action_type'] === 'massive_copy') {
        massive_copy()
    }
    if (action_data['action_type'] === 'massive_move') {
        massive_move()
    }
    if (action_data['action_type'] === 'massive_remove'){
        massive_remove()
    }
    if (action_data['action_type'] === 'massive_add_attribute_to_solution'){
        massive_add_attribute()
    }
    if (action_data['action_type'] === 'massive_export'){
        massive_export()
    }
}

function massive_copy() {
    crm_action_type = 'copy_stars';
    document.getElementById('confirm_button').innerHTML = 'Копировать';
    document.getElementById('choose_target_folder_ModalLabel').innerHTML = 'В какую папку копировать выбранные задачи и решения?';
    $('#choose_target_folder_modal').modal('show');
}

function massive_move() {
    document.getElementById('confirm_button').innerHTML = 'Переместить';
    document.getElementById('choose_target_folder_ModalLabel').innerHTML = 'В какую папку переместить выбранные задачи и решения?';
    $('#choose_target_folder_modal').modal('show');
}

function massive_remove() {
    document.getElementById('remove_modal_text').innerHTML = 'Удалить выбранные задачи и решения?';
    $('#remove_task_from_folder_modal').modal('show')
}

function massive_add_attribute() {
    action_data['action_type'] = 'massive_add_attribute_to_solution';
    action_data['checkbox_values'] = checkbox_values;
    document.getElementById('add_attribute_ModalLabel').innerHTML = 'Выберите атрибуты, которые нужно добавить отмеченным решениям?';
    $('#add_attribute_modal').modal('show')
}


function massive_export() {
    $('#export_modal').modal('show');
}

function export_tasks() {
    let rows = document.getElementsByTagName("table")[0].rows;
    let list_of_id = [];
    for (var i = 0; i < rows.length; i++) {
        list_of_id.push(rows[i].id)
    }
}


// bind to buttons from modals on main_page
function copy_move_remove_task_or_solution(){
    let send_data = action_data;
    send_data = JSON.stringify(send_data);
    $.ajax({
        type: 'POST',
        url: 'copy_move_remove_task_or_solution',
        data: {'data': send_data},
        dataType: 'json',
        success: function(data){
            var pathname = window.location.pathname; // Returns path only


            if (pathname !== '/edit_source_catalog/main_page' && pathname !== '/edit_source_catalog/main_page_system'){
                if (action_data['view_folder']!=='') {
                    show_tasks(action_data['view_folder'], 1, show_tasks_url)
                }
            }
        },
        error : function(error) {console.log(error)
        }
    });
}