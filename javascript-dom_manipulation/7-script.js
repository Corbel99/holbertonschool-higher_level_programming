const div = document.querySelector('#list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    for (let i = 0; i < data.results.length; i++) {
      const movie = document.createElement('li');
      movie.textContent = data.results[i].title;
      div.appendChild(movie);
    }
  });
