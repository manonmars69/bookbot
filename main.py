def main ():
    
    try:
        book_path = input("Please enter book path: ")
        b_path = "books/frankenstein.txt"

        def read_book (book_path): 
            with open(book_path) as f:
                file_contents = f.read()
                print(file_contents)
        return read_book(book_path)
    
    except FileNotFoundError:
        print("Please enter a correct path - f.e.: books/lorem_ipsum.txt") 
    
    
    #def word_counter():
            #words = 0
            #for i in file_contents:
                #words += i
            #print(words)

#review ch.13 & 14

main ()

