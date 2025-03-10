// alert('Hello Js!');
var button = document.querySelector('#btn-joke');
// console.log(button);

function foo(event)// Функция foo НЕ РАБОТАЕТ!!!
{
    element = event.target;
    element.classList.remove('btn-info');
    element.classList.add('btn-danger');
}
button.addEventListener('click', foo, false);

// AJAX
$( document ).on('click', '#ajax-btn', function(event) {
    console.log('Step 1');
    $.ajax({
                url: '/users/update_token_ajax/',
                success: function (data) {
                    // data - ответ от сервера
                    console.log('Step 2')
                    console.log(data);
                    $('#token').html(data.key); // В теге с id 'token' обновляем содержимое в котором лежит токен по ключу key, полученный из 'data'
                },
            });
});