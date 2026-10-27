const div = document.querySelector('#add_item');
const list = document.querySelector('.my_list');
div.addEventListener('click', function () {
  const item = document.createElement('li');
  item.textContent = 'Item';
  list.appendChild(item);
});
