// Получает json для дерева отфильтрованных атрибутов
function get_mathattr_in_filter_json() {
    var sendData = $('#filter_tree').jstree('get_json', "#");
    console.log(sendData);
    sendData = JSON.stringify(sendData);
    console.log(sendData);


    $.ajax({
        url: "get_json_all_mathattr_in_filter",
        type: "POST",
        data: {'json_tree': sendData},
        success: function(res) {
            jsonTree = res;

            //if tree has already loaded - reload and refresh
            if ($('#mathattr_in_filter_tree').jstree(true)){
                $('#mathattr_in_filter_tree').jstree(true).settings.core.data = jsonTree;
                $('#mathattr_in_filter_tree').jstree(true).refresh();
            }
            else{
                show_math_attr(jsonTree);
            }

        },
        error: function(ts) {
            alert('Error in show_all_mathattr_in_filter');
        }
    });
    return false;
}

// Дерево всех атрибутов, которые есть в отфильтрованных решениях
// Показывает атрибуты, которые есть в отфильтрованных задачах
function show_math_attr(jsonTree) {
    $(function () {
        $('#mathattr_in_filter_tree').jstree({
            'plugins': ['dnd', 'types'],
            'core': {
                'data': jsonTree,
                'dblclick_toggle': false,
                'multiple': false,
                'expand_selected_onload': false,
                'check_callback': false,
                'themes':{'dots':false}
            },
            "types": {
                "#": {
                    "valid_children": []
                },
                "MathAttr": {
                    "icon": PATH_JSTREE_PIC + "mathattr.png",
                    "valid_children": []
                },
            }
        });
    });
}

