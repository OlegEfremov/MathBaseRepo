function write_checkbox_counter() {
    document.getElementById('checkbox_counter').innerHTML = count_checkboxes();
}

function count_checkboxes(){
    let sols=0, tasks=0, tasks_list={};
    for (let item in checkbox_values){
        if (checkbox_values[item]){
            if (item.indexOf('sol') !== -1){
                sols += 1;
                //if one or more sols of this task checked then add true to task_list
                for (let task in all_tasks_all_sols_json){
                    let sol_id = item.replace('checkbox_sol_', '');
                    if (all_tasks_all_sols_json[task].includes(sol_id)) {tasks_list[task] = true}
                }
            }
        }
    }
    // count true in tasks_list
    for (let item in tasks_list){
        if (tasks_list[item]){tasks = tasks+1}
    }
    return '' +  tasks.toString() + ' (' + sols.toString()+')';
}