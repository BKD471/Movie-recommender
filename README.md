# Movie-recommender
<a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/1c502d149c62da4bd1055404c29743154b7bdd316aab0d466025751c2df7e163/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e382d626c756576696f6c6574"><img src="https://camo.githubusercontent.com/1c502d149c62da4bd1055404c29743154b7bdd316aab0d466025751c2df7e163/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e382d626c756576696f6c6574" alt="Python" data-canonical-src="https://img.shields.io/badge/Python-3.8-blueviolet" style="max-width:100%;"></a>
<a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/a8256d965b9ade271a5aa6fffecc3b4564a0ede3c8a77287b1de5310fece95da/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4672616d65776f726b2d466c61736b2d726564"><img src="https://camo.githubusercontent.com/a8256d965b9ade271a5aa6fffecc3b4564a0ede3c8a77287b1de5310fece95da/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4672616d65776f726b2d466c61736b2d726564" alt="Framework" data-canonical-src="https://img.shields.io/badge/Framework-Flask-red" style="max-width:100%;"></a>
<a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/0b62a236c961e03fda7bc31de5e286161319fed1b9bfa162e825ad9d7e059e4f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f46726f6e74656e642d48544d4c2f4353532f4a532d677265656e"><img src="https://camo.githubusercontent.com/0b62a236c961e03fda7bc31de5e286161319fed1b9bfa162e825ad9d7e059e4f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f46726f6e74656e642d48544d4c2f4353532f4a532d677265656e" alt="Frontend" data-canonical-src="https://img.shields.io/badge/Frontend-HTML/CSS/JS-green" style="max-width:100%;"></a>
<a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/8785a2cfa54ec466fe1d65c77a0aa7495f2b9188c4c46e50588f3bd65641dcd8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4150492d544d44422d666362613033"><img src="https://camo.githubusercontent.com/8785a2cfa54ec466fe1d65c77a0aa7495f2b9188c4c46e50588f3bd65641dcd8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4150492d544d44422d666362613033" alt="API" data-canonical-src="https://img.shields.io/badge/API-TMDB-fcba03" style="max-width:100%;"></a>
<br>
This app shows you all the details regarding the cast and crew information ,genres of all hollywood movies from 1916 to 2020.
Besides giving you all the details, it recommends you several movies based on your search 
and performs sentiment analysis on the viewers comments which shows the acceptance/disliking of that movie among the audience
<h1>App is hosted at<h1>
<ul><li><a href='https://movieprime.herokuapp.com/' target="_blank">Click  here to see the App in action</a></li></ul>

<h1>How to run this project</h1>
<ol>
<li>Clone this repository to your local machine.</li>
<li>Install all the libraries mentioned in the requirements.txt file</li>
<li>Get your API key from https://www.themoviedb.org/.</li>
<ul>
  <p>Create an account in https://www.themoviedb.org/, click on the API link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your API sidebar once your request is approved.</p>
</ul>
<li>Replace YOUR_API_KEY where it is needed in static/recommend.js file.</li>
<li>Open your terminal/command prompt from your project directory and run the file by typing pythhon app.py  nd then enter</li>
<li>Go to your browser and type the adrress of your ip i.e localhost with port no in which it is running....like http://127.0.0.1:5000/  </li>
</ol>

<h1>Similarity metric used here for recommendation is <b>Similarity Score</b></h1>
<ul><p>More similar the movies are , higher will be the similarity score</p></ul>

<h1>Datasets used</h1>
<ul>
 <li><a href='https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset' >imdb 5000 movies dataset</a></li>
 <li><a href='https://en.wikipedia.org/wiki/List_of_American_films_of_2016' >wikipedia list of all american films in 2016</a></li>
<li><a href='https://en.wikipedia.org/wiki/List_of_American_films_of_2017' >wikipedia list of all american films in 2017</a></li>
<li><a href='https://en.wikipedia.org/wiki/List_of_American_films_of_2018' >wikipedia list of all american films in 2018</a></li>
<li><a href='https://en.wikipedia.org/wiki/List_of_American_films_of_2019' >wikipedia list of all american films in 2019</a></li>
<li><a href='https://en.wikipedia.org/wiki/List_of_American_films_of_2020' >wikipedia list of all american films in 2020</a></li>
</ul>
