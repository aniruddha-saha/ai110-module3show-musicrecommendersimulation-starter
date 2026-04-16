
## Goal / Task
This system recommends songs based on a user’s preferences for genre, mood, and energy. It tries to suggest songs that feel similar to what the user already likes.

## Data Used
The dataset contains around 15–20 songs.
Each song includes:
* genre
* mood
* energy (0–1)
* optional features like tempo and valence
The dataset is small and not balanced across genres, so some types of music appear more often than others.

### Algorithm Summary
Each song is given a score based on how well it matches the user’s preferences.
* Genre match → highest weight
* Mood match → medium weight
* Energy similarity → based on closeness
All scores are added together, and songs are ranked from highest to lowest.

## Observed Behavior / Biases
For the "High Energy Pop" profile, songs like "Sunrise City" ranked highest due to strong genre and mood matches and similar energy.
For the "Chill Lofi" profile, lower energy songs were prioritized, showing that energy strongly affects ranking.
For the "Intense Rock" profile, high-energy songs were recommended even when genre did not match perfectly.
In the edge case (conflicting preferences), results were less intuitive, showing limitations of the scoring system.
The system strongly favors genre matching, which can create a filter bubble where users only see similar music.
If the dataset has more songs from one genre (like pop), those songs will be recommended more often.

## Evaluation Process
I tested the system using different user profiles:
* High Energy Pop
* Chill Lofi
* Intense Rock
* Edge case with conflicting preferences
I also changed weights (increasing energy importance) and observed how recommendations changed.
This helped me understand how each feature affects the output.

## Intended Use and Non-Intended Use
Intended Use:
* Educational demonstration
* Understanding recommendation systems
* Simple simulation of content-based filtering
Not Intended For:
* Real-world music apps
* Large-scale recommendation systems
* Personalized systems using real user data

##  Limitations
* Small dataset
* No learning from user behavior
* Fixed weights
* Limited features
The system also may bias toward mid-energy songs due to how similarity is computed.

##  Bias + Filter Bubble
The system may over-recommend songs that match the user’s initial preferences, especially genre.
This creates a filter bubble where users are repeatedly exposed to the same type of music.
If the dataset is imbalanced, some genres will dominate recommendations.

## Future Improvements
* Add collaborative filtering
* Learn weights from data
* Improve diversity in recommendations
* Add more features (tempo, valence, danceability)

## Personal Reflection
My biggest learning moment was seeing how simple scoring rules can still produce meaningful recommendations.
Even without machine learning, combining features like genre, mood, and energy gives results that feel personalized.
AI tools helped speed up coding and debugging, but I had to double-check outputs because small mistakes caused errors.
What surprised me most is how “intelligent” a simple system can feel. Changing the user profile changes recommendations in a noticeable way.
If I continued this project, I would add more features and explore collaborative filtering to make it more realistic.