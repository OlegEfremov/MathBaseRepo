function import_tasks_show_modal(){
    document.getElementById("csv_text_form").value = '';
    $('#import_tasks_modal').modal('show');
}


function import_tasks(){
    var csv_text = document.getElementById("csv_text_form").value;
    import_ending(csv_text)
}

function import_ending(csv_text){
    let send_data = create_data;

    send_data = JSON.stringify(send_data);
    $.ajax({
        type: 'POST',
        url: 'import_tasks',
        data: {'data': send_data, 'csv_text': csv_text},
        dataType: 'json',
        success: function(data){
            document.getElementById('test_csv_textarea').value = 'IMPORT SUCCESS!\n' + document.getElementById('test_csv_textarea').value
        },
        error : function(error) {
            document.getElementById('test_csv_textarea').value = 'ERROR!\n' + document.getElementById('test_csv_textarea').value
        }
    });

}

function replace_all_frac_with_dfrac(){
    var textarea = document.getElementById('test_csv_textarea');
    textarea.value = textarea.value.replace(/\\frac/g, '\\dfrac');

    textarea.value = textarea.value.replace(/\^\s*{\s*\\dfrac/g, '^ { \\frac');
    textarea.value = textarea.value.replace(/\^\s*{\s*-\s*\\dfrac/g, '^ { - \\frac');

    textarea.value = textarea.value.replace(/\\log\s*_\s*{\s*\\dfrac/g, '\\log_{ \\frac');
    textarea.value = textarea.value.replace(/\\log\s*_\s*{\s*-\s*\\dfrac/g, '\\log_{ - \\frac');

    }

function input_new_task_string_in_textarea(){
    var el = $('#test_csv_textarea');
    var empty_task_string = '@@1@num@task@ans@@end_string@';
    typeInTextarea(el, empty_task_string)
}


$( document ).ready(function() {
    var template = $("#form_rows_tpl").html(),
        $target = $(".dynamic-rows"),
        $btnAdd = $("button.add"),
        $btnRemove = $("button.remove"),
        $msg = $('.msg'),
        max = 10,
        count = 1,
        inputRow = [];

    $btnAdd.click(function(e){
      e.preventDefault();
      addRows();
    });

    $btnRemove.click(function(e){
      e.preventDefault();
      removeRows();
    });

function addRows(){
  if(count <= max){
    inputRow = {
      count : count
    }
    var html = Mustache.to_html(template, inputRow);
    $target.append(html);
    count++;
  }else{
    $msg.text('too many fields!');
  }
}

function removeRows(){
  $target.find('.row').last().remove();
  $msg.text('');
  if(count <= 1){
    count = 1;
  }else{
    count--;
  }
}


})





// addRows();
