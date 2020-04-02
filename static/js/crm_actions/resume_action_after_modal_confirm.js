// squares
function resume_copy_squares(){
        $.ajax({
        type: 'POST',
        url: 'crm_actions/copy_massive',
        data: {
            'list_values': JSON.stringify(square_values),
            'target_folder': action_data['target_folder'],
        },
        dataType: 'json',
        success: function(data){},
        error : function(error) {
            console.log(error)
        }
    });
}

function resume_move_squares(){
        $.ajax({
        type: 'POST',
        url: 'crm_actions/move_massive',
        data: {
            'list_values': JSON.stringify(square_values),
            'target_folder': action_data['target_folder'],
            'current_folder': action_data['view_folder']
        },
        dataType: 'json',
        success: function(data){
            var pathname = window.location.pathname; // Returns path only
            if (pathname.indexOf('solution_catalog') !== -1){
                if (action_data['view_folder']!=='') {
                    show_tasks(action_data['view_folder'], 1, 'show_tasks')
                }
            }
            square_values = {}
        },
        error : function(error) {
            console.log(error)
        }
    });
}

function resume_erase_squares(){
    $.ajax({
        type: 'POST',
        url: 'crm_actions/erase_massive',
        data: {
            'list_values': JSON.stringify(square_values),
            'current_folder': action_data['view_folder']
        },
        dataType: 'json',
        success: function(data){
            var pathname = window.location.pathname; // Returns path only
            if (pathname.indexOf('solution_catalog') !== -1){
                if (action_data['view_folder']!=='') {
                    show_tasks(action_data['view_folder'], 1, 'show_tasks')
                }
            }
            square_values = {}
        },
        error : function(error) {
            console.log(error)
        }
    });
}

function resume_add_attribute_squares(){
    $.ajax({
        type: 'POST',
        url: 'crm_actions/add_attribute_massive',
        data: {
            'list_values': JSON.stringify(square_values),
            'attributes_to_add': JSON.stringify(attributes_to_add),
        },
        dataType: 'json',
        success: function(data){
            var pathname = window.location.pathname; // Returns path only
            if (pathname.indexOf('solution_catalog') !== -1){
                if (action_data['view_folder']!=='') {
                    show_tasks(action_data['view_folder'], 1, 'show_tasks')
                }
            }
        },
        error : function(error) {
            console.log(error)
        }
    });
}


// stars
function resume_copy_stars(){
        $.ajax({
        type: 'POST',
        url: 'crm_actions/copy_massive',
        data: {
            'list_values': JSON.stringify(checkbox_values),
            'target_folder': action_data['target_folder'],
        },
        dataType: 'json',
        success: function(data){
            var pathname = window.location.pathname; // Returns path only
            if (pathname.indexOf('solution_catalog') !== -1){
                if (action_data['view_folder']!=='') {
                    show_tasks(action_data['view_folder'], 1, 'show_tasks')
                }
            }
        },
        error : function(error) {
            console.log(error)
        }
    });
}

function resume_move_stars(){
        $.ajax({
        type: 'POST',
        url: 'crm_actions/move_massive',
        data: {
            'list_values': JSON.stringify(checkbox_values),
            'target_folder': action_data['target_folder'],
            'current_folder': action_data['view_folder']
        },
        dataType: 'json',
        success: function(data){
            var pathname = window.location.pathname; // Returns path only
            if (pathname.indexOf('solution_catalog') !== -1){
                if (action_data['view_folder']!=='') {
                    show_tasks(action_data['view_folder'], 1, 'show_tasks')
                }
            }
            square_values = {}
        },
        error : function(error) {
            console.log(error)
        }
    });
}

function resume_erase_stars(){
        $.ajax({
        type: 'POST',
        url: 'crm_actions/erase_massive',
        data: {
            'list_values': JSON.stringify(checkbox_values),
            'current_folder': action_data['view_folder']
        },
        dataType: 'json',
        success: function(data){
            var pathname = window.location.pathname; // Returns path only
            if (pathname.indexOf('solution_catalog') !== -1){
                if (action_data['view_folder']!=='') {
                    show_tasks(action_data['view_folder'], 1, 'show_tasks')
                }
            }
            square_values = {}
        },
        error : function(error) {
            console.log(error)
        }
    });
}

function resume_add_attribute_stars(){
    $.ajax({
        type: 'POST',
        url: 'crm_actions/add_attribute_massive',
        data: {
            'list_values': JSON.stringify(checkbox_values),
            'attributes_to_add': JSON.stringify(attributes_to_add),
        },
        dataType: 'json',
        success: function(data){
            var pathname = window.location.pathname; // Returns path only
            if (pathname.indexOf('solution_catalog') !== -1){
                if (action_data['view_folder']!=='') {
                    show_tasks(action_data['view_folder'], 1, 'show_tasks')
                }
            }
        },
        error : function(error) {
            console.log(error)
        }
    });
}


// solution
function resume_copy_solution(){
    list_values = {};
    list_values['checkbox_sol_'+crm_action_sol_id] = true;

    $.ajax({
        type: 'POST',
        url: 'crm_actions/copy_massive',
        data: {
            'list_values': JSON.stringify(list_values),
            'target_folder': action_data['target_folder'],
        },
        dataType: 'json',
        success: function(data){},
        error : function(error) {
            console.log(error)
        }
    });
}

function resume_move_solution(){
    list_values = {};
    list_values['checkbox_sol_'+crm_action_sol_id] = true;

    $.ajax({
        type: 'POST',
        url: 'crm_actions/move_massive',
        data: {
            'list_values': JSON.stringify(list_values),
            'target_folder': action_data['target_folder'],
            'current_folder': action_data['view_folder'],
        },
        dataType: 'json',
        success: function(data){
            var pathname = window.location.pathname; // Returns path only
            if (pathname.indexOf('solution_catalog') !== -1){
                if (action_data['view_folder']!=='') {
                    show_tasks(action_data['view_folder'], 1, 'show_tasks')
                }
            }
        },
        error : function(error) {
            console.log(error)
        }
    });
}

function resume_erase_solution(){
    list_values = {};
    list_values['checkbox_sol_'+crm_action_sol_id] = true;

    $.ajax({
        type: 'POST',
        url: 'crm_actions/erase_massive',
        data: {
            'list_values': JSON.stringify(list_values),
            'current_folder': action_data['view_folder'],
        },
        dataType: 'json',
        success: function(data){
            var pathname = window.location.pathname; // Returns path only
            if (pathname.indexOf('solution_catalog') !== -1){
                if (action_data['view_folder']!=='') {
                    show_tasks(action_data['view_folder'], 1, 'show_tasks')
                }
            }
            square_values = {}
        },
        error : function(error) {
            console.log(error)
        }
    });
}

function resume_add_attribute_solution(){
    list_values = {};
    list_values['checkbox_sol_'+crm_action_sol_id] = true;

    $.ajax({
        type: 'POST',
        url: 'crm_actions/add_attribute_massive',
        data: {
            'attributes_to_add': JSON.stringify(attributes_to_add),
            'list_values': JSON.stringify(list_values),
        },
        dataType: 'json',
        success: function(data){
            var pathname = window.location.pathname; // Returns path only
            if (pathname.indexOf('solution_catalog') !== -1){
                if (action_data['view_folder']!=='') {
                    show_tasks(action_data['view_folder'], 1, 'show_tasks')
                }
            }
        },
        error : function(error) {
            console.log(error)
        }
    });
}


// task
function resume_copy_task(){
    list_values = {};
    list_values['checkbox_task_'+crm_action_task_id] = true;

    $.ajax({
        type: 'POST',
        url: 'crm_actions/copy_massive',
        data: {
            'list_values': JSON.stringify(list_values),
            'target_folder': action_data['target_folder'],
        },
        dataType: 'json',
        success: function(data){},
        error : function(error) {
            console.log(error)
        }
    });
}

function resume_move_task(){
    list_values = {};
    list_values['checkbox_task_'+crm_action_task_id] = true;

    $.ajax({
        type: 'POST',
        url: 'crm_actions/move_massive',
        data: {
            'list_values': JSON.stringify(list_values),
            'target_folder': action_data['target_folder'],
            'current_folder': action_data['view_folder'],
        },
        dataType: 'json',
        success: function(data){
            var pathname = window.location.pathname; // Returns path only
            if (pathname.indexOf('solution_catalog') !== -1){
                if (action_data['view_folder']!=='') {
                    show_tasks(action_data['view_folder'], 1, 'show_tasks')
                }
            }
            square_values = {}
        },
        error : function(error) {
            console.log(error)
        }
    });
}

function resume_erase_task(){
    list_values = {};
    list_values['checkbox_task_'+crm_action_task_id] = true;

    $.ajax({
        type: 'POST',
        url: 'crm_actions/erase_massive',
        data: {
            'list_values': JSON.stringify(list_values),
            'current_folder': action_data['view_folder'],
        },
        dataType: 'json',
        success: function(data){
            var pathname = window.location.pathname; // Returns path only
            if (pathname.indexOf('solution_catalog') !== -1){
                if (action_data['view_folder']!=='') {
                    show_tasks(action_data['view_folder'], 1, 'show_tasks')
                }
            }
            square_values = {}
        },
        error : function(error) {
            console.log(error)
        }
    });
}

function resume_add_attribute_task(){
    list_values = {};
    list_values['checkbox_task_'+crm_action_task_id] = true;

    $.ajax({
        type: 'POST',
        url: 'crm_actions/add_attribute_massive',
        data: {
            'attributes_to_add': JSON.stringify(attributes_to_add),
            'list_values': JSON.stringify(list_values),
        },
        dataType: 'json',
        success: function(data){
            var pathname = window.location.pathname; // Returns path only
            if (pathname.indexOf('solution_catalog') !== -1){
                if (action_data['view_folder']!=='') {
                    show_tasks(action_data['view_folder'], 1, 'show_tasks')
                }
            }
        },
        error : function(error) {
            console.log(error)
        }
    });
}
