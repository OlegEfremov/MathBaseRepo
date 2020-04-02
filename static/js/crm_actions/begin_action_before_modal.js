var crm_action_type = '',
    crm_action_sol_id = '',
    crm_action_task_id = '',
    list_values = {},
    attributes_to_add = {};

// squares actions
function copy_squares_begin(){
    crm_action_type = 'copy_squares';

    document.getElementById('confirm_button').innerHTML = 'Копировать';
    document.getElementById('choose_target_folder_ModalLabel').innerHTML = 'В какую папку копировать выбранное?';

    $('#choose_target_folder_modal').modal('show');
}

function move_squares_begin(){
    crm_action_type = 'move_squares';

    document.getElementById('confirm_button').innerHTML = 'Переместить';
    document.getElementById('choose_target_folder_ModalLabel').innerHTML = 'В какую папку переместить выбранное?';

    $('#choose_target_folder_modal').modal('show');
}

function erase_squares_begin(){
    crm_action_type = 'erase_squares';

    document.getElementById('remove_modal_text').innerHTML = 'Удалить выбранное из папки?'
    $('#remove_task_from_folder_modal').modal('show')
}

function add_attribute_squares_begin(){
    crm_action_type = 'add_attribute_squares';

    document.getElementById('add_attribute_ModalLabel').innerHTML = 'Выберите атрибуты, которые нужно добавить к выбранным решениям?';
    $('#add_attribute_modal').modal('show')
}


// stars actions
function copy_stars_begin(){
    crm_action_type = 'copy_stars';

    document.getElementById('confirm_button').innerHTML = 'Копировать';
    document.getElementById('choose_target_folder_ModalLabel').innerHTML = 'В какую папку копировать выбранное?';

    $('#choose_target_folder_modal').modal('show');
}

function move_stars_begin(){
    crm_action_type = 'move_stars';

    document.getElementById('confirm_button').innerHTML = 'Переместить';
    document.getElementById('choose_target_folder_ModalLabel').innerHTML = 'В какую папку переместить выбранное?';

    $('#choose_target_folder_modal').modal('show');
}

function erase_stars_begin(){
    crm_action_type = 'erase_stars';

    document.getElementById('remove_modal_text').innerHTML = 'Удалить выбранное из папки?'
    $('#remove_task_from_folder_modal').modal('show')
}

function add_attribute_stars_begin(){
    crm_action_type = 'add_attribute_stars';

    document.getElementById('add_attribute_ModalLabel').innerHTML = 'Выберите атрибуты, которые нужно добавить к выбранным решениям?';
    $('#add_attribute_modal').modal('show')
}

// solution action
function copy_solution_begin(sol_id){
    crm_action_type = 'copy_solution';
    crm_action_sol_id = sol_id;

    document.getElementById('confirm_button').innerHTML = 'Копировать';
    document.getElementById('choose_target_folder_ModalLabel').innerHTML = 'В какую папку копировать решение?';

    // enable_disable_start_action_button_in_modal();
    $('#choose_target_folder_modal').modal('show');
}

function move_solution_begin(sol_id){
    crm_action_type = 'move_solution';
    crm_action_sol_id = sol_id;

    document.getElementById('confirm_button').innerHTML = 'Переместить';
    document.getElementById('choose_target_folder_ModalLabel').innerHTML = 'В какую папку переместить решение?';

    // enable_disable_start_action_button_in_modal();
    $('#choose_target_folder_modal').modal('show');
}

function erase_solution_begin(sol_id){
    crm_action_type = 'erase_solution';
    crm_action_sol_id = sol_id;

    document.getElementById('remove_modal_text').innerHTML = 'Удалить решение из папки?';
    $('#remove_task_from_folder_modal').modal('show')
}

function add_attribute_solution_begin(sol_id){
    crm_action_type = 'add_attribute_solution';
    crm_action_sol_id = sol_id;

    document.getElementById('add_attribute_ModalLabel').innerHTML = 'Выберите атрибуты, которые нужно добавить к решению?';
    $('#add_attribute_modal').modal('show')
}


// task action
function copy_task_begin(task_id){
    crm_action_type = 'copy_task';
    crm_action_task_id = task_id;

    document.getElementById('confirm_button').innerHTML = 'Копировать';
    document.getElementById('choose_target_folder_ModalLabel').innerHTML = 'В какую папку копировать задачу?';

    // enable_disable_start_action_button_in_modal();
    $('#choose_target_folder_modal').modal('show');
}

function move_task_begin(task_id){
    crm_action_type = 'move_task';
    crm_action_task_id = task_id;

    document.getElementById('confirm_button').innerHTML = 'Переместить';
    document.getElementById('choose_target_folder_ModalLabel').innerHTML = 'В какую папку переместить задачу?';

    // enable_disable_start_action_button_in_modal();
    $('#choose_target_folder_modal').modal('show');
}

function erase_task_begin(task_id){
    crm_action_type = 'erase_task';
    crm_action_task_id = task_id;

    document.getElementById('remove_modal_text').innerHTML = 'Удалить задачу из папки?';
    $('#remove_task_from_folder_modal').modal('show')
}

function add_attribute_task_begin(task_id){
    crm_action_type = 'add_attribute_task';
    crm_action_task_id = task_id;

    document.getElementById('add_attribute_ModalLabel').innerHTML = 'Выберите атрибуты, которые нужно добавить ко всем решениям задачи?';
    $('#add_attribute_modal').modal('show')
}