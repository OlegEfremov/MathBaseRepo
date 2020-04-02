// $(document).ready(function() {
// var password = document.getElementById("id_password1")
//     , confirm_password = document.getElementById("id_password2");
//
// function validatePassword(){
//
//   if(password.value.length < 8) {
//     password.setCustomValidity("Пароль слишком короткий");
//     return false
//   } else {
//     password.setCustomValidity('');
//   }
//
//   if (password.value.match(/^[-\+]?\d+/) === null) {
//     console.log(password.value)
//     password.setCustomValidity("Пароль не может состоять только из цифр");
//     return false
//   } else {
//     password.setCustomValidity('');
//   }
//
//   if(password.value != confirm_password.value) {
//     confirm_password.setCustomValidity("Пароли не совпадают");
//     return false
//   } else {
//     confirm_password.setCustomValidity('');
//   }
// }
//
// password.onchange = validatePassword;
// confirm_password.onkeyup = validatePassword;
// });