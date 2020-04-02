$(document).ready(function() {
    init_all_tasks_all_sols_json();
    init_checkbox_values();
    write_checkbox_counter();

    // set_checkbox_values();
    // if (document.getElementById('checkbox_counter') != null){
    //     document.getElementById('checkbox_counter').innerHTML = count_checkboxes();
    // }
});

// // инициализирует checkbox_values
// function set_checkbox_values() {
// 	if (sessionStorage.getItem('checkbox_values') == null) {
//         checkbox_values = {};
// 	    sessionStorage.setItem('checkbox_values', JSON.stringify(checkbox_values));
//     } else {
//         checkbox_values =  JSON.parse(sessionStorage.getItem('checkbox_values'));
//     }
// }


//считает количество выбранных решений и задач по массивам checkbox_values и tasks_sols
//tasks_sols - массив задач и входящих в них решений
// function count_checkboxes(){
//     let sols=0, tasks=0, tasks_list={};
//     for (let item in checkbox_values){
//         if (checkbox_values[item]){
//             if (item.indexOf('sol') !== -1){
//                 sols += 1;
//                 for (let task in tasks_sols){
//                     let sol_id = item.replace('checkbox_sol_', '');
//                     if (tasks_sols[task].includes(sol_id)) {tasks_list[task] = true}
//                 }
//             }
//         }
//     }
//     for (let item in tasks_list){
//         if (tasks_list[item]){tasks += 1 }
//     }
//     return '' +  tasks.toString() + ' (' + sols.toString()+')';
// }
