import streamlit as st
from db import init_db, add_plan, get_all_plans
from agent import generate_plan
from datetime import datetime

st.set_page_config(
    page_title="AI Task Planner",
    layout="wide"
)

init_db()

st.sidebar.header("Plan History")
all_plans = get_all_plans()

if not all_plans:
    st.sidebar.info("No plans have been generated yet.")
else:
    for plan_id, goal, plan_content, timestamp in all_plans:
        with st.sidebar.expander(f"Goal: {goal} - (Created: {timestamp.split('.')[0]})"):
            st.markdown(plan_content)

st.title("AI Task Planner")

now = datetime.now()
date_time_str = now.strftime("%A, %B %d, %Y - %I:%M %p")
st.caption(f"Pimpri-Chinchwad, Maharashtra | {date_time_str}")

st.markdown("Enter your goal and let the AI agent create a detailed, actionable plan for you.")

with st.form("goal_form"):
    goal_input = st.text_input(
        "Enter your goal:",
        placeholder="e.g., Plan my upcoming weekend"
    )
    submitted = st.form_submit_button("Generate Plan")

if submitted and goal_input:
    with st.spinner("The agent is thinking and gathering information... Please wait."):
        generated_plan = generate_plan(goal_input)

        if generated_plan:
            add_plan(goal_input, generated_plan)
            st.subheader("Your Generated Plan:")
            st.markdown(generated_plan)
        else:
            st.error("Sorry, the agent could not generate a plan. Please try again.")

