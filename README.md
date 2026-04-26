ere’s your UPDATED README with only the required additions/changes (nothing unnecessary changed). You can copy-paste this directly.

# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This project implements a simple content-based music recommender system that suggests songs based on a user’s taste profile. Instead of using other users’ behavior, the system analyzes song attributes such as genre, mood, and energy to find songs with a similar “vibe.” Each song is scored based on how closely it matches the user’s preferences, and the highest-scoring songs are recommended. This project demonstrates the core ideas behind real-world recommendation systems in a simplified and interpretable way.

---

## How Real-World Recommenders Work

Real-world music recommendation systems like Spotify and YouTube use a combination of user data and song features to predict what users will enjoy. These systems collect input data such as songs a user has liked, skipped, or added to playlists, along with features like genre, mood, tempo, and listening history.

There are two main approaches. Collaborative filtering uses patterns from other users with similar behavior to suggest songs, while content-based filtering recommends songs with similar attributes to ones the user already likes.

In these systems, the input data (song features and user history) is combined with user preferences to calculate a relevance score for each song. The system then ranks all available songs and selects the highest-scoring ones to recommend. This ranking process is what determines what appears in a user’s feed or playlist.

## How The System Works

This recommender system works by comparing user preferences to song attributes and assigning each song a score based on how well it matches the user’s taste.

Each Song includes features such as genre, mood, energy, tempo_bpm, valence, and acousticness. These features represent different aspects of a song’s overall vibe, such as how energetic, emotional, or acoustic it feels.

The UserProfile stores the user’s preferences, including their favorite genre, favorite mood, target energy level, and whether they prefer acoustic music. These preferences define what kind of songs the system should prioritize.

### User Profile Example

The system uses a user profile to represent musical preferences. For example:

- Favorite genre: pop  
- Favorite mood: happy  
- Target energy: 0.8  
- Prefers acoustic: false  

This profile represents a user who enjoys upbeat, energetic music and prefers more produced (non-acoustic) sounds.

To generate recommendations, the system computes a score for each song using a combination of rules:

Songs receive a strong score boost if their genre matches the user’s favorite genre.  
Songs receive additional points if their mood matches the user's preferred mood, helping the system capture the emotional "vibe" the user is looking for.  
Numerical features like energy are scored based on how close they are to the user’s target value, so songs that closely match the desired energy receive higher scores.  
Songs may also receive a bonus if their acousticness matches the user’s preference.

After all songs are scored, the system ranks them from highest to lowest score and selects the top results as recommendations. This ensures that the songs returned are the best overall match for the user’s preferences.

### Algorithm Recipe

The recommender assigns a score to each song based on how well it matches the user's preferences.

* +2.0 points if the song's genre matches the user's favorite genre  
* +1.5 points if the song's mood matches the user's preferred mood  
* Songs receive additional points based on how close their energy level is to the user's target energy. Songs with similar energy are scored higher.  
* Songs are also adjusted based on whether they match the user's preference for acoustic or non-acoustic music  

After scoring all songs, the system sorts them from highest to lowest score and returns the top recommendations.

### Potential Bias

This system may over-prioritize genre, which could cause it to ignore songs from different genres that still match the user’s mood or energy. It also simplifies musical taste by focusing on a small set of features and does not account for real-world factors such as listening context or past behavior.

### System Flow

User Preferences → Score Each Song → Rank Songs → Return Top K Recommendations

First, the system reads the user’s preferences. Then it evaluates every song in the dataset using the scoring rules. After assigning scores, it sorts the songs from highest to lowest and returns the top results.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Below is an example of the recommender system output for a "pop/happy" user profile:

![CLI output](image.png)


Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

SS of profiles 

![alt text](image-1.png)
![alt text](image-2.png)


### Comparison of Results

The High-Energy Pop profile recommended songs like "Sunrise City" and "Gym Hero", which have high energy and match the pop genre. This shows that the system correctly prioritizes both genre and energy for upbeat music.

The Chill Lofi profile produced very different results, with songs like "Library Rain" and "Midnight Coding" appearing at the top. These songs have lower energy and higher acousticness, showing that the system adapts well to relaxed and acoustic preferences.

The Intense Rock profile strongly favored "Storm Runner", which matches both the rock genre and high energy level. Compared to the pop profile, the recommendations shifted toward more intense and aggressive songs.

Overall, the system responds well to different user preferences, but some songs like "Gym Hero" still appear across profiles due to strong energy similarity. This shows that energy has a strong influence on the scoring.


### Weight Shift Experiment

I modified the scoring system by reducing the importance of genre and increasing the importance of energy.

![alt text](image-3.png)

After this change, songs with similar energy levels appeared more frequently, even if they did not match the user’s preferred genre. This made the recommendations more diverse but sometimes less accurate in terms of musical style.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Architecture Diagram

```mermaid
flowchart TD
    A[User Profile Input] --> B[Recommender System]
    B --> C[Score Songs]
    C --> D[Top K Songs]
    D --> E[RAG Retriever]
    E --> F[Knowledge Base]
    F --> E
    E --> G[AI Explanation Generator]
    G --> H[Guardrail Validator]
    H --> I[Final Output to User]
```

---

## AI Extension (RAG-Based Recommender)

This project was extended with a Retrieval-Augmented Generation (RAG) system that enhances recommendation explanations.

The system now:

* Retrieves relevant music knowledge from a local knowledge base
* Combines that information with scoring results
* Generates more informative explanations
* Uses guardrails to ensure explanations reference actual song features

Example output:

* Song name
* Score
* Explanation + retrieved context

Run the extended pipeline with:

```bash
python src/main.py
python src/evaluate.py
```

---

## Sample Output

```
=== High-Energy Pop Profile ===

Sunrise City - Score: 6.16
Explanation: This song matches your preferences (genre match (+2.0), mood match (+1.5), energy similarity (+1.84), acoustic match (+0.82)). Context: High-energy songs are often good for workouts or parties because they have strong rhythm and fast tempo. Rock and intense songs usually feel powerful due to high energy and aggressive instruments.

Gym Hero - Score: 4.89
Explanation: This song matches your preferences (genre match (+2.0), energy similarity (+1.94), acoustic match (+0.95)). Context: Rock and intense songs usually feel powerful due to high energy and aggressive instruments. High-energy songs are often good for workouts or parties because they have strong rhythm and fast tempo.
```

The evaluation script reports guardrail pass rates across the three profiles, e.g. `Guardrail results: 9/9 passed`.

---

## Reliability / Guardrails

The system includes a validation step that checks whether explanations mention real song features like genre, mood, or energy.

If not, a warning is added. This prevents misleading or generic explanations.

The guardrail logic lives in `src/guardrails.py` and is invoked from `src/ai_assistant.py` after every explanation is generated. The evaluation script in `src/evaluate.py` reports how many explanations pass for a given run.

---

## Reflection

This project showed how even simple recommendation systems can feel intelligent when they combine data with structured reasoning.

Using AI tools helped speed up development, especially when generating boilerplate code and structuring new features like RAG. However, some AI suggestions needed to be verified manually, especially around logic correctness and imports.

One interesting insight was how small changes in scoring weights significantly affected recommendations. It also became clear how bias can easily emerge from limited datasets or overly strong features like genre.

If extended further, I would improve the system by increasing dataset size, adding personalization over time, and using more advanced similarity methods.

### Design Reflection

* AI helped with structure and speed, especially when scaffolding the RAG retriever and guardrail layer.
* AI sometimes gave incorrect imports or logic that did not match the existing module layout.
* Human verification was required to ensure the extension did not break the original recommender, scoring, or CSV loading code.

See also `model_card.md`:

[**Model Card**](model_card.md)


---

## 🧪 Experiments & Results

The following terminal screenshots show the recommender system running across three different user profiles, plus the evaluation script with guardrail results.

### High-Energy Pop Profile
![High Energy](image-1.png)

### Chill Lofi Profile
![Chill Lofi](image-2.png)

### Intense Rock + Guardrails
![Rock + Evaluation](image-3.png)

### Observations

- High-energy profiles return energetic songs (e.g. *Sunrise City*, *Gym Hero*, *Festival Lights*).
- Chill profiles return low-energy acoustic songs (e.g. *Library Rain*, *Midnight Coding*, *Deep Focus Waves*).
- The Rock profile prioritizes intense songs (e.g. *Storm Runner*, *Trap Thunder*).
- Some songs repeat across profiles due to strong energy weighting in the scoring rule.
- Guardrails passed successfully — every generated explanation referenced genre, mood, or energy (`9/9 passed`).

---
