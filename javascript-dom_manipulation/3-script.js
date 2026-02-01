const toggleHeader = document.querySelector('#toggle_header');
const header = document.querySelector('header');

toggleHeader.addEventListener('click', function () {
  header.classList.toggle('red');
  header.classList.toggle('green');
});
