function test_csv(){
    var csv_text = document.getElementById('test_csv_textarea').value;

    if (csv_text[csv_text.length-1] !== '@'){
        document.getElementById('test_view_task_table').innerHTML = 'ERROR - problem with last string - delete all symbols after last dog';
        return false
    }
    var count_task = (csv_text.match(/@end_string@/g) || []).length;
    var count_dog = (csv_text.match(/@/g) || []).length;

    if (count_dog % count_task !== 0){
        document.getElementById('test_view_task_table').innerHTML = 'ERROR - problem with dogs';
        console.log('ERROR - problem with dogs')
        // return false
    }


    var string_array = csv_text.split('@end_string@');

    var table = '<table class="table table-bordered" id="text_csv_table" >';

    for (var i=0; i<string_array.length-1; i++){
        var fields = string_array[i].split('@');
        if (fields.length !== 7){
            document.getElementById('test_view_task_table').innerHTML = 'ERROR2'+'\n'+string_array[i];
            if (i !== 0 && i !== string_array.length){
                document.getElementById('test_view_task_table').innerHTML = 'ERROR2'+'\n'+string_array[i-1]+'\n'+string_array[i]+'\n'+string_array[i+1];
            }
            else {
                document.getElementById('test_view_task_table').innerHTML = 'ERROR2'+'\n'+string_array[i]+'END OR LAST';
            }
            console.log(i);
            return false
        }
        var source = fields[0],
            chapter = fields[1],
            task_order = fields[2],
            tasknumber = fields[3],
            task_body = fields[4],
            ans = fields[5],
            sol_instruction = fields[6];

        table += '<tr>';
        table += '<td>№'+tasknumber+'</td>';
        table += '<td>'+task_body+'</td>';
        table += '<td>'+ans+'</td>';
        table += '</tr>'
    }

    table += '</table>';

    MathJax.Hub.Startup.onload();
    document.getElementById('test_view_task_table').innerHTML = '';
    document.getElementById('test_view_task_table').innerHTML = table;
    MathJax.Hub.Queue(["Typeset",MathJax.Hub]);

    // $.ajax({
    //     url: 'test_csv',
    //     type: "POST",
    //     data: {'csv_text': csv_text},
    //     success: function(res) {
    //         MathJax.Hub.Startup.onload();
    //         document.getElementById('test_view_task_table').innerHTML = '';
    //         document.getElementById('test_view_task_table').innerHTML = res;
    //         MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
    //     },
    //     error: function(ts) {
    //         console.log(ts)
    //     }
    // })
}