import streamlit as st
import pandas as pd
import numpy as np

st.title("Random list app")

tab1, tab2, tab3 = st.tabs([":dog: Top dog", "Ultimate trivia", "Recommendation"])

with tab1:
    st.header("Top dog")
    
    with st.expander("**Exercise 1** Guess my favourite!"):
        st.write("Please create:")
        st.checkbox("A list of comparable things you like ex. movies, books, songs, artists, foods, ice-creams etc.", key="1.1")
        st.checkbox("A selection interface, i.e. drop-down", key="1.2")
        st.checkbox("User clicks on a submit button.", key="1.3")
        st.checkbox("Feedback pop-up on whether the user guessed it or not.", key="1.4")
        st.checkbox("Give your riddle a header with and a short description.", key="1.5")
        st.info("Useful commands: st.header(), st.write(), st.selectbox(), st.select_slider(), st.button(), st.balloons() (maybe try st radio too)")
    
    st.write(" All of these icons brought new waves of movement qualities and ideas into the choreography world. I love all of them, but...")
    favourite_things = ["Shakira", "Charlie Chaplin", "Jung Kook", "Lady Gaga", "Michael Jackson"]
    
    guess = None
    submitted = None

    guess = st.selectbox("Which dancer so you think is my No1 inspiration?", favourite_things, index=None)

    submitted = st.button("Submit!")

    if (guess and submitted):
        if guess=="Jung Kook":
            st.success("That's correct!")
            st.balloons()
        else: 
            st.error("Sadly not. Try again!")



with tab2:

    st.header("My trivia title")
    with st.expander("**Exercise 2** Ultimate trivia"):
        st.write("Please create:")
        st.checkbox("A view with multiple tabs and place your first app there.", key="2.1")
        st.checkbox("One numeric list and one categorical list linked to the favourite things, i.e. publication year and genre.", key="2.2")
        st.checkbox("Wrap up the contents in a pandas dataframe, i.e. columns = [`authors`, `books`, `year`]", key="2.3")
        st.checkbox("Create a 2 question about the 1st and 2nd property, where the contents of the question are randomly appearing. i.e. Who is the `author`(column name) of the book (random item from the `books` column).", key="2.4")
        st.checkbox("Split the screen in two for each question with `st.columns()`",  key="2.5")
        st.checkbox("Give your riddle a header with and a short description.", key="2.6")
        st.info("Useful commands: pd.DataFrame(), st.columns(), with col1:, np.random.randint(), np.sort(), st.multiselect(), ")

    st.write("My trivia description")

    peak_activity_approx = [2005, 1920, 2020, 2010, 1995]
    dance_style = ["Latin", "Jazz", "Urban", "Experimental", "Jazz"]
    
    dancer_df = pd.DataFrame({
        "dancer": favourite_things,
        "style": dance_style,
        "peak_activity_approx": peak_activity_approx
    })



    c1, c2 = st.columns(2)
            
    with c1:
        question1 = "Around which year did this artist have their peak success?"
        dancers = dancer_df['dancer'].unique()

        random_id = np.random.randint(len(dancers))
        if "dancer" not in st.session_state:
            st.session_state.dancer = dancer_df['dancer'][random_id]

        dancer = st.session_state.dancer

        st.info(dancer)
        year_guess = st.select_slider(question1, np.sort(peak_activity_approx), value=None)

        submit1 = None
        submit1 = st.button("Submit year")
        answer1 = dancer_df[dancer_df["dancer"]==dancer]["peak_activity_approx"].iloc[0]

        if submit1:
            if year_guess == answer1:
                st.success("Bravo! You are an expert.")
            else:
                st.error("Please try again.")

    with c2:
        question2 = "Which artist is most representative of the following style?"

        styles = dancer_df['style'].unique()
        style_id = np.random.randint(len(styles))

        if "style" not in st.session_state:
            st.session_state.style = dancer_df['style'][style_id]

        style = st.session_state.style
        st.info(style)

        dancer_guess = st.segmented_control(question2,dancer_df['dancer'])
        st.write(dancer_guess)
        answer2 = dancer_df[dancer_df["style"]==style]["dancer"].tolist()
        submit2 = st.button("Submit dancer")
        if submit2:
            st.write(answer2)
            st.write(dancer_guess in answer2)



with tab3:
    st.header("Recommendation")

    with st.expander("**Exercise 3** (Un)beatable advice"):
        st.write("Please create:")
        st.checkbox("A relevant question to help the user find their next read/practice/inspiration/product/meal. i.e. Which book fits my interests right now?", key="3.1")
        st.checkbox("Find at least 2 numeric features that would help determine the answer on the same scale. i.e. book length and original content in the 1-5 out of 5 scale", key="3.2")
        st.checkbox("Complete the dataframe with these new features for the existing objects.", key="3.3")
        st.checkbox("Ask the user to order the preferences from most important to least important features.", key="3.4")
        st.checkbox("Create 2 models which will give advice at the same time. The first model generates the recommendations using a weighted sum approach of user preference and object score, while the other is fully random.", key="1.5")
        st.checkbox("Provide both results at the same time, and ask the user which recommendation matches their preference.")
        st.checkbox("Upon selection, show the rankings and tell the user if they were right about their assumed preferences.")
        st.info("Useful commands: st.header(), st.write(), st.selectbox(), st.select_slider(), st.button(), st.balloons() (maybe try st radio too)")
    


    versatility = [2,3,5,1,2]
    creativity = [2,5,4,5,5]
    skill = [4,5,3,2,4]
    personality = [5,4,3,4,5]
    #notable_for = ["Adaptation", "Impressions", "Artistic Versatility", "Raw Expression", "Personality"]
    features = ["versatility", "creativity", "skill", "personality"]
    #image = []
    
    dancer_df["versatility"] = versatility
    dancer_df["creativity"] = creativity
    dancer_df["skill"] = skill
    dancer_df["personality"] = personality

    order1, order2, order3, order4 = st.columns(4)

    with order1:
        or1 = st.selectbox(features)
    with order2:
        or2 = st.selectbox(features-or1)
    with order3:
        or3 = st.selectbox(features-or1-or2)
    with order4:
        or4 = st.selectbox(features-or1-or2-or3)

    dancer_df["scores"] = 4*dancer_df[or1]
    st.text(dancer_df["scores"])