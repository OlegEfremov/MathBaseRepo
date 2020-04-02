function copy_cart_to_folder(){
    // console.log(checkbox_values);
    action_data['action_type'] = 'massive_copy';
    action_data['checkbox_values'] = checkbox_values;
    // console.log(action_data);
    massive_copy();
    $('#choose_target_folder_modal').modal('show');
}
