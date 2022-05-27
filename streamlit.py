import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('tranformed.csv')

st.title("Consumer Complaint Data")
complaints, State = st.columns((4,1))

states_drop = State.selectbox("State",pd.unique(df["state"]))
df = df[df["state"] == states_drop]




total_complaints = len(df)
closed_filter = df[df["company_response"]=="Closed with explanation"]
closed = len(closed_filter)
timely_filter = df[df["timely"]=="Yes"]
timely = len(timely_filter)
progress_filter = df[df["company_response"]=="In progress"]
prog = len(progress_filter)
states = df['state'].unique()
month_comp = df.groupby(['date_received']).size().reset_index(name='count').sort_values(by='date_received', ascending=True)
issue = df.groupby(['issue', 'sub_issue']).size().reset_index(name='count').sort_values(by='count', ascending=True)

total_kpi,closed_kpi,timely_kpi,prog_kpi, state = st.columns(5)
total_kpi.metric(label="Total Complaints",value=total_complaints, delta=-0.75)
closed_kpi.metric(label = "Closed Status Complaints",value=closed, delta=-0.75)
timely_kpi.metric(label="Timely Responded Complaints",value=timely, delta=-0.75)
prog_kpi.metric(label="Progress Status Complaints",value=prog, delta=-0.75)

monthly_complaints, issues = st.columns(2)

with monthly_complaints:
    st.subheader("Complaints by Month")
    fig = px.line(month_comp , x='date_received', y='count')
    st.write(fig)
with issues:
    st.subheader("Complaints by Issue and Sub-Issue")
    fig = px.treemap(issue, path=['issue', 'sub_issue'], values='count')
    st.write(fig)

    

