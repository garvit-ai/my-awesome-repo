import streamlit as st
from PIL import Image

# Simulating the C++ "sum" class
class Sum:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def __eq__(self, other):
        # This mimics your original print logic
        result = f"{other.num1} + {other.num2} = dekho verma zada bakchodi krne ki adat nhi hai hame"
        return result

# Streamlit UI
st.title("Calculator")

# Input fields (plain text boxes)
num1 = st.text_input("Enter first number")
num2 = st.text_input("Enter second number")

# Validate inputs and proceed
if st.button("Add"):
    try:
        # Convert to integers
        num1_int = int(num1)
        num2_int = int(num2)

        # Assign to objects
        s1 = Sum()
        s1.num1 = num1_int
        s1.num2 = num2_int

        s3 = Sum()
        result = s3.__eq__(s1)

        # Display result and image
        st.success(result)
        image = Image.open("verma.jpeg")
        st.image(image, caption="Bakchod Verma ", use_container_width=True)
    
    except ValueError:
        st.error("Please enter valid numbers.")
