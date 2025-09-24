# AI Task Planner

This project is an AI assistant that turns your simple goals into clear, step-by-step plans. It uses live information from the internet to make the plans smart and useful.

## How It Works

Tell the AI what you want to do, like "plan a weekend trip." The AI uses a web search to find the best places and a weather tool to check the forecast. It then combines all this info to create a detailed schedule for you. Every plan you make is saved automatically so you can look at it later.

## Setup and Run Instructions

### 1. Get the code:

```bash
git clone https://github.com/deepnavale/AI-Task-Planner.git
cd AI-Task-Planner
```

### 2. Install the necessary packages:

```bash
pip install -r requirements.txt
```

### 3. Add your API keys:

Create a new file named `.env` in the project folder and paste this inside, adding your keys:

```env
GROQ_API_KEY="your_groq_api_key"
TAVILY_API_KEY="your_tavily_api_key"
OPENWEATHER_API_KEY="your_openweathermap_api_key"
```

### 4. Run the app:

Open your terminal and run this command:

```bash
streamlit run app.py
```

## Example Goals with Generated Plans

Here are a couple of examples of what the planner can do.

### Example 1: Historical Delhi

**Goal:** `Plan a 2-day historical tour of Delhi.`

**Generated Plan:**

#### 2-Day Delhi Historical Tour

**Day 1: Old & New Delhi**
- **9:00 AM - 1:00 PM:** Explore the Red Fort and Jama Masjid in Old Delhi.
- **2:00 PM - 5:00 PM:** Visit India Gate and the President's House area.
- **6:00 PM onwards:** Visit Humayun's Tomb.

**Day 2: South Delhi Monuments**
- **10:00 AM - 1:00 PM:** Visit the Qutub Minar complex.
- **2:00 PM - 4:00 PM:** Walk through the historic Lodhi Garden.
- **5:00 PM onwards:** Visit the modern Lotus Temple.

### Example 2: A Day in Pune

**Goal:** `Plan a 1-day trip to Pune with historical sites and local food.`

**Generated Plan:**

#### 1-Day Pune Itinerary

**Morning: Peshwa History**
- **9:00 AM - 12:00 PM:** Visit Shaniwar Wada, the historic fortified palace of the Peshwas.
- **1:00 PM - 2:00 PM:** Enjoy authentic Misal Pav for lunch at a famous local spot.

**Afternoon: National Heritage**
- **2:30 PM - 5:00 PM:** Explore the Aga Khan Palace, a memorial to Mahatma Gandhi.

**Evening: Local Culture**
- **6:00 PM onwards:** Walk through the bustling Laxmi Road for shopping and street food.

