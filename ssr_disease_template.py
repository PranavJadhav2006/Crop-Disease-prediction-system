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
    # Add prefix for rice seedling stage
    prefix = "ssr"  # seedling stage rice
    
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
                st.image(current_image, width=600, caption=disease_name)

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

def render_rice_seedling_diseases():
    IMAGE_FOLDER = "img1/"

    disease_data = [
         ("Bottom Rot (Fungus)", [os.path.join("img1", "bottom-rot-lettuce-1.jpg")],
         """• Yellowing and wilting of lower leaves  
            • Rotting of the seedling base  
            • Weak root system and plant collapse""",
         """• Use well-drained soil to prevent excessive moisture  
            • Avoid overwatering to reduce fungal growth  
            • Use fungicide-treated seeds to prevent infections""",
         """• Caused by *Rhizoctonia solani*, a soil-borne fungus  
            • Thrives in high moisture and poorly aerated soil  
            • Spreads through infected soil and plant debris"""),

         ("Stackburn of Rice (Fungus)", [os.path.join("img1", "stackburn-of-rice-rice-.jpg"),os.path.join("img1", "stackburn-of-rice-rice-1.jpg"),os.path.join("img1", "stackburn-of-rice-rice-2.jpg"),os.path.join("img1", "stackburn-of-rice-rice-3.jpg")],
         """• Brown necrotic spots with yellow margins on leaves  
            • Affected areas turn reddish-brown and dry up  
            • Severely infected seedlings may die""",
         """• Use disease-resistant rice varieties  
            • Maintain good field sanitation by removing infected debris  
            • Apply recommended fungicides during early symptoms""",
         """• Caused by *Alternaria padwickii*, a fungal pathogen  
            • Favors high humidity and warm temperatures  
            • Spread through infected seeds and plant debris"""),

         ("Aphids (Insect)", [os.path.join("img1", "aphids-rice-1.jpg"),os.path.join("img1", "aphids-rice-2.jpg")],
         """• Leaves curl and turn yellow due to sap-sucking  
            • Sticky honeydew secretions attract ants  
            • Plants show stunted growth and reduced vigor""",
         """• Introduce natural predators like ladybugs and lacewings  
            • Use neem oil sprays to repel aphids naturally  
            • Apply systemic insecticides in severe infestations""",
         """• Small, soft-bodied insects that suck plant sap  
            • Reproduce rapidly under warm and dry conditions  
            • Can transmit viral diseases to plants"""),

         ("Termites (Insect)", [os.path.join("img1", "termites-1.jpg")],
         """• Hollowed-out plant stems and weakened roots  
            • Seedlings can be pulled from soil easily  
            • Presence of mud tubes in affected fields""",
         """• Apply termiticides to soil before planting  
            • Use neem cake or organic barriers for protection  
            • Reduce excessive crop residues that attract termites""",
         """• Colonies of termites feed on plant roots and stems  
            • Thrive in dry conditions and organic debris  
            • Cause major losses in poorly managed fields"""),

         ("Rice Case Worm (Insect)", [os.path.join("img1", "rice-case-worm-1.jpg"),os.path.join("img1", "rice-case-worm-3.jpg"),os.path.join("img1", "Rice-Case-Worm-2.jpg")],
         """• Irregular feeding scars on leaves  
            • Larvae create floating leaf cases on water surface  
            • Affected leaves turn white and dry up""",
         """• Use light traps to monitor and control adult moths  
            • Maintain proper water levels to discourage larvae  
            • Apply biological pesticides like *Bacillus thuringiensis*""",
         """• Caused by *Nymphula depunctalis*, a moth species  
            • Eggs are laid on leaves and hatch into larvae  
            • Spreads rapidly in stagnant water fields"""),

         ("Demerara Froghopper (Insect)", [os.path.join("img1", "demerara-froghopper-rice-1.jpg")],
         """• Wilting and yellowing of seedlings  
            • White frothy secretions around base of plants  
            • Reduced tillering and poor crop establishment""",
         """• Introduce natural predators like spiders and beetles  
            • Remove grassy weeds that act as alternate hosts  
            • Apply insecticidal soap sprays in early infestations""",
         """• Caused by *Aeneolamia varia*, a sap-sucking insect  
            • Prefers high moisture environments  
            • Spreads through contaminated irrigation water"""),

         ("Rice Leaf Mite (Mite)", [os.path.join("img1","rice-leaf-mite-1.jpg"),os.path.join("img1","rice-leaf-mite-2.jpg")],
         """• Tiny reddish mites visible under magnification  
            • Leaves show white speckling and curling  
            • Severe infestations cause leaf drying""",
         """• Increase humidity to discourage mite reproduction  
            • Introduce predatory mites to control populations  
            • Use miticides in severe cases""",
         """• Caused by *Oligonychus oryzae*, a tiny mite species  
            • Thrives in dry, hot conditions  
            • Spreads through wind and infected plants"""),
      ]

    
      # Seedling Stage Diseases (Rice)
    st.markdown("## 🌱 Seedlingage (Rice)")

    for i, disease in enumerate(disease_data):
       
        disease_template(
            disease_name=disease[0],
            image_paths=disease[1],
            symptoms=disease[2],
            prevention=disease[3],
            causes=disease[4],
            disease_index=i 
           )

render_rice_seedling_diseases()