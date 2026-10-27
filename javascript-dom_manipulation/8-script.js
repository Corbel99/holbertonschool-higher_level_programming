document.addEventListener('DOMContentLoaded', function () {
  const div = document.querySelector('#hello');
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      div.textContent = data.hello;
    });
});
