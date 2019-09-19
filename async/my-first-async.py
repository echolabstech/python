API_KEY = 'AIzaSyDSc4h-R_ByHJAr7wzPeqEHne9hkaMIa4w';
UUID = '111456584073054736246';

URLS = {
    'search': 'https://www.googleapis.com/books/v1/volumes?q=',
}

# search_term - string of search terms
def search_books_for(search_term):
    query_param = search_term.lower().split(' ');
    query_param = '+'.join(query_param)
    print(query_param);

if __name__ == "__main__":
    search_books_for('star wars')