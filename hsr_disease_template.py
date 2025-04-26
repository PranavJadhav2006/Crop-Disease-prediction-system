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
    # Add prefix for rice harvesting stage
    prefix = "hsr"  # harvesting stage rice
    
    if f"{prefix}_{disease_name}_index" not in st.session_state:
        st.session_state[f"{prefix}_{disease_name}_index"] = 0

    def next_image():
      if image_paths:
        st.session_state[f"{prefix}_{disease_name}_index"] = (st.session_state[f"{prefix}_{disease_name}_index"] + 1) % len(image_paths)

    def prev_image():
      if image_paths:
        st.session_state[f"{prefix}_{disease_name}_index"] = (st.session_state[f"{prefix}_{disease_name}_index"] - 1) % len(image_paths)

    # **Title Section (NOT inside any container)**
    st.markdown(f"<h3 style='color: #228B22; text-align: center;'>{disease_name}</h3>", unsafe_allow_html=True)

    # **Image Navigation**
    col1, col2, col3 = st.columns([1, 4, 1])

    with col1:
        if st.button("◀", key=f"{prefix}_prev_{disease_name}_{disease_index}"):
            prev_image()

    with col2:
        if image_paths:
            current_image = load_image(image_paths[st.session_state[f"{prefix}_{disease_name}_index"]])
            if current_image:
                st.image(current_image, width=700, caption=disease_name)

    with col3:
        if st.button("▶", key=f"{prefix}_next_{disease_name}_{disease_index}"):
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

def render_rice_harvesting_diseases():
    IMAGE_FOLDER = "img1/"

    # Harvesting Stage Diseases (Rice)
    st.markdown("## 🌾 Harvesting Stage (Rice)")

    disease_data = [
        ("Rice Panicle Mite (Mite)", [os.path.join("img1", "rice-panicle-mite-rice-1.jpg"),os.path.join("img1", "rice-panicle-mite-rice-2.jpg"),os.path.join("img1", "rice-panicle-mite-rice-3.jpg"),os.path.join("img1", "rice-panicle-mite-rice-4.jpg")],
        """• Causes curling and discoloration of panicles  
            • Affected grains become shriveled  
            • Reduces grain quality and weight""",
        """• Spray miticides like sulfur or abamectin  
            • Avoid excess nitrogen fertilizers  
            • Remove infected plant debris""",
        """• Caused by *Steneotarsonemus spinki*  
            • Spread through contaminated seeds and wind  
            • Favors hot and humid conditions"""),

        ("Bacterial Panicle Blight (Bacteria)", [os.path.join("img1", "bacterial-blight-of-rice-rice-1.jpg"),os.path.join("img1", "bacterial-blight-of-rice-rice-2.jpg"),os.path.join("img1", "bacterial-blight-of-rice-rice-3.jpg"),os.path.join("img1", "bacterial-blight-of-rice-rice-4.jpg")],
        """• Grains turn brown and fail to develop  
            • High temperatures increase disease severity  
            • Reduced yield and poor grain quality""",
        """• Use certified disease-free seeds  
            • Avoid excessive nitrogen fertilizers  
            • Improve field drainage to reduce moisture""",
        """• Caused by *Burkholderia glumae*  
            • Spread through infected seeds and insects  
            • Thrives in warm, wet climates"""),

        ("Leaf-Footed Bug (Insect)", [os.path.join("img1", "Leaf-Footed-Bug.jpg")],
        """• Pierces and sucks sap from developing grains  
            • Causes empty or shriveled grains  
            • Leaves brown scars on grain surfaces""",
        """• Use insecticidal sprays like neem oil  
            • Remove alternate host plants  
            • Encourage natural predators like spiders""",
        """• Caused by *Leptoglossus phyllopus*  
            • Spread through flying adults and eggs  
            • Prefers warm, dry environments"""),

        ("Short-Horned Grasshopper & Locust (Insect)", [os.path.join("img1", "Short-Horned-Grasshopper-Locust.1.jpg"),os.path.join("img1", "Short-Horned-Grasshopper-Locust.2.jpg")],
        """• Defoliation of plants, leading to low yield  
            • Feeds on developing grains  
            • Severe outbreaks cause massive crop losses""",
        """• Use biological control methods (fungal biopesticides)  
            • Apply insecticides in early infestation  
            • Implement cultural control by removing weeds""",
        """• Caused by *Acrididae family*  
            • Thrives in dry conditions  
            • Swarms migrate and damage crops quickly"""),
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
        
render_rice_harvesting_diseases()