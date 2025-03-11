import gradio as gr
import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


def predict_price(house_size, num_rooms):
   
    prediction = float(model.predict([[house_size, num_rooms]])[0])
    return f"Predicted House Price: ${prediction:.2f}"


iface = gr.Interface(
    fn=predict_price,  
    inputs=[
        gr.Number(label="House Size (in square meters)"), 
        gr.Number(label="Number of Rooms") 
    ],
    outputs=gr.Textbox(label="Predicted Price"), 
    title="House Price Prediction",  
    description="Enter house size and number of rooms to get the predicted price of the house."  # Description
)
iface.launch()
