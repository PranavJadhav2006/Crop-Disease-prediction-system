import streamlit as st
import os
from PIL import Image

# Function to check if image exists
def load_image(image_path):
    if os.path.exists(image_path):
        st.write(f"✅ Loading image: {image_path}")
        img = Image.open(image_path)
        
        # Resize to fixed square (300x300 pixels)
        img = img.resize((300, 300))  # Adjust size as needed

        return img
    else:
        st.warning(f"⚠ Image not found: {image_path}")
        return None

# Disease Template Function
def disease_template(disease_name, image_paths, symptoms, prevention, causes, disease_index):
    if f"{disease_name}_index" not in st.session_state:
        st.session_state[f"{disease_name}_index"] = 0

    def next_image():
      if image_paths:
        st.session_state[f"{disease_name}_index"] = (st.session_state[f"{disease_name}_index"] + 1) % len(image_paths)

    def prev_image():
      if image_paths:
        st.session_state[f"{disease_name}_index"] = (st.session_state[f"{disease_name}_index"] - 1) % len(image_paths)

    # **Title Section (NOT inside any container)**
    st.markdown(f"<h3 style='color: #228B22; text-align: center;'>{disease_name}</h3>", unsafe_allow_html=True)

    # **Image Navigation**
    col1, col2, col3 = st.columns([1, 4, 1])

    with col1:
        if st.button("◀", key=f"prev_{disease_name}_{disease_index}"):
            prev_image()

    with col2:
        if image_paths:
            current_image = load_image(image_paths[st.session_state[f"{disease_name}_index"]])
            if current_image:
                st.image(current_image, width=600, caption=disease_name)
        else:
            st.warning("⚠ No images available for this disease.")

    with col3:
        if st.button("▶", key=f"next_{disease_name}_{disease_index}"):
            next_image()

    # **Separators to prevent nesting issues**
    st.markdown("---")

    # **Expanders (Not Nested)**
    with st.expander("🩺 Symptoms", expanded=False):
        st.write(symptoms)

    with st.expander("🛡 Prevention Measures", expanded=False):
        st.write(prevention)

    with st.expander("🦠 Causes", expanded=False):
        st.write(causes)

def render_wheat_harvesting_diseases():
    IMAGE_FOLDER = "img/"

    disease_data = [
            ("Loose Smut of Wheat (Fungus)", [os.path.join("img", "loose-smut-of-wheat-wheat-1.jpg"), os.path.join("img", "loose-smut-of-wheat-wheat-2.jpg"),os.path.join("img", "loose-smut-of-wheat-wheat-3.jpg")],
             """• Infected heads appear black and powdery  
                • Grains replaced by black fungal spores  
                • Entire ear gets destroyed before maturity""",
             """• Use certified, disease-free seeds  
                • Apply systemic fungicides before sowing  
                • Remove and burn infected plants to prevent spread""",
             """• Caused by *Ustilago tritici* fungus  
                • Spreads through infected seeds  
                • Becomes active under cool, humid conditions"""),

            ("Karnal Bunt of Wheat (Fungus)",[os.path.join("img", "karnal-bunt-of-wheat-wheat-1.jpg"), os.path.join("img", "karnal-bunt-of-wheat-wheat-2.jpg")],
             """• Partial replacement of wheat grains by black spores  
                • Foul, fishy smell in infected grains  
                • Grain discoloration and shriveling""",
             """• Use resistant wheat varieties  
                • Treat seeds with fungicides before planting  
                • Avoid late sowing to reduce disease incidence""",
             """• Caused by *Tilletia indica* fungus  
                • Spreads through wind-borne spores  
                • Favors cool, moist conditions during flowering"""),

            ("Fusarium Head Blight (Fungus)", [os.path.join("img", "fusarium-head-blight-1.jpg"), os.path.join("img", "fusarium-head-blight-wheat-2.jpg"),os.path.join("img", "fusarium-head-blight-wheat-3.jpg")],
             """• Bleaching of wheat heads, especially in patches  
                • Grains appear shriveled and lightweight  
                • Pinkish fungal growth on spikelets""",
             """• Avoid excessive nitrogen fertilization  
                • Rotate crops to break the fungal cycle  
                • Apply fungicides at early flowering stages""",
             """• Caused by *Fusarium graminearum* fungus  
                • Spreads through infected crop residues  
                • Thrives in warm, humid conditions"""),

            ("Common Bunt of Wheat (Fungus)", [os.path.join("img", "common-bunt-of-wheat-1.jpg")],
             """• Grains replaced by dark, foul-smelling fungal masses  
                • Stunted plant growth and low yield  
                • Black spore balls develop inside infected kernels""",
             """• Use fungicide-treated seeds  
                • Clean equipment to prevent spore transmission  
                • Remove and destroy infected crops""",
             """• Caused by *Tilletia caries* and *Tilletia foetida* fungi  
                • Spores survive in soil and infect new crops  
                • Spreads through contaminated seeds""")
        ]

    for i, disease in enumerate(disease_data):
       
        disease_template(
            disease_name=disease[0],
            image_paths=disease[1],
            symptoms=disease[2],
            prevention=disease[3],
            causes=disease[4],
            disease_index=i 
           )

render_wheat_harvesting_diseases()