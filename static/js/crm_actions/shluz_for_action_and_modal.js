function resume_action_after_modal_confirm(){
    // squares
    if (crm_action_type === 'copy_squares'){
        resume_copy_squares()
    }
    else if (crm_action_type === 'move_squares'){
        resume_move_squares()
    }
    else if (crm_action_type === 'erase_squares'){
        resume_erase_squares()
    }

    else if (crm_action_type === 'add_attribute_squares'){
        resume_add_attribute_squares()
    }

    // stars
    else if (crm_action_type === 'copy_stars'){
        resume_copy_stars()
    }
    else if (crm_action_type === 'move_stars'){
        resume_move_stars()
    }
    else if (crm_action_type === 'erase_stars'){
        resume_erase_stars()
    }
    else if (crm_action_type === 'add_attribute_stars'){
        resume_add_attribute_stars()
    }

    // solution
    else if (crm_action_type === 'copy_solution'){
        resume_copy_solution()
    }
    else if (crm_action_type === 'move_solution'){
        resume_move_solution()
    }
    else if (crm_action_type === 'erase_solution'){
        resume_erase_solution()
    }
    else if (crm_action_type === 'add_attribute_solution'){
        resume_add_attribute_solution()
    }

    // task
    else if (crm_action_type === 'copy_task'){
        resume_copy_task()
    }
    else if (crm_action_type === 'move_task'){
        resume_move_task()
    }
    else if (crm_action_type === 'erase_task'){
        resume_erase_task()
    }
    else if (crm_action_type === 'add_attribute_task'){
        resume_add_attribute_task()
    }
}