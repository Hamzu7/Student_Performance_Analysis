# 📊 Student Performance Analysis

This project analyzes a dataset of students’ academic performance to uncover how various factors like parental education, test preparation, lunch type, sports activity, and study hours impact student scores.

## 🔧 Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## 📂 Dataset

Dataset: `Expanded_data_with_more_features.csv`  
It includes features like:
- Math, Reading, Writing Scores
- Weekly Study Hours
- Number of Siblings
- Practice Sport Frequency
- Parent Education & Marital Status
- Test Preparation Completion
- Lunch Type
- Ethnic Group

## 🧼 Data Cleaning Steps

- Removed irrelevant columns (`Unnamed: 0`, `TransportMeans`)
- Filled missing values using appropriate strategies (mode, median, grouped mode)
- Removed duplicate records
- Added a new column `Total` for combined scores

## 📊 Exploratory Data Analysis (EDA)

Key analysis and insights:
- **Test Preparation:** Students who completed test prep scored higher across all subjects.
- **Lunch Type:** Those who had "standard" lunch performed better than those on free/reduced lunch.
- **Parental Education:** Higher parental education generally corresponds to higher scores.
- **Practice Sport:** Regular sports activity is slightly linked to improved performance.
- **First Child:** Being the first child has a small positive impact.
- **Study Hours:** Students studying more than 10 hours weekly had the best scores.
- **Siblings Count:** A slight decline in scores as the number of siblings increases.
- **Top Performers:** Identified top 10 students based on total score.

## 📈 Visualizations

- Heatmaps for score comparisons
- Countplots and Pie charts for distribution
- Boxplots to analyze score spread
- Line and bar plots for trend analysis

## 🏁 Conclusion

This project demonstrates how socio-academic factors influence student performance and provides practical insights using Python-based data analysis.

## 🚀 Future Work

- Model building to predict student scores
- More advanced feature engineering
- Interactive dashboard (e.g., using Streamlit)

---

⭐ **Feel free to fork, explore, and connect!**

