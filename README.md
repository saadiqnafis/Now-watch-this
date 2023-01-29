# Now-watch-this

Inspiration:
“Now, Watch This” was inspired by a constant problem that all college students run into at some point- they have so many choices for entertainment, but barely any time to experience it. With “Now Watch This,” this problem is solved in a manner corresponding to a student’s available free time. This project is under the "Automating for Meaning" track and the "BU Spark: Best College Life Hack" challenge category.

What it does:
“Now Watch This” takes a user’s playlist of “To Watch” YouTube videos and finds two videos from the list that add up to the duration of the user’s free time and sends the videos to the user through an HTML newsletter. For example, if you have one hour of free time, the algorithm will find two half-hour long videos, and generate an HTML newsletter from the videos’ titles, durations, links, and thumbnails.

How we built it:
This project was built around three major components: a login/submission web page, an algorithm that scrapes data from the playlist and finds the two videos from the list, and a newsletter web page constructed from the two videos’ data. Both web pages were constructed using Flask (Python/HTML) and a small bit of JavaScript, and the algorithm was built in Python.

Challenges we ran into:
We ran into several challenges, the first of which being the use of the YouTube API, given that the data is reported through many different subfields of videos, playlist items, and playlists. Finding out how to combine various traits of a video from these formats into our chosen data structure, the Python dictionary with values being lists, was very difficult and required much trial and error. Challenges also arose from implementing the web interface, as implementing a user login became out of our scope due to a lack of understanding of JavaScript or FireBase, which we intended on utilizing, but did not have time to. The same applies for the email segment of the application as the intended use of twil.io was unavailable to free users, and a personal email server is not available to enable a python-based solution.

Accomplishments that we're proud of:
We are proud of the progress we have made in integrating Python into web applications as well as the speed of the algorithm considering the huge amount of items (~2000) in the test case. The data is properly retrieved and formatted for our use case. Using this back-end program in combination with a front-end is a very new concept to our team members and we are proud of being able to implement this combination.

What we learned:
We learned how to utilize Flask and use Python to grab data from the YouTube Data API via Google Cloud. This was a big step as a group given that this was our first time working with dynamic web development as well as the Youtube API and Google Cloud.
