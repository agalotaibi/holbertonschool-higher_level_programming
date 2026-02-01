const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then(response => response.json())
  .then(data => {
    const listMovies = document.querySelector('#list_movies');
    
    data.results.forEach(movie => {
      const newItem = document.createElement('li');
      newItem.textContent = movie.title;
      listMovies.appendChild(newItem);
    });
  });
