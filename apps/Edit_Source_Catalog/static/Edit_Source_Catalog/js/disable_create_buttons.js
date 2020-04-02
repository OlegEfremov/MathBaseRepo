function disable_create_buttons(){

    $('#create_source_folder_button').prop('disabled', true);
    $('#create_source_button').prop('disabled', true);
    $('#create_task_number_button').prop('disabled', true);
    $('#create_task_button').prop('disabled', true);
    $('#create_chapter_button').prop('disabled', true);
    $('#import_tasks_button').prop('disabled', true);
    $('#import_from_test_button').prop('disabled', true);


    if (create_data['node_dbType'] === 'TaskNumber'){
        $('#create_source_folder_button').prop('disabled', true);
        $('#create_source_button').prop('disabled', true);
        $('#create_task_number_button').prop('disabled', true);
        $('#create_task_button').prop('disabled', true);
        $('#create_chapter_button').prop('disabled', true);
        $('#import_tasks_button').prop('disabled', true);
        $('#import_from_test_button').prop('disabled', true);
    }

    if (create_data['node_dbType'] === 'Source'){
        $('#create_source_folder_button').prop('disabled', true);
        $('#create_source_button').prop('disabled', true);
        $('#create_task_number_button').prop('disabled', false);
        $('#create_task_button').prop('disabled', false);
        $('#create_chapter_button').prop('disabled', false);
        $('#import_tasks_button').prop('disabled', false);
        $('#import_from_test_button').prop('disabled', false);
    }

    if (create_data['node_dbType'] === 'Source_Folder'){
        $('#create_source_folder_button').prop('disabled', false);
        $('#create_source_button').prop('disabled', false);
        $('#create_task_number_button').prop('disabled', true);
        $('#create_task_button').prop('disabled', true);
        $('#create_chapter_button').prop('disabled', true);
        $('#import_tasks_button').prop('disabled', true);
        $('#import_from_test_button').prop('disabled', true);
    }

    if (create_data['node_dbType'] === 'Chapter'){
        $('#create_source_folder_button').prop('disabled', true);
        $('#create_source_button').prop('disabled', true);
        $('#create_task_number_button').prop('disabled', false);
        $('#create_task_button').prop('disabled', false);
        $('#create_chapter_button').prop('disabled', false);
        $('#import_tasks_button').prop('disabled', false);
        $('#import_from_test_button').prop('disabled', false);
    }
}
