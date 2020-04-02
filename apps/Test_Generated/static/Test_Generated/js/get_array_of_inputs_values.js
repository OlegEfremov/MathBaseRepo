function get_array_of_inputs_values(){
    var a=[];
    var all_inputs = $(':input[type="number"]');
    for (var i=0; i<all_inputs.length; i++){
        a.push(all_inputs[i].value)
    }
    return a;
}