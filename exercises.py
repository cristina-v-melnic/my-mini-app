import streamlit as st


with st.expander("**Exercise 1** Guess my favourite!"):
        st.write("Please create:")
        st.checkbox("A list of comparable things you like ex. movies, books, songs, artists, foods, ice-creams etc.", key="1.1")
        st.checkbox("A selection interface, i.e. drop-down", key="1.2")
        st.checkbox("User clicks on a submit button.", key="1.3")
        st.checkbox("Feedback pop-up on whether the user guessed it or not.", key="1.4")
        st.checkbox("Give your riddle a header with and a short description.", key="1.5")
        st.info("Useful commands: st.header(), st.write(), st.selectbox(), st.select_slider(), st.radio(), st.button(), st.success(), st.error(), st.info(), st.balloons()")


with st.expander("**Exercise 2** Ultimate trivia"):
        st.write("Please create:")
        st.checkbox("A view with multiple tabs and place your first app there.", key="2.1")
        st.checkbox("One numeric list and one categorical list linked to the favourite things, i.e. publication year and genre.", key="2.2")
        st.checkbox("Wrap up the contents in a pandas dataframe, i.e. columns = [`authors`, `books`, `year`]", key="2.3")
        st.checkbox("Create a 2 question about the 1st and 2nd property, where the contents of the question are randomly appearing. i.e. Who is the `author`(column name) of the book (random item from the `books` column).", key="2.4")
        st.checkbox("Split the screen in two for each question with `st.columns()`",  key="2.5")
        st.checkbox("Give your riddle a header with and a short description.", key="2.6")
        st.info("Useful commands: pd.DataFrame(), st.dataframe(), st.columns(), with col1:, np.random.randint(), np.sort(), st.select_slider(), st.selected_control(), st.success(), st.error(), st.info(), st.session_state.<var_name>")

with st.expander("**Exercise 3** (Un)beatable advice"):
        st.write("Please create:")
        st.checkbox("A relevant question to help the user find their next read/practice/inspiration/product/meal. i.e. Which book fits my interests right now?", key="3.1")
        st.checkbox("Find at least 2 numeric features that would help determine the answer on the same scale. i.e. book length and original content in the 1-5 out of 5 scale", key="3.2")
        st.checkbox("Complete the dataframe with these new features for the existing objects.", key="3.3")
        st.checkbox("Ask the user to order the preferences from most important to least important features.", key="3.4")
        st.checkbox("Create a model that returs the recommendations using a weighted sum approach of user preference and feature scores.", key="3.5")
        st.checkbox("Ask the user if they can figure out your own preferred ordering that lead to the answer from the first exercise.", key="3.6")
        st.checkbox("Add a  conditional pop-up for when the user selection is the same as the author's.")
        st.info("Useful commands: st.subheader(), st.write(), st.selectbox(), st.button(), st.info()/success()/error(), st.balloons()")
    
