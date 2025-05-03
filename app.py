import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

teams = ['Royal Challengers Bangalore',
 'Mumbai Indians',
 'Sunrisers Hyderabad',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl','rb'))
st.title('IPL Win Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))

if batting_team == bowling_team:
    st.warning("Batting and bowling teams cannot be the same. Please select different teams.")
    st.stop()

selected_city = st.selectbox('Select host city',sorted(cities))

target = st.number_input('Target', min_value=00, step=5, format="%d")
if target < 0:
    st.warning("Please enter a valid target score.")
    st.stop()


col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score', step=5)
if score < 0:
    st.warning("Score cannot be negative.")
    st.stop()

with col4:
    overs = st.number_input('Overs completed')
if overs < 0:
    st.warning("Overs cannot be negative.")
    st.stop()
if overs > 20:
    st.warning("Overs cannot be greater than 20.")
    st.stop()

with col5:
    wickets = st.number_input('Wickets out', step=1)
if wickets < 0:
    st.warning("Wickets cannot be negative.")
    st.stop()
if wickets > 10:
    st.warning("Wickets cannot be greater than 10.")
    st.stop()


if st.button('Predict Probability'):
    if target <= 0 or score < 0 or overs <= 0 or wickets < 0 or overs > 20 or wickets > 10:
        st.warning("Please make sure all fields are filled correctly and within valid limits.")
        st.stop()
        
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")
    fig, ax = plt.subplots()
    teams = [batting_team, bowling_team]
    probabilities = [win * 100, loss * 100]
    colors = ['green', 'red']

    ax.bar(teams, probabilities, color=colors)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Win Probability (%)")
    ax.set_title("Predicted Win Probability")
    for i, v in enumerate(probabilities):
        ax.text(i, v + 2, f"{round(v)}%", ha='center', fontweight='bold')
    st.pyplot(fig)
  