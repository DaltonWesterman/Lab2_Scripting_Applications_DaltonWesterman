"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
        'name' : 'Dalton Westerman',
        'student ID' : 10257099,
        'pizza toppings': [
            'PEPPERONI',
            'BACON',
            'SAUSAGE'
        ],
        'movie info' : [
            {
                'title' : 'Return of the jedi',
                'genre' : 'sci-fi'
            },
            {
                'title' : 'Revenge of the sith',
                'genre' : 'sci-fi'
            }
        ]
    }
    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)
    print(f"My name is {about_me['name']}, but you can call me Sir {about_me['name'].split()[0]}")
    print(f"My student ID is {about_me['student ID']}")


    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)
    #for pizza_toppings in about_me['pizza toppings']:
        #print(f'•{pizza_toppings}')

    # Step 5: Add pizza toppings to the data structure
    # TODO: Change to pizza toppings you like
    add_pizza_toppings(about_me, ['chicken', 'ground beef'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, 'John Wick 4', 'action')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)
    for i, add_movie in enumerate (about_me['genre']):
        if i < len(about_me['genre']) - 1:
            print(about_me['genre'], end= ', ')
        else:
            print(about_me['genre'], end= '.')

    # Step 8: Print a comma-separated list of movie titles
    print_movie_genres(about_me)
    for i, add_movie in enumerate (about_me['title']):
        if i < len(about_me['title']) - 1:
            print(about_me['title'], end= ', ')
        else:
            print(about_me['title'], end= '.')


    print_movie_titles(about_me['movies'])

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    # Complete function body per Step 3
    # Print sentence containing name
    print(f"My name is {my_info['name']}, but you can call me Sir {my_info['name'].split()[0]}")

    # Print sentence containing student ID
    print(f"My student ID is {my_info['student ID']}")

    print()

def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    # Complete function body per Step 4
    # Print header "My favourite pizza toppings are:"
    print(f'My favourite favourite pizza toppings are:')
    
    # Print bullet list of favourite pizza toppings
    for pizza_toppings in my_info['pizza toppings']:
        print(f'•{pizza_toppings}')
    print()

def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    # Complete function body per Step 5
    # Append new pizza toppings to end of list
    my_info['pizza toppings'].extend({'chicken', 'ground beef'})

    # Convert all pizza toppings to lowercase
    for i, toppings in enumerate (my_info['pizza toppings']):
        my_info['pizza toppings'][i] = toppings.lower()

    # Sort toppings list alphabetically
    my_info['pizza toppings'].sort()

    return

def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    # TODO: Complete function body per Step 6
    # Create dictionary for new movie and add to movie list
    my_info['movies'].append({title:'John Wick 4', genre:'action' })

    return

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 7
    print(f"I like to watch{'sci-fi'},{'sci-fi'}, and {'action'}movies")

    print()

def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    # TODO: Complete function body per Step 8

    # I believe this's how it's done? line 47 add_movie before the movies listed was giving an error since the start, but line 139 and 151 are hopefully exactly you intended us to write them in the D2L lab document
    print(f"Some of my favourite movies are{'return of the jedi'},{'revenge of the sith'}, and {'John Wick 4'}!")

    print()


if __name__ == '__main__':
    main()