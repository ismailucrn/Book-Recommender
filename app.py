import streamlit as st
import pandas as pd
import rec_funct_books
from rec_funct_books import df2

st.title("Book Recommender")

books_label = ["1","2","3","4","5"]
book_list = []
for i in range(len(books_label)):
    book_list.append(st.selectbox(f"Please select number {i+1} movies for recommendation",df2["title"].values, key = i))

#recommend books
if st.button("Recommend"):
    for i in range(len(book_list)):
        if book_list[i] == "":
            st.write("Please select a book")
            break
    else:
        st.header("Your recommendations are:")
        local_book_dict = rec_funct_books.BookRecommender_final(book_list)
        for i in range(len(local_book_dict)):
            title_container = st.container()
            col1, col2 = st.columns([1, 2])
            with title_container:
                with col1:
                    st.subheader(local_book_dict[i])
                    st.image(df2.loc[df2["title"] == (rec_funct_books.BookRecommender_final(book_list)[i])]["image_url"].values[0], width = 200)
                with col2:
                    st.subheader("")
                    st.subheader("")
                    st.subheader("")
                    st.subheader("Author:")
                    st.write(df2.loc[df2["title"] == (rec_funct_books.BookRecommender_final(book_list)[i])]["authors"].values[0])
                    st.subheader("Publisher:")
                    st.write(df2.loc[df2["title"] == (rec_funct_books.BookRecommender_final(book_list)[i])]["publisher"].values[0])
                    st.subheader("Pages:")
                    st.write(df2.loc[df2["title"] == (rec_funct_books.BookRecommender_final(book_list)[i])]["  num_pages"].values[0])
