# main() function 
def main ():

# try / except block for error messages
    try: 
        # user input via terminal to determine the book path
        book_path = input("Please enter book path: ")  
        
        # calling read_book function via var book
        book_text = read_book(book_path)  
        
        # calling word_counter function via var sum_words
        sum_words = word_counter(book_text) 

        # calling letter_counter function via var sum_letters
        sum_letters = letter_counter(book_text) 
        
        print(f"{sum_words} words found in the document")
        print(sum_letters)
    
  # if FileNotFoundError occurs print the following string
    except FileNotFoundError:
        print("Please enter a correct path, f.e.: books/lorem_ipsum.txt") 

 # if KeyboardInterrupt occurs print the following string   
    except KeyboardInterrupt:
        print("Script canceled")

# else print Exception error code 
    except Exception as e:
        print(e)

# function read book from user input and return book text  
def read_book(path): 
    with open(path) as f:
        return f.read()    

# function word counter with len() and .split() function
def word_counter(text):
    return len(text.split())

# function counting letters w/o duplicate & only lower case 
def letter_counter(text):
    # shamelessly stole from stackoverflow - note to my future self why this solution is elegant:
    # ord() function transforms a string into an unicode (int) f.e. ord("a") = 97 and ord("z") = 122
    # which means the whole lower case alphabet is from unicode 97 to 122
    # put into a for loop with an iteration var i, for all elements within range(97, 123) or range(ord("a"), ord("z")+1)  
    # the range() function includes only unicode 121 ("y") so we have to add +1 to the end
    # chr() function transforms a unicode back to a string, in our case chr(97) = "a" to chr(122) = "z" 
    # instead of writing dict_letters = {"a": 0, "b": 0, ... ,"z": 0} we can write:   
    dict_letters = {chr(i): 0 for i in range(ord("a"), ord("z")+1)}  
    
    
    
    return dict_letters 





main ()


