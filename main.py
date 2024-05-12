# main() function 
def main ():

# try / except block for error messages
    try: 
        # user input via terminal to determine the book path
        book_path = input("Please enter book path: ")  
        
        # set var book for read_book function 
        book_text = read_book(book_path)  
        
        # set var sum_words for word_counter function 
        sum_words = word_counter(book_text) 

        # set var book_text_lc for lower_case_book function 
        book_text_lc = lower_case_book(book_text)
        
        # set var sum_letters for letter_counter function 
        sum_letters = letter_counter(book_text_lc) 

        # set var sum_letters_list for letters_list function
        sum_letters_list = letters_list(sum_letters)

        # sort sum_letters_list from highest number to lowest 
        sum_letters_list.sort(reverse = True, key = sort_common)  

        #print report
        print(f"--- Begin report of {book_path} --- \n \n {sum_words} words found in the document \n")
        report_letters(sum_letters_list)
        print(f"\n --- End report ---")
                
  # if FileNotFoundError occurs print the following string
    except FileNotFoundError:
        print("Please enter a correct path, f.e.: books/lorem_ipsum.txt") 

 # if KeyboardInterrupt occurs print the following string   
    except KeyboardInterrupt:
        print("Script canceled")

# else print Exception error code 
    except Exception as e:
        print(e)

# function read book path from user input and return book text  
def read_book(path): 
    with open(path) as f:
        return f.read()    

# function word counter with len() and .split() function
def word_counter(text):
    return len(text.split())

# function to turn all book letters to lower case
def lower_case_book(text):
    return text.lower()

# function counting book letters 
def letter_counter(text_lc):

    # shamelessly stolen from stackoverflow - note to my future self:
    # ord() function transforms a string into an unicode (int) f.e. ord("a") = 97 and ord("z") = 122
    # which means the whole lower case alphabet is from unicode 97 to 122
    # put into a for loop with an iteration var i, for all elements within range(97, 123) or range(ord("a"), ord("z")+1)  
    # the range() function includes only unicode 121 ("y") so we have to add +1 to the end
    # chr() function transforms a unicode back to a string, in our case chr(97) = "a" to chr(122) = "z" 
    # instead of writing dict_letters = {"a": 0, "b": 0, ... ,"z": 0} we can write:   
    # as an afterthought I probably could just create dict_letters = {} and let a for loop fill up the dictionary
    dict_letters = {chr(i): 0 for i in range(ord("a"), ord("z")+1)}  
    
    # for loop comparing parameter text_lc letters with dictionary dict_letters
    for j in text_lc:
        if j in dict_letters:  
            dict_letters[j] += 1
    return dict_letters


# turn dictionary to a list of dictionaries
def letters_list(dict):
    l_list = []
    for k in dict:
        l_list.append({"char": k, "num": dict[k]})
    return l_list

# sort function for "num" 
def sort_common(list_dict):
    return list_dict["num"]


# report function for letters count
def report_letters(list_dict_sorted):
    for l in list_dict_sorted:
        print(f"The '{l['char']}' character was found {l['num']} times")

main ()


