# 🎧 Model Card: Music Recommender Simulation

## Model Name  

VibeMatch 1.0  

---

## Goal / Task  

This recommender suggests songs that match a user’s taste based on their preferred genre, mood, and energy level. The goal is to rank songs so the most relevant ones appear first.

---

## Data Used  

The dataset contains around 10–18 songs with features such as genre, mood, energy, tempo, valence, and acousticness. It includes a mix of genres like pop, rock, lofi, and ambient.

However, the dataset is small and does not fully represent real-world music diversity, which limits recommendation variety.

---

## Algorithm Summary  

The system compares user preferences with song features and assigns each song a score.

Songs gain points if the genre matches and if the mood matches. They also receive points based on how close their energy level is to the user’s target energy. Acousticness is included depending on whether the user prefers acoustic music.

After scoring all songs, the system sorts them from highest to lowest score and returns the top results.

---

## Observed Behavior / Biases  

The system tends to over-prioritize genre and energy, which can lead to repetitive recommendations (a filter bubble).

It also struggles with conflicting preferences, such as high energy but sad mood, because it cannot fully balance those features.

Additionally, the small dataset creates bias toward certain genres like pop, reducing diversity.

---

## Evaluation Process  

I tested the system using multiple user profiles, including High-Energy Pop, Chill Lofi, Intense Rock, and a conflicting edge-case profile.

The results generally matched expectations. High-energy profiles received energetic songs, while chill profiles received slower songs.

One interesting observation was that some songs, like "Gym Hero," appeared frequently due to strong energy and genre weighting.

I also ran an experiment by increasing the importance of energy and reducing genre weight. This made the system recommend songs with similar energy levels but from different genres.

---

## Intended Use and Non-Intended Use  

This system is designed for educational purposes to demonstrate how recommendation systems work.

It should not be used as a real music recommender because it has a small dataset, simple logic, and does not adapt to user behavior.

---

## Ideas for Improvement  

- Add more features like tempo and valence into the scoring  
- Increase dataset size for better diversity  
- Add diversity rules so the same songs do not always appear  
- Support multiple or changing user preferences  

---

## Personal Reflection  

My biggest learning moment was realizing how small changes in scoring weights can completely change recommendations.  

Using AI tools helped me quickly generate ideas and debug code, but I still had to verify the logic myself to make sure it made sense.  

It was surprising how even a simple scoring system could feel like a real recommender when the outputs matched user preferences.  

If I extended this project, I would add more data and try using machine learning methods like similarity or clustering.