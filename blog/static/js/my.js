// alert('Hello Js!');
var button = document.querySelector('#btn-joke');
// console.log(button);
function foo(event)
{
    element = event.target;
    element.classList.remove('btn-info');
    element.classList.add('btn-danger');
}
button.addEventListener('click', foo, false);