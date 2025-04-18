import streamlit as st
import json

# File to store book data
LIBRARY_FILE = "library.json"

def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def add_book(title, author, year, genre, read_status):
    library = load_library()
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    save_library(library)
    return "Book added successfully!"

def remove_book(title):
    library = load_library()
    library = [book for book in library if book["title"].lower() != title.lower()]
    save_library(library)
    return "Book removed successfully!"

def search_books(query, search_by):
    library = load_library()
    results = [book for book in library if query.lower() in book[search_by].lower()]
    return results

def get_statistics():
    library = load_library()
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    return total_books, percentage_read

# Streamlit UI
st.title("📚 Personal Library Manager")
menu = st.sidebar.selectbox("Menu", ["Add Book", "Remove Book", "Search Book", "Display Books", "Statistics"])

if menu == "Add Book":
    st.header("📖 Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, format="%d")
    genre = st.text_input("Genre")
    read_status = st.checkbox("Have you read this book?")
    if st.button("Add Book"):
        message = add_book(title, author, year, genre, read_status)
        st.success(message)

elif menu == "Remove Book":
    st.header("❌ Remove a Book")
    title = st.text_input("Enter the title of the book to remove")
    if st.button("Remove Book"):
        message = remove_book(title)
        st.success(message)

elif menu == "Search Book":
    st.header("🔍 Search for a Book")
    search_by = st.radio("Search by", ["title", "author"])
    query = st.text_input("Enter search term")
    if st.button("Search"):
        results = search_books(query, search_by)
        if results:
            for book in results:
                st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
        else:
            st.warning("No books found.")

elif menu == "Display Books":
    st.header("📚 Your Library")
    library = load_library()
    if library:
        for book in library:
            st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        st.warning("No books in the library.")

elif menu == "Statistics":
    st.header("📊 Library Statistics")
    total_books, percentage_read = get_statistics()
    st.write(f"**Total books:** {total_books}")
    st.write(f"**Percentage read:** {percentage_read:.2f}%")
    st.write(f"**Percentage read:** {percentage_read:.2f}%")