const div = document.querySelector('#update_header');
const header = document.querySelector('header');
div.addEventListener('click', function () {
  header.textContent = 'New Header!!!';
});
