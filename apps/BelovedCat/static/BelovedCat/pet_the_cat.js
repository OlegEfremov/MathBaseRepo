var pet_the_cat_counter = 0;
function pet_the_cat(){
    pet_the_cat_counter += 1;
    console.log(pet_the_cat_counter)
    if (pet_the_cat_counter === 20){
        location.href = '../../beloved_cat/main_page'
    }
}