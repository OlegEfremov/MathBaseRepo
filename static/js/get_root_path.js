function get_root_path(){
    var pathname = window.location.pathname; // Returns path only
    console.log(pathname);
    var levels = pathname.split('/').length - 1
    console.log(levels)
    var root_path = ''
    for (var i=0; i<levels; i++){
        root_path += '../'
    }
    console.log(root_path)
    return root_path
}
