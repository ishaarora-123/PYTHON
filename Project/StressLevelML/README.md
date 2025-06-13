🌿 Stress Level Prediction App (1–10 Scale)
👋 About the Project
~ Ever wondered how your hobbies, social habits, or weekly routine might affect your stress levels?
~ This project is built to predict your stress level on a scale of 1 to 10 using your personal inputs — like how often you engage in hobbies, whether you prefer being         alone or with friends, and how you rate your own mental well-being.
~ I trained a Decision Tree Regressor model to learn from patterns insuch data, and built a simple app where you can try it out yourself!

🎯 Why I Made This
~ Mental health is deeply personal, yet often influenced by our everyday choices. With this app, I wanted to create something that:
~ Helps you understand your stress levels better
~ Encourages reflection on your daily habits
~ Shows how data and technology can support well-being

🧪 What Goes Into the Prediction?
Here are the inputs the model looks at:
| Column               | Description                                                    |
| -------------------- | -------------------------------------------------------------- |
| `Name`               | First name (optional — not used in prediction)                 |
| `AgeGroup`           | Age range (e.g., 18–24)                                        |
| `Gender`             | Self-identified gender                                         |
| `Hobbies`            | Types of hobbies (e.g., Creative, Social, Intellectual)        |
| `Frequency`          | How often hobbies are done (e.g., Several times a week)        |
| `HoursPerWeek`       | Time spent weekly on hobbies                                   |
| `CurrentStressLevel` | How stressed the person *feels* (Low/Moderate/High)            |
| `MoodEffect`         | Whether the activity helps mood                                |
| `Benefits`           | Self-perceived benefits (Relaxation, Focus, etc.)              |
| `SocialContext`      | Whether done alone or with others                              |
| `StressLevel`        | 🎯 **Target value** — model tries to predict this (scale 1–10) |

🧠 How the Model Works
Model: Decision Tree Regressor
Why? It’s beginner-friendly, interpretable, and works well for small datasets.
Libraries Used:
~ pandas, numpy for data handling
~ scikit-learn for modeling
~ pickle for saving the trained model
~ streamlit for the web app

🚀 What's Next?
~ Improve predictions by training on more data
~ Try different models (e.g., Random Forest, XGBoost)
~ Add explanations for why a certain stress level is predicted
~ Offer suggestions to lower stress based on the inputs
