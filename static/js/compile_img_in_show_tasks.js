function compile_img_in_show_tasks(res){
    k = res.replace(/@bimg@/g,'<img src="');
    k = k.replace(/@size=/g,'" height="');
    k = k.replace(/@style=/g,'" style="');
    k = k.replace(/@eimg@/g,'"/>');
    return k
}



