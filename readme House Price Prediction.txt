#24rp13777
# House Price Prediction

## Overview

This project is a *House Price Prediction* system built using *Machine Learning*. Users can input the number of rooms and the area of a house (in square meters), and the model will predict the estimated price.
## we provide screenshots of our model that show GUI (Graphical user interface) 

We provide two implementations:

1. *Gradio-based Web UI* (for quick model testing and demo)
2. *Flask-based API* (for backend integration with other systems)

## Features

- *Machine Learning Model* trained on housing data
- *Gradio Web Interface* for user-friendly interaction
- *Flask API* for backend usage
- *Pickle Serialization* to save and load the trained model

## Technologies Used

- Python
- Scikit-learn (for model training)
- Gradio (for web UI)
- Flask (for API backend)
- Pickle (for saving/loading models)

---

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train and Save the Model

Run the following script to train a model and save it as model.pkl:

```bash
python train_model.py
```

---

## Running the Application

### *1. Using Gradio (Web UI)*

To launch the Gradio-based web interface, run:

```bash
python app.py
```

After running the command, a link will be generated where users can interact with the model via a browser.

### *2. Using Flask (API Server)*

To start the Flask API, run:

```bash
python server.py
```

The API will be available at: http://127.0.0.1:5000/predict

---

## Usage Guide

### *1. Gradio Web UI*

- Open the *Gradio link* in your browser.
- Enter House Size (sqm) and Number of Rooms.
- Click Submit to get the predicted price.

## File Structure

```
├── house-price-prediction/
│   ├── train_model.py      # Train and save ML model
│   ├── model.pkl           # Saved model
│   ├── gradio_app.py       # Gradio-based UI
│   ├── flask_app.py        # Flask API server
│   ├── requirements.txt    # Python dependencies
│   ├── README.md           # Project documentation
```

---

## License

This project is licensed under the Group_1 License.

---
