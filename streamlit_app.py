import streamlit as st
import pandas as pd
import numpy as np



st.title("Random list app")

tab1, tab2, tab3 = st.tabs([":dog: Top dog", "🏆 Ultimate trivia", "🔮 Recommendation"])

with tab1:
    st.header("Top dog")
    
    with st.expander("**Exercise 1** Guess my favourite!"):
        st.write("Please create:")
        st.checkbox("A list of comparable things you like ex. movies, books, songs, artists, foods, ice-creams etc.", key="1.1")
        st.checkbox("A selection interface, i.e. drop-down", key="1.2")
        st.checkbox("User clicks on a submit button.", key="1.3")
        st.checkbox("Feedback pop-up on whether the user guessed it or not.", key="1.4")
        st.checkbox("Give your riddle a header with and a short description.", key="1.5")
        st.info("Useful commands: st.header(), st.write(), st.selectbox(), st.select_slider(), st.radio(), st.button(), st.success(), st.error(), st.info(), st.balloons()")
    
    st.write(" All of these icons brought new waves of movement qualities and ideas into the choreography world. I love all of them, but...")
    favourite_things = ["Shakira", "Charlie Chaplin", "Jung Kook", "Lady Gaga", "Michael Jackson"]
    #notable_for = ["Adaptation", "Impressions", "Artistic Versatility", "Raw Expression", "Personality"]
    
    guess = None
    submitted = None

    guess = st.selectbox("Which dancer so you think is my No1 inspiration?", options=favourite_things, index=None)

    submitted = st.button("Submit!")

    if (guess and submitted):
        if guess=="Jung Kook":
            st.success("That's correct!")
            st.balloons()
        else: 
            st.error("Sadly not. Try again!")



with tab2:

    st.header("Know your idols")
    with st.expander("**Exercise 2** Ultimate trivia"):
        st.write("Please create:")
        st.checkbox("A view with multiple tabs and place your first app there.", key="2.1")
        st.checkbox("One numeric list and one categorical list linked to the favourite things, i.e. publication year and genre.", key="2.2")
        st.checkbox("Wrap up the contents in a pandas dataframe, i.e. columns = [`authors`, `books`, `year`]", key="2.3")
        st.checkbox("Create a 2 question about the 1st and 2nd property, where the contents of the question are randomly appearing. i.e. Who is the `author`(column name) of the book (random item from the `books` column).", key="2.4")
        st.checkbox("Split the screen in two for each question with `st.columns()`",  key="2.5")
        st.checkbox("Give your riddle a header with and a short description.", key="2.6")
        st.info("Useful commands: pd.DataFrame(), st.dataframe(), st.columns(), with col1:, np.random.randint(), np.sort(), st.select_slider(), st.selected_control(), st.success(), st.error(), st.info(), st.session_state.<var_name>")

    st.write("Let's see how well you know these timeless dance idols.")

    peak_activity_approx = [2005, 1920, 2020, 2010, 1995]
    dance_style = ["Latin", "Physical Theatre", "Urban", "Experimental", "Jazz"]
    
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

        year_guess = st.select_slider(question1, np.sort(peak_activity_approx), value=None)
        st.info(dancer)

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
        

        dancer_guess = st.segmented_control(question2,dancer_df['dancer'])
        st.info(style)
        answer2 = dancer_df[dancer_df["style"]==style]["dancer"].tolist()
        submit2 = st.button("Submit dancer")
        if submit2:
            if answer2 == dancer_guess:
                st.success("Wow! You know", dancer_guess, "well!")
            else:
                st.error("Not really.",answer2,"is best known as a ", dancer_df[dancer_df["dancer"]==answer2[0]]['style'].iloc[0]," dancer!")



with tab3:
    st.header("Recommendation")

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
    

    st.subheader("Who is your dance idol mentor?")
    st.write("Order the dancer traits according to how much it aligns with your inner compass.")

    versatility = [2,3,5,1,2]
    creativity = [2,5,4,5,5]
    skill = [4,5,3,2,4]
    personality = [5,4,3,4,5]
    
    features = ["versatility", "creativity", "skill", "personality"]
    #image = []
    
    dancer_df["versatility"] = versatility
    dancer_df["creativity"] = creativity
    dancer_df["skill"] = skill
    dancer_df["personality"] = personality

    order1, order2, order3, order4 = st.columns(4)
 
    with order1:
        or1 = st.selectbox(" 1:",features, index=None, key="order_1")        
    with order2:
        features2 = [f for f in features if f!=or1]
        or2 = st.selectbox(" 2:",features2, index=None, key="order_2")
    with order3:
        features3 = [f for f in features2 if f!=or2]
        or3 = st.selectbox(" 3:", features3, index=None, key="order_3")
    with order4:
        features4 = [f for f in features3 if f!=or3]
        if len(features4)==1:
            or4 = features4[0]
            st.write(" 4:")
            st.write(or4)
        else:
            or4 = None

    submit_rec=None
    submit_rec = st.button("Find out!", key = "rec_submit")

    if or4 and submit_rec:

        if [or1, or2, or3, or4] == ["versatility", "creativity", "personality", "skill"]:
            st.info("What a coincidence! That's my preference too! We should be dance buddies!")
            st.balloons()

        dancer_df["scores"] = (4 * dancer_df[or1] +
                               3 * dancer_df[or2] +
                               2 * dancer_df[or3] +
                               1 * dancer_df[or4] )
        sorted_dancers = dancer_df[["dancer","scores"]].sort_values(by="scores", ascending=False)

        advice_1 = sorted_dancers["dancer"].iloc[0]

        st.write(advice_1)

  
    with st.expander("Check out the full table here!"):
        st.dataframe(dancer_df)

    if or4 and submit_rec:
         with st.expander("Dancer scores"):
            st.dataframe(dancer_df[["dancer","scores"]].sort_values(by="scores", ascending=False))
