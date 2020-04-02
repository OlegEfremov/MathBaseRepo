function save_filter(data = false){
    var sendData;
	if (data === false){sendData =$('#filter_tree').jstree('get_json', "#");}
	else {sendData = data;}

	sendData = "json="+JSON.stringify(sendData);

	$.ajax({
		type: 'POST',
		url: 'advsearch/save_filter',
		//dataType: "json",
		data: sendData,
		success: function(data){
		}
	});
}

// переменная с html-внутренностью для таблицы с задачами
var table_of_tasks_inner;
//при перезагрузке страницы берет из localstorage предыдущую таблицу с задачами и загружает её
function set_table_of_tasks_inner() {
	table_of_tasks_inner = localStorage.getItem('table_of_tasks_inner');
    MathJax.Hub.Startup.onload();
    document.getElementById('table_of_tasks').innerHTML = '';
    document.getElementById('table_of_tasks').innerHTML = table_of_tasks_inner;
    MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
}

//инициализирует пустую переменную для хранения таблицы задач в localStorage
function populate_table_of_tasks_inner() {
	table_of_tasks_inner = '';
	localStorage.setItem('table_of_tasks_inner', table_of_tasks_inner);
	set_table_of_tasks_inner();
}

// загружает table_of_tasks из localStorage
$(document).ready(function() {
    if (localStorage.getItem('table_of_tasks_inner') === null) {
        populate_table_of_tasks_inner()
    } else {
        set_table_of_tasks_inner()
    }
});

// привязывает к collapse-expand сигнал на сохранение tabke_of_tasks в localStorage
$( document ).ready(function() {
    $(document).on('hidden.bs.collapse', '.collapse', function () {
        send_table_of_tasks_inner_to_storage()
    });
    $(document).on('shown.bs.collapse', '.collapse', function () {
        send_table_of_tasks_inner_to_storage()
    });
});

// записывает значение table_of_tasks в localStorage
function send_table_of_tasks_inner_to_storage(){
    table_of_tasks_inner = document.getElementById('table_of_tasks').innerHTML;
	localStorage.setItem('table_of_tasks_inner', table_of_tasks_inner);
}


// переменная со значениями checkboxes
// привязывает ко всем checkboxes сигнал на изменение - записать новое состояние в localStorage
$(document).ready(function() {
    $(document).on("click", ":checkbox", function () {
        var checkboxValues = JSON.parse(localStorage.getItem('checkboxValues'));
        checkboxValues[this.id] = this.checked;
        localStorage.setItem("checkboxValues", JSON.stringify(checkboxValues));
    });
});


//при перезагрузке страницы берет из localstorage предыдущие checkboxValues и загружает их
function set_checboxValues() {
	checkboxValues =  JSON.parse(localStorage.getItem('checkboxValues'));
    for (var x in checkboxValues){
        if (document.getElementById(x)) {
            document.getElementById(x).checked = checkboxValues[x];
        }
    }
}

//инициализирует пустую переменную для checkboxValues в localStorage
function populate_checboxValues() {
	checkboxValues = {};
	localStorage.setItem('checkboxValues', JSON.stringify(checkboxValues));
	set_checboxValues();
}

// загружает checkboxValues из localStorage
$(document).ready(function() {
    if (localStorage.getItem('checkboxValues') == null) {
        populate_checboxValues();
    } else {
        set_checboxValues();
    }
});


// Показывает задания, соответствующие текущему фильтру
// Привязана к кнопке в Расширенном фильтре
function show_tasks(page_number) {
    get_mathattr_in_filter_json();
    var sendData = $('#filter_tree').jstree('get_json', "#");
    sendData = JSON.stringify(sendData);

    $.ajax({
        url: "show_tasks",
        type: "GET",
        data: {'json_tree': sendData, 'page': page_number, 'per_page': get_per_page()},
        success: function(res) {
            MathJax.Hub.Startup.onload();
            document.getElementById('table_of_tasks').innerHTML = '';
            document.getElementById('table_of_tasks').innerHTML = res;
            MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
            send_table_of_tasks_inner_to_storage();
            set_checboxValues();
        },
        error: function(ts) {
            alert('Error in show_tasks');
        }
    });
    return false;
}



$(document).ready(function() {
    if (localStorage.getItem('per_page') === null) {
        localStorage.setItem('per_page', '1');
        document.getElementById('select_tasks_per_page').selectedIndex = Number(localStorage.getItem('per_page'))-1;
    } else {
        document.getElementById('select_tasks_per_page').selectedIndex = Number(localStorage.getItem('per_page'))-1;
    }
});


function get_per_page(){
    var e = document.getElementById('select_tasks_per_page');
    return e.options[e.selectedIndex].innerHTML;
}


function show_tasks_without_solution(page_number){
    $.ajax({
        url: "show_tasks_without_solution?page="+page_number+'&per_page='+get_per_page(),
        type: "GET",
        success: function(res) {
            MathJax.Hub.Startup.onload();
            document.getElementById('table_of_tasks').innerHTML = '';
            document.getElementById('table_of_tasks').innerHTML = res;
            MathJax.Hub.Queue(["Typeset",MathJax.Hub]);

        },
        error: function(ts) {
            alert('show_tasks_without_solution ERROR');
        }
    });
return false;
}