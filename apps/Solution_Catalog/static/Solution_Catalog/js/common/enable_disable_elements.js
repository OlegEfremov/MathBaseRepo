$(document).ready(function() {
    // enable_disable_start_massive_action_button();
});

function enable_disable_start_massive_action_button(){
        // if (action_data['view_folder'] === ''){
        //         document.getElementById('start_massive_action_button').disabled = true;
        // }
        // if (action_data['view_folder'] !== ''){
        //         document.getElementById('start_massive_action_button').disabled = false;
        // }
}

function enable_disable_start_action_button_in_modal(){
    if (action_data['target_folder'] === ''){
            document.getElementById('confirm_button').disabled = true;
    }
    if (action_data['target_folder'] !== ''){
            document.getElementById('confirm_button').disabled = false;
    }
}