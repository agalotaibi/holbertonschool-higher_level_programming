document.addEventListener('DOMContentLoaded', function () {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';

  fetch(url)
    .then(response => response.json())
    .then(data => {
      const helloElement = document.querySelector('#hello');
      helloElement.textContent = data.hello;
    });
});
