

Steps:
Scrape and store each of the 8 lists
    Store the 8 lists:
        for each list:
            (movie name, rank for that list)

Run an algorithm with all 8 lists as the input
    (keep the different ranks and corresponding website for each movie)

    --> Output a list of 100 movies ranked according to all 8 lists (weighted equally? or maybe give more weight to experts/critics over audience)

    One algorithm idea:
        initialize a dictionary ((key, value): (movie_name = average rank)) 
        sort dictionary by value (ascending order): keep only the top 100 movies with the lowest average rank
        loop through all of the lists, 

Display all 100 movies as a simple list on a webpage
    onClick or onHover: show the rank on the different websites, and have link to those websites

