# Flight Search Engine
Project 
#### Description:
This program is meant to retrive information regarding flights and is built primarily around 'Amadeus' library (https://github.com/amadeus4dev/amadeus-python) and API.

On start, you will be offered 2 options: 'anyl' and 'specific'.
>**'anyl'** will prompt the user to input the origin airport IATA code (airport code). Program will then use the API to retrive data regarding all the cheapest direct flights from the airport provided

>**'specific'** will prompt the user to input IATA code of origin and destination and to specify the date for the flights in YYYY-MM-DD format.

Inside the function "get_airport_details", IATA codes are being checked trough the 'airportsdata' module and if the code is recognized, the full name, country and city for that airport is going to be returned.

The 'specific' function uses 'time_conversion' function in order to get easy to read format for the duration of the flight.

### Global variables:
For the purpose of this project, the API was used and integrated directly into the program.
The program starts setting up 2 global variables: the API (which was used in both main functions) and the airports dictionary.
The only reason I have left the airports dictionary as a global 'dictionary' if you will, is that the program seemed faster to already have it loaded, rather than loading every time it would need to fetch the info.

### Functions:
#### main
Contains a short explanation of the program and then prompts the user to input their choice.
The choice will run trough a match case statement which will take the next inputs of the user and run them as arguments for '***anyl***' or '***specific***' functions.

#### anyl
This funtion is meant to give details regarding all the direct flights from a 'origin' location.
It takes only argument which is used to call a function from the 'amadeus' module using the API that was set in the begining of the program.
From that the program enters in a 'for' loop and gets all the details for each flight found.
The details are then placed in a template and displayed to the user.
Lastly if the function ends successfully, it will return True, or False if something will go wrong. (this is used for the test.py)

#### specific
This function is a bit different from the previous one, since it can retrive multiple itineraries for each offer.
It is meant to give you the details of all the flights between A and B on a specific date.
That means that there might be 2 or more flights / offer due to stop overs.
Same as before, program will enter in some 'for' loops, some of them being nested, due to how complicated the data / dictionary retrived was.
The date and time was formatted in a more readable way with a 'try except' block.
At the end, same as with ***anyl*** function, we have return True / False for the test.py

#### time_conversion
Here the conversion of the duration of the flight is made.
The duration retrived from the ***response.data*** whithin the ***specific*** function comes in a 'PTxHyM' where x and y are the hour and minute.
In order to achieve this a RegEx function is being used.

#### get_airports_details
This function is used in both "anyl" and "specific" functions in order to retrive more information regarding the airports names and locations.
It uses the 'airportsdata' module and retrives the data from the dictionary that was declared as global variable at the beginning of the program.

### Extras
Initially Google Flight API was considered but it was discontinued.
Flight API by Amadeus became the next best choice as they offered a free solution with their 'Amadeus for Developers' platform.

Aviationstack API was the first choice before 'airportsdata', but somehow I did not manage to make it work.
I have reached out to their support, but, due to lack of patience, I tried to find a replacement, which in turn I guess it made the program faster since it didn't need to retrive data from 2 APIs.

The "anyl" function was inially named "any" until I realized python has a function named "any()".

Funnily enough, the beginning this program was supposed to be something entirely different.
I believe during the 4th week of the course, I've started developing an app that to this day I am using at my workplace.
As I learned more and more, I've kept adding functionality to it.
The issue arised that I never created functions for it, but just code everything straight.
In the end I decided to instead opt for an entirely different project, rather than re-write something.
I learned so much more and had a lot more fun with this.
I believe there is nothing more satisfying than not seeing an error popping after a few hours of debugging.
