import streamlit as st
import pandas as pd
import numpy as np



st.title("Random list app")

tab1, tab2, tab3 = st.tabs([":dog: Top dog", "🏆 Ultimate trivia", "🔮 Recommendation"])

with tab1:
    st.header("Top dog")
    
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
        answer2 = dancer_df[dancer_df["style"]==style]["dancer"].iloc[0]
        submit2 = st.button("Submit dancer")

        if submit2:
            if answer2 == dancer_guess:
                st.success(f"Wow! You know {dancer_guess} well!")
            else:
                true_style=dancer_df[dancer_df["dancer"]==dancer_guess]["style"].iloc[0]
                st.error(f"Not really. {dancer_guess} is best known as a {true_style.lower()} dancer!")

with tab3:
    st.header("Recommendation")

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
