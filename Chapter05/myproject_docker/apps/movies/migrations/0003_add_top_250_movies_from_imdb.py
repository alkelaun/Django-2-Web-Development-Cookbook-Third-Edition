from django.db import migrations


def insert(apps, schema_editor):
    Movie = apps.get_model("movies", "Movie")
    db_alias = schema_editor.connection.alias
    Movie.objects.using(db_alias).bulk_create([
        Movie(**data) for data in movie_data
    ])


def delete(apps, schema_editor):
    Movie = apps.get_model("movies", "Movie")
    db_alias = schema_editor.connection.alias
    for data in movie_data:
        matched = Movie.objects.using(db_alias).filter(**data).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('movies', '0002_auto_20180920_0458'),
    ]

    operations = [
        migrations.RunPython(insert, delete)
    ]


movie_data = [
    {"rank": 1, "title": "The Shawshank Redemption", "release_year": 1994, "rating": 9.2},
    {"rank": 2, "title": "The Godfather", "release_year": 1972, "rating": 9.2},
    {"rank": 3, "title": "The Godfather: Part II", "release_year": 1974, "rating": 9},
    {"rank": 4, "title": "The Dark Knight", "release_year": 2008, "rating": 9},
    {"rank": 5, "title": "12 Angry Men", "release_year": 1957, "rating": 8.9},
    {"rank": 6, "title": "Schindler's List", "release_year": 1993, "rating": 8.9},
    {"rank": 7, "title": "The Lord of the Rings: The Return of the King", "release_year": 2003, "rating": 8.9},
    {"rank": 8, "title": "Pulp Fiction", "release_year": 1994, "rating": 8.9},
    {"rank": 9, "title": "The Good, the Bad and the Ugly", "release_year": 1966, "rating": 8.8},
    {"rank": 10, "title": "Fight Club", "release_year": 1999, "rating": 8.8},
    {"rank": 11, "title": "The Lord of the Rings: The Fellowship of the Ring", "release_year": 2001, "rating": 8.8},
    {"rank": 12, "title": "Forrest Gump", "release_year": 1994, "rating": 8.7},
    {"rank": 13, "title": "Star Wars: Episode V - The Empire Strikes Back", "release_year": 1980, "rating": 8.7},
    {"rank": 14, "title": "Inception", "release_year": 2010, "rating": 8.7},
    {"rank": 15, "title": "The Lord of the Rings: The Two Towers", "release_year": 2002, "rating": 8.7},
    {"rank": 16, "title": "One Flew Over the Cuckoo's Nest", "release_year": 1975, "rating": 8.7},
    {"rank": 17, "title": "Goodfellas", "release_year": 1990, "rating": 8.7},
    {"rank": 18, "title": "The Matrix", "release_year": 1999, "rating": 8.6},
    {"rank": 19, "title": "Seven Samurai", "release_year": 1954, "rating": 8.6},
    {"rank": 20, "title": "Star Wars: Episode IV - A New Hope", "release_year": 1977, "rating": 8.6},
    {"rank": 21, "title": "City of God", "release_year": 2002, "rating": 8.6},
    {"rank": 22, "title": "Se7en", "release_year": 1995, "rating": 8.6},
    {"rank": 23, "title": "The Silence of the Lambs", "release_year": 1991, "rating": 8.6},
    {"rank": 24, "title": "It's a Wonderful Life", "release_year": 1946, "rating": 8.6},
    {"rank": 25, "title": "Life Is Beautiful", "release_year": 1997, "rating": 8.6},
    {"rank": 26, "title": "The Usual Suspects", "release_year": 1995, "rating": 8.6},
    {"rank": 27, "title": "Spirited Away", "release_year": 2001, "rating": 8.5},
    {"rank": 28, "title": "Léon", "release_year": 1994, "rating": 8.5},
    {"rank": 29, "title": "Saving Private Ryan", "release_year": 1998, "rating": 8.5},
    {"rank": 30, "title": "Interstellar", "release_year": 2014, "rating": 8.5},
    {"rank": 31, "title": "The Green Mile", "release_year": 1999, "rating": 8.5},
    {"rank": 32, "title": "American History X", "release_year": 1998, "rating": 8.5},
    {"rank": 33, "title": "Psycho", "release_year": 1960, "rating": 8.5},
    {"rank": 34, "title": "Once Upon a Time in the West", "release_year": 1968, "rating": 8.5},
    {"rank": 35, "title": "City Lights", "release_year": 1931, "rating": 8.5},
    {"rank": 36, "title": "Casablanca", "release_year": 1942, "rating": 8.5},
    {"rank": 37, "title": "Untouchable", "release_year": 2011, "rating": 8.5},
    {"rank": 38, "title": "Modern Times", "release_year": 1936, "rating": 8.5},
    {"rank": 39, "title": "The Pianist", "release_year": 2002, "rating": 8.5},
    {"rank": 40, "title": "The Departed", "release_year": 2006, "rating": 8.5},
    {"rank": 41, "title": "Raiders of the Lost Ark", "release_year": 1981, "rating": 8.5},
    {"rank": 42, "title": "Terminator 2: Judgment Day", "release_year": 1991, "rating": 8.5},
    {"rank": 43, "title": "Rear Window", "release_year": 1954, "rating": 8.5},
    {"rank": 44, "title": "Back to the Future", "release_year": 1985, "rating": 8.5},
    {"rank": 45, "title": "Whiplash", "release_year": 2014, "rating": 8.5},
    {"rank": 46, "title": "Gladiator", "release_year": 2000, "rating": 8.5},
    {"rank": 47, "title": "The Lion King", "release_year": 1994, "rating": 8.5},
    {"rank": 48, "title": "The Prestige", "release_year": 2006, "rating": 8.5},
    {"rank": 49, "title": "Memento", "release_year": 2000, "rating": 8.4},
    {"rank": 50, "title": "Apocalypse Now", "release_year": 1979, "rating": 8.4},
    {"rank": 51, "title": "Alien", "release_year": 1979, "rating": 8.4},
    {"rank": 52, "title": "The Great Dictator", "release_year": 1940, "rating": 8.4},
    {"rank": 53, "title": "Cinema Paradiso", "release_year": 1988, "rating": 8.4},
    {"rank": 54, "title": "Sunset Boulevard", "release_year": 1950, "rating": 8.4},
    {"rank": 55, "title": "Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb", "release_year": 1964,
     "rating": 8.4}, {"rank": 56, "title": "Grave of the Fireflies", "release_year": 1988, "rating": 8.4},
    {"rank": 57, "title": "The Lives of Others", "release_year": 2006, "rating": 8.4},
    {"rank": 58, "title": "Coco", "release_year": 2017, "rating": 8.4},
    {"rank": 59, "title": "Paths of Glory", "release_year": 1957, "rating": 8.4},
    {"rank": 60, "title": "The Shining", "release_year": 1980, "rating": 8.4},
    {"rank": 61, "title": "Django Unchained", "release_year": 2012, "rating": 8.4},
    {"rank": 62, "title": "WALL·E", "release_year": 2008, "rating": 8.4},
    {"rank": 63, "title": "Princess Mononoke", "release_year": 1997, "rating": 8.4},
    {"rank": 64, "title": "American Beauty", "release_year": 1999, "rating": 8.4},
    {"rank": 65, "title": "The Dark Knight Rises", "release_year": 2012, "rating": 8.4},
    {"rank": 66, "title": "Witness for the Prosecution", "release_year": 1957, "rating": 8.4},
    {"rank": 67, "title": "Oldboy", "release_year": 2003, "rating": 8.4},
    {"rank": 68, "title": "Aliens", "release_year": 1986, "rating": 8.4},
    {"rank": 69, "title": "Once Upon a Time in America", "release_year": 1984, "rating": 8.3},
    {"rank": 70, "title": "Das Boot", "release_year": 1981, "rating": 8.3},
    {"rank": 71, "title": "Citizen Kane", "release_year": 1941, "rating": 8.3},
    {"rank": 72, "title": "North by Northwest", "release_year": 1959, "rating": 8.3},
    {"rank": 73, "title": "Vertigo", "release_year": 1958, "rating": 8.3},
    {"rank": 74, "title": "Braveheart", "release_year": 1995, "rating": 8.3},
    {"rank": 75, "title": "Reservoir Dogs", "release_year": 1992, "rating": 8.3},
    {"rank": 76, "title": "Star Wars: Episode VI - Return of the Jedi", "release_year": 1983, "rating": 8.3},
    {"rank": 77, "title": "Dangal", "release_year": 2016, "rating": 8.3},
    {"rank": 78, "title": "M", "release_year": 1931, "rating": 8.3},
    {"rank": 79, "title": "Your Name", "release_year": 2016, "rating": 8.3},
    {"rank": 80, "title": "Requiem for a Dream", "release_year": 2000, "rating": 8.3},
    {"rank": 81, "title": "Like Stars on Earth", "release_year": 2007, "rating": 8.3},
    {"rank": 82, "title": "Amadeus", "release_year": 1984, "rating": 8.3},
    {"rank": 83, "title": "Amélie", "release_year": 2001, "rating": 8.3},
    {"rank": 84, "title": "A Clockwork Orange", "release_year": 1971, "rating": 8.3},
    {"rank": 85, "title": "Lawrence of Arabia", "release_year": 1962, "rating": 8.3},
    {"rank": 86, "title": "Eternal Sunshine of the Spotless Mind", "release_year": 2004, "rating": 8.3},
    {"rank": 87, "title": "Double Indemnity", "release_year": 1944, "rating": 8.3},
    {"rank": 88, "title": "Taxi Driver", "release_year": 1976, "rating": 8.3},
    {"rank": 89, "title": "Singin' in the Rain", "release_year": 1952, "rating": 8.3},
    {"rank": 90, "title": "2001: A Space Odyssey", "release_year": 1968, "rating": 8.3},
    {"rank": 91, "title": "3 Idiots", "release_year": 2009, "rating": 8.3},
    {"rank": 92, "title": "To Kill a Mockingbird", "release_year": 1962, "rating": 8.3},
    {"rank": 93, "title": "Toy Story", "release_year": 1995, "rating": 8.3},
    {"rank": 94, "title": "Full Metal Jacket", "release_year": 1987, "rating": 8.3},
    {"rank": 95, "title": "Inglourious Basterds", "release_year": 2009, "rating": 8.3},
    {"rank": 96, "title": "The Sting", "release_year": 1973, "rating": 8.3},
    {"rank": 97, "title": "Bicycle Thieves", "release_year": 1948, "rating": 8.3},
    {"rank": 98, "title": "The Kid", "release_year": 1921, "rating": 8.3},
    {"rank": 99, "title": "Toy Story 3", "release_year": 2010, "rating": 8.3},
    {"rank": 100, "title": "Snatch", "release_year": 2000, "rating": 8.3},
    {"rank": 101, "title": "Good Will Hunting", "release_year": 1997, "rating": 8.3},
    {"rank": 102, "title": "The Hunt", "release_year": 2012, "rating": 8.3},
    {"rank": 103, "title": "Monty Python and the Holy Grail", "release_year": 1975, "rating": 8.3},
    {"rank": 104, "title": "For a Few Dollars More", "release_year": 1965, "rating": 8.3},
    {"rank": 105, "title": "Scarface", "release_year": 1983, "rating": 8.2},
    {"rank": 106, "title": "L.A. Confidential", "release_year": 1997, "rating": 8.2},
    {"rank": 107, "title": "The Apartment", "release_year": 1960, "rating": 8.2},
    {"rank": 108, "title": "Metropolis", "release_year": 1927, "rating": 8.2},
    {"rank": 109, "title": "A Separation", "release_year": 2011, "rating": 8.2},
    {"rank": 110, "title": "Rashomon", "release_year": 1950, "rating": 8.2},
    {"rank": 111, "title": "Indiana Jones and the Last Crusade", "release_year": 1989, "rating": 8.2},
    {"rank": 112, "title": "Up", "release_year": 2009, "rating": 8.2},
    {"rank": 113, "title": "Yojimbo", "release_year": 1961, "rating": 8.2},
    {"rank": 114, "title": "All About Eve", "release_year": 1950, "rating": 8.2},
    {"rank": 115, "title": "Batman Begins", "release_year": 2005, "rating": 8.2},
    {"rank": 116, "title": "Some Like It Hot", "release_year": 1959, "rating": 8.2},
    {"rank": 117, "title": "Unforgiven", "release_year": 1992, "rating": 8.2},
    {"rank": 118, "title": "The Treasure of the Sierra Madre", "release_year": 1948, "rating": 8.2},
    {"rank": 119, "title": "My Father and My Son", "release_year": 2005, "rating": 8.2},
    {"rank": 120, "title": "Downfall", "release_year": 2004, "rating": 8.2},
    {"rank": 121, "title": "Die Hard", "release_year": 1988, "rating": 8.2},
    {"rank": 122, "title": "Heat", "release_year": 1995, "rating": 8.2},
    {"rank": 123, "title": "Raging Bull", "release_year": 1980, "rating": 8.2},
    {"rank": 124, "title": "Ikiru", "release_year": 1952, "rating": 8.2},
    {"rank": 125, "title": "Three Billboards Outside Ebbing, Missouri", "release_year": 2017, "rating": 8.2},
    {"rank": 126, "title": "The Great Escape", "release_year": 1963, "rating": 8.2},
    {"rank": 127, "title": "The Third Man", "release_year": 1949, "rating": 8.2},
    {"rank": 128, "title": "Children of Heaven", "release_year": 1997, "rating": 8.2},
    {"rank": 129, "title": "Chinatown", "release_year": 1974, "rating": 8.2},
    {"rank": 130, "title": "Pan's Labyrinth", "release_year": 2006, "rating": 8.2},
    {"rank": 131, "title": "Incendies", "release_year": 2010, "rating": 8.2},
    {"rank": 132, "title": "My Neighbor Totoro", "release_year": 1988, "rating": 8.2},
    {"rank": 133, "title": "Ran", "release_year": 1985, "rating": 8.2},
    {"rank": 134, "title": "Judgment at Nuremberg", "release_year": 1961, "rating": 8.2},
    {"rank": 135, "title": "The Secret in Their Eyes", "release_year": 2009, "rating": 8.2},
    {"rank": 136, "title": "The Gold Rush", "release_year": 1925, "rating": 8.2},
    {"rank": 137, "title": "Howl's Moving Castle", "release_year": 2004, "rating": 8.2},
    {"rank": 138, "title": "The Bridge on the River Kwai", "release_year": 1957, "rating": 8.2},
    {"rank": 139, "title": "On the Waterfront", "release_year": 1954, "rating": 8.2},
    {"rank": 140, "title": "Inside Out", "release_year": 2015, "rating": 8.2},
    {"rank": 141, "title": "Lock, Stock and Two Smoking Barrels", "release_year": 1998, "rating": 8.2},
    {"rank": 142, "title": "The Seventh Seal", "release_year": 1957, "rating": 8.2},
    {"rank": 143, "title": "A Beautiful Mind", "release_year": 2001, "rating": 8.2},
    {"rank": 144, "title": "Casino", "release_year": 1995, "rating": 8.2},
    {"rank": 145, "title": "Room", "release_year": 2015, "rating": 8.2},
    {"rank": 146, "title": "Mr. Smith Goes to Washington", "release_year": 1939, "rating": 8.2},
    {"rank": 147, "title": "The Elephant Man", "release_year": 1980, "rating": 8.1},
    {"rank": 148, "title": "The Wolf of Wall Street", "release_year": 2013, "rating": 8.1},
    {"rank": 149, "title": "Sherlock Jr.", "release_year": 1924, "rating": 8.1},
    {"rank": 150, "title": "V for Vendetta", "release_year": 2005, "rating": 8.1},
    {"rank": 151, "title": "Blade Runner", "release_year": 1982, "rating": 8.1},
    {"rank": 152, "title": "Wild Strawberries", "release_year": 1957, "rating": 8.1},
    {"rank": 153, "title": "The General", "release_year": 1926, "rating": 8.1},
    {"rank": 154, "title": "Warrior", "release_year": 2011, "rating": 8.1},
    {"rank": 155, "title": "Dial M for Murder", "release_year": 1954, "rating": 8.1},
    {"rank": 156, "title": "Trainspotting", "release_year": 1996, "rating": 8.1},
    {"rank": 157, "title": "Gone with the Wind", "release_year": 1939, "rating": 8.1},
    {"rank": 158, "title": "Gran Torino", "release_year": 2008, "rating": 8.1},
    {"rank": 159, "title": "No Country for Old Men", "release_year": 2007, "rating": 8.1},
    {"rank": 160, "title": "The Sixth Sense", "release_year": 1999, "rating": 8.1},
    {"rank": 161, "title": "Fargo", "release_year": 1996, "rating": 8.1},
    {"rank": 162, "title": "The Deer Hunter", "release_year": 1978, "rating": 8.1},
    {"rank": 163, "title": "There Will Be Blood", "release_year": 2007, "rating": 8.1},
    {"rank": 164, "title": "The Thing", "release_year": 1982, "rating": 8.1},
    {"rank": 165, "title": "Finding Nemo", "release_year": 2003, "rating": 8.1},
    {"rank": 166, "title": "The Big Lebowski", "release_year": 1998, "rating": 8.1},
    {"rank": 167, "title": "Come and See", "release_year": 1985, "rating": 8.1},
    {"rank": 168, "title": "Sunrise", "release_year": 1927, "rating": 8.1},
    {"rank": 169, "title": "Cool Hand Luke", "release_year": 1967, "rating": 8.1},
    {"rank": 170, "title": "Tokyo Story", "release_year": 1953, "rating": 8.1},
    {"rank": 171, "title": "Kill Bill: Vol. 1", "release_year": 2003, "rating": 8.1},
    {"rank": 172, "title": "Rebecca", "release_year": 1940, "rating": 8.1},
    {"rank": 173, "title": "The Bandit", "release_year": 1996, "rating": 8.1},
    {"rank": 174, "title": "Shutter Island", "release_year": 2010, "rating": 8.1},
    {"rank": 175, "title": "Hacksaw Ridge", "release_year": 2016, "rating": 8.1},
    {"rank": 176, "title": "Andrei Rublev", "release_year": 1966, "rating": 8.1},
    {"rank": 177, "title": "How to Train Your Dragon", "release_year": 2010, "rating": 8.1},
    {"rank": 178, "title": "Mary and Max", "release_year": 2009, "rating": 8.1},
    {"rank": 179, "title": "Blade Runner 2049", "release_year": 2017, "rating": 8.1},
    {"rank": 180, "title": "Gone Girl", "release_year": 2014, "rating": 8.1},
    {"rank": 181, "title": "Into the Wild", "release_year": 2007, "rating": 8.1},
    {"rank": 182, "title": "Life of Brian", "release_year": 1979, "rating": 8.1},
    {"rank": 183, "title": "Wild Tales", "release_year": 2014, "rating": 8.1},
    {"rank": 184, "title": "Rang De Basanti", "release_year": 2006, "rating": 8.1},
    {"rank": 185, "title": "It Happened One Night", "release_year": 1934, "rating": 8.1},
    {"rank": 186, "title": "The Passion of Joan of Arc", "release_year": 1928, "rating": 8.1},
    {"rank": 187, "title": "Platoon", "release_year": 1986, "rating": 8.1},
    {"rank": 188, "title": "In the Name of the Father", "release_year": 1993, "rating": 8.1},
    {"rank": 189, "title": "Network", "release_year": 1976, "rating": 8.1},
    {"rank": 190, "title": "Hotel Rwanda", "release_year": 2004, "rating": 8.1},
    {"rank": 191, "title": "Stand by Me", "release_year": 1986, "rating": 8.1},
    {"rank": 192, "title": "The Grand Budapest Hotel", "release_year": 2014, "rating": 8.1},
    {"rank": 193, "title": "The Wages of Fear", "release_year": 1953, "rating": 8.1},
    {"rank": 194, "title": "Stalker", "release_year": 1979, "rating": 8.1},
    {"rank": 195, "title": "Ben-Hur", "release_year": 1959, "rating": 8.1},
    {"rank": 196, "title": "Jurassic Park", "release_year": 1993, "rating": 8.1},
    {"rank": 197, "title": "Rush", "release_year": 2013, "rating": 8.1},
    {"rank": 198, "title": "Persona", "release_year": 1966, "rating": 8.1},
    {"rank": 199, "title": "12 Years a Slave", "release_year": 2013, "rating": 8.1},
    {"rank": 200, "title": "Memories of Murder", "release_year": 2003, "rating": 8.1},
    {"rank": 201, "title": "Million Dollar Baby", "release_year": 2004, "rating": 8.1},
    {"rank": 202, "title": "The Truman Show", "release_year": 1998, "rating": 8.1},
    {"rank": 203, "title": "The 400 Blows", "release_year": 1959, "rating": 8.1},
    {"rank": 204, "title": "Mad Max: Fury Road", "release_year": 2015, "rating": 8.1},
    {"rank": 205, "title": "Spotlight", "release_year": 2015, "rating": 8.1},
    {"rank": 206, "title": "Logan", "release_year": 2017, "rating": 8.1},
    {"rank": 207, "title": "Amores Perros", "release_year": 2000, "rating": 8.1},
    {"rank": 208, "title": "Before Sunrise", "release_year": 1995, "rating": 8.1},
    {"rank": 209, "title": "Hachi: A Dog's Tale", "release_year": 2009, "rating": 8.1},
    {"rank": 210, "title": "Butch Cassidy and the Sundance Kid", "release_year": 1969, "rating": 8.1},
    {"rank": 211, "title": "La La Land", "release_year": 2016, "rating": 8.1},
    {"rank": 212, "title": "Nausicaä of the Valley of the Wind", "release_year": 1984, "rating": 8.1},
    {"rank": 213, "title": "The Princess Bride", "release_year": 1987, "rating": 8.1},
    {"rank": 214, "title": "Prisoners", "release_year": 2013, "rating": 8},
    {"rank": 215, "title": "A Wednesday", "release_year": 2008, "rating": 8},
    {"rank": 216, "title": "Catch Me If You Can", "release_year": 2002, "rating": 8},
    {"rank": 217, "title": "The Maltese Falcon", "release_year": 1941, "rating": 8},
    {"rank": 218, "title": "Harry Potter and the Deathly Hallows: Part 2", "release_year": 2011, "rating": 8},
    {"rank": 219, "title": "Rocky", "release_year": 1976, "rating": 8},
    {"rank": 220, "title": "The Nights of Cabiria", "release_year": 1957, "rating": 8},
    {"rank": 221, "title": "The Grapes of Wrath", "release_year": 1940, "rating": 8},
    {"rank": 222, "title": "Monsters, Inc.", "release_year": 2001, "rating": 8},
    {"rank": 223, "title": "Donnie Darko", "release_year": 2001, "rating": 8},
    {"rank": 224, "title": "Les Diaboliques", "release_year": 1955, "rating": 8},
    {"rank": 225, "title": "Barry Lyndon", "release_year": 1975, "rating": 8},
    {"rank": 226, "title": "Paper Moon", "release_year": 1973, "rating": 8},
    {"rank": 227, "title": "Gandhi", "release_year": 1982, "rating": 8},
    {"rank": 228, "title": "Touch of Evil", "release_year": 1958, "rating": 8},
    {"rank": 229, "title": "The Terminator", "release_year": 1984, "rating": 8},
    {"rank": 230, "title": "La Haine", "release_year": 1995, "rating": 8},
    {"rank": 231, "title": "Groundhog Day", "release_year": 1993, "rating": 8},
    {"rank": 232, "title": "The Wizard of Oz", "release_year": 1939, "rating": 8},
    {"rank": 233, "title": "The Bourne Ultimatum", "release_year": 2007, "rating": 8},
    {"rank": 234, "title": "Annie Hall", "release_year": 1977, "rating": 8},
    {"rank": 235, "title": "Dead Poets Society", "release_year": 1989, "rating": 8},
    {"rank": 236, "title": "8½", "release_year": 1963, "rating": 8},
    {"rank": 237, "title": "Jaws", "release_year": 1975, "rating": 8},
    {"rank": 238, "title": "The Help", "release_year": 2011, "rating": 8},
    {"rank": 239, "title": "In the Mood for Love", "release_year": 2000, "rating": 8},
    {"rank": 240, "title": "The Best Years of Our Lives", "release_year": 1946, "rating": 8},
    {"rank": 241, "title": "Infernal Affairs", "release_year": 2002, "rating": 8},
    {"rank": 242, "title": "Paris, Texas", "release_year": 1984, "rating": 8},
    {"rank": 243, "title": "Twelve Monkeys", "release_year": 1995, "rating": 8},
    {"rank": 244, "title": "Three Colours: Red", "release_year": 1994, "rating": 8},
    {"rank": 245, "title": "Beauty and the Beast", "release_year": 1991, "rating": 8},
    {"rank": 246, "title": "Before Sunset", "release_year": 2004, "rating": 8},
    {"rank": 247, "title": "Tangerines", "release_year": 2013, "rating": 8},
    {"rank": 248, "title": "Dog Day Afternoon", "release_year": 1975, "rating": 8},
    {"rank": 249, "title": "The Battle of Algiers", "release_year": 1966, "rating": 8},
    {"rank": 250, "title": "Pirates of the Caribbean: The Curse of the Black Pearl", "release_year": 2003, "rating": 8}
]
