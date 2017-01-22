# SlugPark Parking Tracker 

This is an app used to track parking spots at UCSC using class enrollment data, statistical inference, and user location data. Made at [Hack UCSC 2017](www.hackucsc.com). For more information see our corresponding [devpost submission](https://devpost.com/software/slugpark). 

## Team

Name				| Github Account
-----				| --------------
Nicholas Mandel		| nwmandel
Jonathon Allen		| jonath0n
Lucas Tay			| ltay
Neda Ronaghi		| nedaronaghi
Julia Philipp		| nattifftoffe

![team](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/000/464/765/datas/gallery.jpg)

## Special Thanks To

Eric Fultz, for advising on project scope.
Jeffrey Rennie, for advising on implementation.
Emmanuel Leroy, for advising on machine learning, API usage.
Kevin Cameron, for advising on databases and web development.

## Usage

Visit slugpark.com to see the current occupation of the East remote, West remote, and North remote parking lots on the UCSC campus. Click the refresh button under each of the parking lots to receive updated information.

## Discussion
### How we built it
Our working prototype includes the website Slugpark.com that random numbers for three parking lots in form of gages as well as predictions for the whole day based on randomly generated data stored in arrays. The real-time object recognition program YOLO has been tested on parking lot webcam images and the absolute number of cars has been extracted from the analysis. The website UI prototype was built using Javascript, HTML, and CSS. 

### Challenges we ran into
We tried several different approaches to accomplish an accurate and reliable parking tracker. Our initial idea was to base the information about parking lot occupation on user input. The website/ app would provide the user with the option to enter when they entered or left the parking lot or left the parking lot without finding a spot. However, it seemed very unlikely that our users would remember to do that, and it would require all the users to download the application. Therefore, our next approach was to come up with the necessary statistical framework (Rayleigh distribution) to predict and fill in missing data.
In our next pipeline, we considered utilizing geofencing data by having the app/website open in the background of the user’s smartphone. Based on the speed at which the user was moving, we would be able to predict the parking behavior of the user (e.g. if the user is parking if they are driving into the lot and walking out of it). Our main problem with this approach was our lack of knowledge in app development, but extracting geofencing data and making very accurate predictions about the user’s behavior from the web browser is also very limited. Finally, we came up with our last and current approach to use an image recognition software.

### What's next for SlugPark
The next step will be to establish a data structure in which the information received from the real-time object detector YOLO can be stored and read out by our website. Next will be the establishment of the necessary infrastructure (installation of webcams on the parking lots), so SlugPark.com can display actual real-time data. Furthermore, we’re planning to train and develop YOLO further to be able to identify cars on live video footage and to become more and more reliable in identifying cars in full parking lots. Additionally, we would like to extend SlugPark to display the parking lot information in a more detailed way, such as information about each level of a parking garage and information about separate spots being occupied or open (The object recognition software is already able to do that). After that, we want to turn SlugPark into a mobile application so that users do not need to visit the website anymore if they are already on their way to campus or on campus. 
For reliable predictions, we will download, organize, and store class schedules and class sizes as well as store the data that YOLO generates from the webcam images. For that purpose, we will need to develop a plan for secure data storage.
SlugPark can also be applied to other college campuses as well as to city-wide parking systems.


## Support

Please [open an issue](https://github.com/nwmandel/slugpark/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/nwmandel/slugpark/compare/).
