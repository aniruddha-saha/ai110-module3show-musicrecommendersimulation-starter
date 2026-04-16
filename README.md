## Project Summary
This project builds a simple music recommender system using song features like genre, mood, and energy.
Instead of using complex machine learning, the system uses a scoring rule to compare songs with a user’s preferences. Each song is given a score based on how well it matches what the user likes, and the top songs are recommended.
This shows how real-world systems like Spotify can work at a basic level.

## How The System Works
Modern recommendation systems like Spotify combine user behavior and song features to predict what users will enjoy. These systems often use collaborative filtering (based on similar users) and content-based filtering (based on item attributes).
This project implements a simplified content-based recommender system.
Each song has features:
* genre
* mood
* energy (0 to 1)
The user profile defines preferences for these same features.
The system:
* Gives high points for exact matches (genre, mood)
* Computes similarity for energy based on closeness
* Combines everything into a final score
Songs are ranked by score, and the top K are returned.

## Algorithm Recipe
Each song is assigned a score based on the following:
* +40 points → Genre match
* +30 points → Mood match
* +0–20 points → Energy similarity
Energy similarity is computed as:
score = (1 - |song_energy - user_energy|) × 20
Total score = sum of all components
Songs are sorted by total score, and the top K are returned.

## Data Flow
flowchart TD
    A[User Preferences] --> B[Loop Through Songs]
    C[Song Dataset] --> B
    B --> D[Compute Score for Each Song]
    D --> E[Sort Songs by Score]
    E --> F[Top K Recommendations]

## Experiments I Tried
* Increasing energy weight made recommendations more diverse
* Reducing genre weight caused songs from different genres to appear
* Adding more songs improved variety across profiles

Limitations and Risks
* Very small dataset
* Does not learn from user behavior
* Strong bias toward genre matching
* Can create repetitive recommendations

Reflection
This project helped me understand how recommendation systems convert user preferences into scores and rankings.
Even with a simple rule-based system, the results can feel personalized. However, I also saw how bias can appear easily, especially when the system over-prioritizes one feature like genre.

Simple Explanation (Non-Technical)
The system recommends songs by checking how similar each song is to what the user likes.
It looks at genre, mood, and energy, gives each song a score, and then shows the highest scoring ones.
For example, if a user likes energetic pop music, songs with similar energy and genre will rank higher.