import hii from "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl\_lossy,f\_auto,q\_auto/cb26c44b691754d7ca67f67d824e8411"

import hey from "https://shoopy.b-cdn.net/340140/aashirvaad-atta-1702468645457\_SKU-0836\_0.jpg?format=webp"

import hello from "https://images.ctfassets.net/sabbecbbwaz3/75LNk0YBkx43OwldxrGUc6/eaa574a84c4eceef2910dd9b567edd52/VVR\_50g\_Jar\_Closed\_\_1\_.png?w=262"





const prod = \[

    {

        names:"Society Tea",

        price: 42,

        descript:"Hii all",

        rating: 5.7,

        image: "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl\_lossy,f\_auto,q\_auto/cb26c44b691754d7ca67f67d824e8411"

    },

    {

        names:"Aashirvad Aata",

        price: 250,

        descript:"Hello world",

        rating: 6.9,

        image: "https://shoopy.b-cdn.net/340140/aashirvaad-atta-1702468645457\_SKU-0836\_0.jpg?format=webp"

    },

    {

        names:"Vicks Vapour Rub",

        price: 95,

        descript:"Hola amigos",

        rating: 7.8,

        image: "https://images.ctfassets.net/sabbecbbwaz3/75LNk0YBkx43OwldxrGUc6/eaa574a84c4eceef2910dd9b567edd52/VVR\_50g\_Jar\_Closed\_\_1\_.png?w=262"

    },

    {

        names:"Britannia Marie Gold Biscuit",

        price: 240,

        descript:"good day",

        rating: 8.7,

        image: "https://www.bbassets.com/media/uploads/p/l/220244\_9-britannia-marie-gold-biscuits.jpg"

    },

    {

        names:"Fair and Lovely Makeup Cream",

        price: 104,

        descript:"happy sunday",

        rating: 7.2,

        image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9ihoCrL2sLyUModSz063Hj\_PQwp8\_Q8vWYg\&s"

    },

    {

        names:"Kissan Tomato Sauce Ketchup",

        price: 34,

        descript:"thanks a tone, for the sauce",

        rating: 8.0,

        image: "https://5.imimg.com/data5/OW/FI/TP/SELLER-5099161/kissan-tomato-ketchup-500x500.jpg"

    },

    {

        names:"Tira Refined Sunflower Oil",

        price: 600,

        descript:"So very good for health, its a boon indeed",

        rating: 6.8,

        image: "https://5.imimg.com/data5/SELLER/Default/2024/4/408939312/PJ/EU/OL/3572809/5l-tirupati-sunpride-refined-sunflower.png"

    }

];



export default prod;



---



i want to navigate to the next page displaying the movie details,  So that i can display its details,



// const reportWebVitals = onPerfEntry => {

//   if (onPerfEntry \&\& onPerfEntry instanceof Function) {

//     import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {

//       getCLS(onPerfEntry);

//       getFID(onPerfEntry);

//       getFCP(onPerfEntry);

//       getLCP(onPerfEntry);

//       getTTFB(onPerfEntry);

//     });

//   }

// };



// export default reportWebVitals;



import React, {useState, useEffect} from 'react';

import { useNavigate } from 'react-router-dom';



function Home() {

&nbsp;   \*\*const navigate = useNavigate()\*\*

    \*\*// function shifting() {\*\*

    \*\*//     navigate('/')\*\*

    \*\*// }\*\*

    \*\*const  moves = \\\[\*\*


{

&nbsp;   \*\*id: 1,\*\*

    \*\*movie\\\_name: "Dune2",\*\*

    \*\*image\\\_url: "https://4kwallpapers.com/images/wallpapers/dune-2-movie-poster-2732x2732-14717.jpg",\*\*

    \*\*description: "In Dune, Paul Atreides joins forces with Chani and the Fremen to avenge his family's downfall. Faced with a pivotal decision, he balances love and duty to avert a catastrophic destiny.",\*\*

    \*\*genre: "Action/Fantasy/Sci-Fi",\*\*

    \*\*censor: "U/A",\*\*

    \*\*director: "Denis Villeneuve",\*\*

    \*\*rating: "8.5/10",\*\*

    \*\*cast: \\\[\*\*

      \*\*"Timothée Chalamet",\*\*

      \*\*"Rebecca Ferguson",\*\*

      \*\*"Zendaya"\*\*

    \*\*]\*\*


},

{

&nbsp;   \*\*id: 2,\*\*

    \*\*movie\\\_name: "Oppenheimer",\*\*

    \*\*image\\\_url: "https://images4.alphacoders.com/132/1323605.jpeg",\*\*

    \*\*description: "Oppenheimer follows the life of J. Robert Oppenheimer, the physicist who led the Manhattan Project, as he grapples with the moral and ethical implications of creating the atomic bomb, ultimately shaping the course of modern history.",\*\*

    \*\*genre: "Biographical/Drama",\*\*

    \*\*censor: "U",\*\*

    \*\*director: "Christopher Nolan",\*\*

    \*\*rating: "8.3/10",\*\*

    \*\*cast: \\\[\*\*

      \*\*"Cillian murphy",\*\*

      \*\*"Robert Downey Jr.",\*\*

      \*\*"Emily Blunt"\*\*

    \*\*]\*\*


},

{

&nbsp;   \*\*id: 3,\*\*

    \*\*movie\\\_name: "OG",\*\*

    \*\*image\\\_url: "https://moviegalleri.net/wp-content/uploads/2024/02/Pawan-Kalyan-OG-Movie-Release-Date-on-September-27th-Poster-HD.jpg",\*\*

    \*\*description: "Ojas Gambheera, a feared gangster, returns to Mumbai after a decade in exile, determined to reclaim his power and finish what he started.",\*\*

    \*\*genre: "Action/Drama",\*\*

    \*\*censor: "U/A",\*\*

    \*\*director: "Sujeeth",\*\*

    \*\*rating: "6.5/10",\*\*

    \*\*cast: \\\[\*\*

      \*\*"Pawan Kalyan",\*\*

      \*\*"Emraan Hashmi",\*\*

      \*\*"Priyanka Mohan"\*\*

    \*\*]\*\*


},

{

&nbsp;   \*\*id: 4,\*\*

    \*\*movie\\\_name: "Baahubali: The Conclusion",\*\*

    \*\*image\\\_url: "https://e1.pxfuel.com/desktop-wallpaper/875/703/desktop-wallpaper-prabhas-baahubali-the-conclusion-movie-ultra-posters-baahubali-the-beginning.jpg",\*\*

    \*\*description: "The second installment of the epic Baahubali saga.",\*\*

    \*\*genre: "Action/Drama",\*\*

    \*\*censor: "U/A",\*\*

    \*\*director: "S.S. Rajamouli",\*\*

    \*\*rating: "8.2/10",\*\*

    \*\*cast: \\\[\*\*

      \*\*"Prabhas",\*\*

      \*\*"Rana Daggubati",\*\*

      \*\*"Anushka Shetty"\*\*

    \*\*]\*\*


},

{

&nbsp;   \*\*id: 5,\*\*

    \*\*movie\\\_name: "Interstellar",\*\*

    \*\*image\\\_url: "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@.\\\_V1\\\_.jpg",\*\*

    \*\*description: "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",\*\*

    \*\*genre: "Sci-Fi/Drama",\*\*

    \*\*censor: "PG-13",\*\*

    \*\*director: "Christopher Nolan",\*\*

    \*\*rating: "8.7/10",\*\*

    \*\*cast: \\\[\*\*

      \*\*"Matthew McConaughey",\*\*

      \*\*"Anne Hathaway",\*\*

      \*\*"Jessica Chastain"\*\*

    \*\*]\*\*


},

{

&nbsp;   \*\*id: 6,\*\*

    \*\*movie\\\_name: "Arjun Reddy",\*\*

    \*\*image\\\_url: "https://i.pinimg.com/originals/9d/84/5e/9d845e298cb90b177bf008f28abb1030.jpg",\*\*

    \*\*description: "A brilliant medical student spirals into self-destruction after an intense breakup.",\*\*

    \*\*genre: "Drama/Romance",\*\*

    \*\*censor: "A",\*\*

    \*\*director: "Sandeep Reddy Vanga",\*\*

    \*\*rating: "7.9/10",\*\*

    \*\*cast: \\\[\*\*

      \*\*"Vijay Deverakonda",\*\*

      \*\*"Shalini Pandey"\*\*

    \*\*]\*\*


},

{

&nbsp;   \*\*\\\_\\\_v: 0,\*\*

    \*\*id: 7,\*\*

    \*\*movie\\\_name: "The Dark Knight",\*\*

    \*\*image\\\_url: "https://i.pinimg.com/originals/41/83/28/41832844a09a83213c8a29fc577ca7c8.jpg",\*\*

    \*\*description: "Batman faces off against the Joker, a criminal mastermind set on wreaking havoc on Gotham City.",\*\*

    \*\*genre: "Action/Crime/Drama",\*\*

    \*\*censor: "PG-13",\*\*

    \*\*director: "Christopher Nolan",\*\*

    \*\*rating: "9/10",\*\*

    \*\*cast: \\\[\*\*

      \*\*"Christian Bale",\*\*

      \*\*"Heath Ledger",\*\*

      \*\*"Aaron Eckhart"\*\*

    \*\*]\*\*


},

{

&nbsp;   \*\*\\\_\\\_v: 0,\*\*

    \*\*id: 8,\*\*

    \*\*movie\\\_name: "Rangasthalam",\*\*

    \*\*image\\\_url: "https://e0.pxfuel.com/wallpapers/814/824/desktop-wallpaper-ram-charan-s-rangasthalam-is-first-non-baahubali-telugu-film-to-achieve-it-tollywood-thumbnail.jpg",\*\*

    \*\*description: "A man born with dwarfism sets out to prove himself in a small village ruled by a tyrannical president.",\*\*

    \*\*genre: "Drama/Action",\*\*

    \*\*censor: "U/A",\*\*

    \*\*director: "Sukumar",\*\*

    \*\*rating: "8.2/10",\*\*

    \*\*cast: \\\[\*\*

      \*\*"Ram Charan",\*\*

      \*\*"Samantha Akkineni"\*\*

    \*\*]\*\*


},

{

&nbsp;   \*\*\\\_\\\_v: 0,\*\*

    \*\*id: 9,\*\*

    \*\*movie\\\_name: "Inception",\*\*

    \*\*image\\\_url: "https://c4.wallpaperflare.com/wallpaper/764/590/391/inception-leonardo-dicaprio-movie-posters-2400x3500-entertainment-movies-hd-art-wallpaper-preview.jpg",\*\*

    \*\*description: "A thief who enters the dreams of others to steal their secrets must plant an idea in someone's mind.",\*\*

    \*\*genre: "Action/Sci-Fi/Thriller",\*\*

    \*\*censor: "PG-13",\*\*

    \*\*director: "Christopher Nolan",\*\*

    \*\*rating: "8.8/10",\*\*

    \*\*cast: \\\[\*\*

      \*\*"Leonardo DiCaprio",\*\*

      \*\*"Joseph Gordon-Levitt",\*\*

      \*\*"Ellen Page"\*\*

    \*\*]\*\*


},

{

&nbsp;   \*\*\\\_\\\_v: 0,\*\*

    \*\*id: 10,\*\*

    \*\*movie\\\_name: "Avatar",\*\*

    \*\*image\\\_url: "https://i.pinimg.com/736x/8b/2f/a6/8b2fa6fb94810cd0d335b479896f7fc8.jpg",\*\*

    \*\*description: "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",\*\*

    \*\*genre: "Action/Adventure/Fantasy",\*\*

    \*\*censor: "PG-13",\*\*

    \*\*director: "James Cameron",\*\*

    \*\*rating: "7.9/10",\*\*

    \*\*cast: \\\[\*\*

      \*\*"Sam Worthington",\*\*

      \*\*"Zoe Saldana",\*\*

      \*\*"Sigourney Weaver"\*\*

    \*\*]\*\*


}

]

console.log(moves)



return (

&nbsp;   \*\*<div>\*\*

        \*\*<h1>List of movies here:</h1>\*\*

        \*\*{<ul>\*\*

            \*\*{\*\*

                \*\*moves.map(function (i) {\*\*

                  \*\*return  <li key={i.id}style={{ listStyleType: "none"}}><a href={`/${i.id}`} style={{color: "goldenrod"}}>{i.movie\\\_name}</a> has a rating of {i.rating}</li>\*\*

                \*\*})\*\*

            \*\*}\*\*

        \*\*</ul>}\*\*

        \*\*<br/>\*\*

        \*\*<main>\*\*

            \*\*<p>Happy Day</p>\*\*

            \*\*<pre>Happy ThursDay</pre>\*\*

            \*\*<p>Good Afternooon</p>\*\*

          \*\*</main>\*\*

    \*\*</div>\*\*


)

}



export default Home

//  has a rating of {i.rating}





and to extract the details of the each movie, the code is written below:





import React from 'react'



function Dates(props) {

&nbsp;   \*\*console.log(props)\*\*


return (

&nbsp;   \*\*<div>Dates</div>\*\*


)

}



export default Dates





\#include <iostream>

\#include <string>

\#include <unordered\_map>



using namespace std;



int user\_logic(const string\& s) {

    unordered\_map<char, int> freq;

 

    // Count frequency of each character

    for (char ch : s) {

        freq\[ch]++;

    }



    int length = 0;

    bool oddFound = false;



    for (auto\& pair : freq) {

        int count = pair.second;

        if (count % 2 == 0) {

            length += count;

        } else {

            length += count - 1;  // Use even part

            oddFound = true;

        }

    }



    // One odd character can be used in the center

    if (oddFound) {

        length += 1;

    }



    return length;

}



int main() {

    string s;

    cin >> s;



    int result = user\_logic(s);

    cout << result << endl;



    return 0;

}





int freq\[128] = {0}; // Covers all uppercase and lowercase letters



    // Step 1: Count frequency of each character

    for (char ch : s) {

        freq\[ch]++;

    }



    int length = 0;

    bool hasOdd = false;



    // Step 2: Use counts to calculate max palindrome length

    for (int i = 0; i < 128; ++i) {

        if (freq\[i] % 2 == 0) {

            length += freq\[i]; // Use all

        } else {

            length += freq\[i] - 1; // Use one less (even part)

            hasOdd = true;

        }

    }



    // Step 3: If there was any odd count, we can add one center character

    if (hasOdd) {

        length += 1;

    }



    return length;





---



   int freq\[128] = {0};

    int length = 0;

    bool hasOdd = false;



    for (char ch : s) {

        freq\[ch]++;

    }



    for (int i = 0; i < 128; ++i) {

        if (freq\[i] % 2 == 0) {

            length += freq\[i];

        } else {

            length += freq\[i] - 1;

            hasOdd = true;

        }

    }



    if (hasOdd) { length += 1; }

    return length;

