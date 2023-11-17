**Machine Learning for Kickstarter Project Status Prediction**

In this project, I developed a machine learning program to predict the success or failure status of Kickstarter projects based on their descriptions. The program utilizes three different machine learning models: Decision Tree, K-Nearest Neighbors (KNN), and Neural Network. The project involves data preprocessing, model training, and evaluation using standard metrics.

Key Components and Techniques:

1. Data Preprocessing:

- Utilized the pandas library to load and filter Kickstarter project data from a CSV file.

- Removed projects with statuses "Cancelled by Creator" and "Cancelled by Kickstarter."

- Processed project descriptions and statuses into arrays for model training.

2. Text Vectorization:

- Created a document-term matrix using the CountVectorizer from scikit-learn.

- Applied stop-word removal using NLTK to enhance feature quality.

- Limited the features to the top 1000 most frequent words.

3. Machine Learning Models:

- Developed functions for training Decision Tree, KNN, and Neural Network models.

- Implemented error handling to address potential file loading issues.

- Split the data into training and test sets for model evaluation.

4. Model Training and Evaluation:

- Trained each model on the preprocessed data.

- Computed and displayed accuracy for each model.

- Utilized scikit-learn metrics for accuracy assessment.

5. Confusion Matrix and Classification Report:

- Created a function to generate confusion matrices and classification reports.

- Plotted and displayed confusion matrices using Matplotlib.

- Outputted detailed classification reports for model performance evaluation.

6. Model Persistence:

- Saved the most accurate model (Neural Network) to a file using joblib for future use.

Results:

- The Decision Tree, KNN, and Neural Network models were trained and evaluated on Kickstarter project data.

- The Neural Network model demonstrated the highest accuracy among the three models.

- Confusion matrices and classification reports provide insights into the models' strengths and weaknesses.

This project showcases my proficiency in data preprocessing, machine learning model implementation, and model evaluation using popular Python libraries such as pandas, scikit-learn, NLTK, and Matplotlib. The code is designed to be modular, making it adaptable for different datasets and machine learning tasks.

**Real-time Earthquake Data Analysis and Visualization**

In this project, I designed a Python program to fetch, process, and analyze real-time earthquake data from the USGS Earthquake Hazards Program API. The program retrieves earthquake information, including magnitude, location, and occurrence time, and then enhances the data with geographical details using the OpenCage Geocoding API. The final output is stored in a CSV file for further analysis or visualization.

Key Features and Components:

1. Data Retrieval:

- Utilized the `requests` library to fetch real-time earthquake data from the USGS API in GeoJSON format.

2. Data Processing:

- Extracted relevant earthquake information such as magnitude, occurrence time, and geographic coordinates from the API response.

- Implemented functions to convert timestamps, adjust for time zones, and enhance location details.

3. Geocoding:

- Integrated the OpenCage Geocoding API to obtain additional information about the earthquake locations, including county and state.

4. CSV File Generation:

- Created a CSV file containing the processed earthquake data for easy storage, sharing, and further analysis.

5. User-Friendly Output:

- Developed a user-friendly output that displays earthquake details, including magnitude, occurrence time, and precise location information (latitude, longitude, county, state).

6. Error Handling:

- Implemented error handling to manage potential connection issues with the APIs, ensuring a smooth user experience.

Results and Output:

- The program successfully fetches real-time earthquake data, processes it, and enriches it with additional geospatial details.

- The final output includes a user-friendly display of earthquake details and a CSV file containing a comprehensive dataset for further analysis.

Skills Demonstrated:

- API integration and data retrieval using the `requests` library.

- Data processing and manipulation using Python's `datetime`, `json`, and `xmltodict` libraries.

- Geocoding implementation for location enhancement.

- CSV file handling and data storage for easy accessibility and analysis.

This project showcases my ability to work with real-time data, integrate external APIs, and create a structured and user-friendly output. The code is designed to be flexible, allowing for easy adaptation to different datasets or APIs.