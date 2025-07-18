# 🎬📺 Anime & Movie Recommender System

A unified recommendation system that suggests similar **anime** or **movies** based on the title you enter. It uses two separate datasets—anime (~12,000 entries) and movies (~5,000 entries)—to provide smart, content-based recommendations.

Built with **Python**, **scikit-learn**, **pandas**, and **Streamlit**.

---

## 🚀 Features

- 🔍 Choose between Anime or Movie recommendations
- 🎯 Content-based filtering using TF-IDF Vectorization
- 📊 Clean tabular output using Pandas DataFrame
- 🧠 Intelligent similarity search
- 📁 Separate recommendation logic for anime and movies

---

## 📂 Project Structure

```
├── anime.csv
├── movies.csv
├── app.py
├── util.py
├── animerec.ipynb
├── PRJ Movie Recommendation.ipynb
└── README.md
```

---

## ⚠️ Disclaimer

The recommendation system is trained on a larger **anime dataset (~12k rows)** compared to the **movie dataset (~5k rows)**. So, results for anime may be more accurate or detailed. Movie recommendations will still work well but may benefit from more data in future versions.

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 📚 Datasets

- `anime.csv`: Contains anime metadata including titles, genres, and descriptions.
- `movies.csv`: Contains movie titles, genres, and short summaries.

---

## 🛠 Tech Stack

- Python
- Pandas
- scikit-learn
- Streamlit
- TF-IDF Vectorizer

---

## 🤝 Contributions

Feel free to fork this repo, raise issues, or submit pull requests.

---

## 📄 License

This project is licensed under the MIT License.
