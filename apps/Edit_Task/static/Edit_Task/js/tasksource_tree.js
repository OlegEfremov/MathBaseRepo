//tasksource_tree
    $(function () {
        $('#tasksource_tree').jstree({
            'plugins': ['dnd', 'types', 'deleteNode'],
            'deleteNode': function (node) {
                var ref = $('#tasksource_tree').jstree(true);
                ref.delete_node(node);

                var node_dbType = node['a_attr']['dbType'];
                var node_dbID = node['a_attr']['dbID'];

                var sendData = 'node_dbType=' + node_dbType;
                sendData += '&node_dbID=' + node_dbID;
                sendData += '&taskid=' + taskid;

                $.ajax({
                    type: 'POST',
                    url: 'delete_tasknumber_from_task',
                    data: sendData,
                    success: function (data) {
                        show_tasks(taskid)
                    }
                });

            },
            'core': {
                'check_callback': function (operation, node, node_parent, node_position, more) {
                    if (operation == 'copy_node') {
                        current_dbID = node['a_attr']['dbID'];
                        var ref = $('#tasksource_tree').jstree(true);
                        var i, j, child;
                        for (i = 0; i < node_parent['children'].length; i++) {
                            child_id = node_parent['children'][i];
                            child = ref.get_node(child_id);
                            dbID = child['a_attr']['dbID'];
                            if (dbID === current_dbID) {
                                return false
                            }
                        }
                    }

                    if (more) {
                        if (more.is_multi) {
                            // prevent move from source catalog to task - only copy
                            more.origin.settings.dnd.always_copy = true;
                        } else {
                            // prevent self-dnd in tasksource_tree
                            return false
                        }
                    }
                    return true
                },
                'data': {
                    "url": "tasksource_tree/" + taskid,
                    "dataType": "json" // needed only if you do not supply JSON headers
                },
                'themes': {
                    'dots': false
                },
                'dblclick_toggle': false
            },
            "types": {
                "#": {
                    "valid_children": []
                },
                "Task": {
                    "icon": "fas fa-question-circle",
                    "valid_children": ['TaskNumber']
                },
                "TaskNumber": {
                    "icon": 'fas fa-circle fa-xs',
                    "valid_children": []
                }
            }
        })
            .bind('copy_node.jstree', function (e, data) {
                var refsource = $('#source_tree').jstree(true);

                var ref = $('#tasksource_tree').jstree(true);

                var newname = refsource.get_node(data.old_parent).text;
                $("#tasksource_tree").jstree('rename_node', data.node, newname + ', ' + data.node.text);

                var nodeNode = data.node;
                var node_dbType = nodeNode['a_attr']['dbType'];
                var node_dbID = nodeNode['a_attr']['dbID'];

                var sendData = 'node_dbType=' + node_dbType;
                sendData += '&node_dbID=' + node_dbID;
                sendData += '&taskid=' + taskid;


                $.ajax({
                    type: 'POST',
                    url: 'add_task_number_to_task',
                    data: sendData,
                    success: function (data) {
                        show_tasks(taskid)
                    }
                });

            });
    });


