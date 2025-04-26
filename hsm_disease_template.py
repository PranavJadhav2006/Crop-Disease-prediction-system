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
    # Add a prefix for harvesting stage
    prefix = "hsm"  # harvesting stage maize
    
    if f"{prefix}_{disease_name}_index" not in st.session_state:
        st.session_state[f"{prefix}_{disease_name}_index"] = 0

    def next_image():
      if image_paths:
        st.session_state[f"{prefix}_{disease_name}_index"] = (st.session_state[f"{prefix}_{disease_name}_index"] + 1) % len(image_paths)

    def prev_image():
      if image_paths:
        st.session_state[f"{prefix}_{disease_name}_index"] = (st.session_state[f"{prefix}_{disease_name}_index"] - 1) % len(image_paths)

    st.markdown(f"<h3 style='color: #228B22; text-align: center;'>{disease_name}</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 4, 1])

    with col1:
        if st.button("◀", key=f"{prefix}_prev_{disease_name}_{disease_index}"):
            prev_image()

    with col2:
        if image_paths:
            current_image = load_image(image_paths[st.session_state[f"{prefix}_{disease_name}_index"]])
            if current_image:
                st.image(current_image,width=600, caption=disease_name)
        else:
            st.warning("⚠ No images available for this disease.")

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

def render_corn_harvesting_diseases():
    IMAGE_FOLDER = "img2"
   
      # Harvesting Stage Diseases (Corn)
    st.markdown("## 🌽 Harvesting Stage (Corn)")

    disease_data = [
         ("Fusarium Ear Rot (Fungus)",[os.path.join("img2", "fusarium-ear-rot-maize-1.jpg"),os.path.join("img2", "fusarium-ear-rot-maize-2.jpg"),os.path.join("img2", "fusarium-ear-rot-maize-3.jpg")],
         """• White, pink, or reddish mold on maize kernels  
            • Kernels may appear shrunken and discolored  
            • Produces harmful mycotoxins affecting grain safety""",
         """• Harvest maize at proper moisture levels  
            • Store grain in dry, well-ventilated conditions  
            • Use fungicide-treated seeds to reduce infections""",
         """• Caused by *Fusarium verticillioides*  
            • Spreads through airborne spores and insect damage  
            • More common in warm, humid conditions"""),

         ("Banded Leaf and Sheath Blight (Fungus)", [os.path.join("img2", "banded-leaf-and-sheath-blight-maize-1.jpg"),os.path.join("img2", "banded-leaf-and-sheath-blight-maize-2.jpg"),os.path.join("img2", "banded-leaf-and-sheath-blight-maize-3.jpg"),os.path.join("img2", "banded-leaf-and-sheath-blight-maize-4.jpg")],
         """• Brown, band-like lesions on leaves and sheaths  
            • White fungal growth between leaf layers  
            • Reduces grain yield and weakens plants""",
         """• Plant resistant maize hybrids  
            • Remove infected crop residues to prevent spread  
            • Apply foliar fungicides during early infection""",
         """• Caused by *Rhizoctonia solani*  
            • Spreads through soil and plant debris  
            • Thrives in high moisture conditions"""),

         ("Fruit Molds (Fungus)",[os.path.join("img2", "fruit-molds-1 (1).jpg"),os.path.join("img2", "fruit-molds-1.jpg")],
         """• Various molds (green, blue, white) covering maize kernels  
            • Kernels become soft, decayed, and foul-smelling  
            • Some molds produce harmful mycotoxins""",
         """• Dry maize properly before storage  
            • Store grain in moisture-proof containers  
            • Inspect stored grain regularly for mold growth""",
         """• Caused by multiple fungal species (*Aspergillus*, *Penicillium*, etc.)  
            • Develops in humid storage conditions  
            • Spreads through contaminated kernels"""),

         ("Spiny Bollworm (Insect)",[os.path.join("img2", "spiny-bollworm-cotton-1.jpg")],
         """• Larvae bore into maize ears, feeding on kernels  
            • Leaves silk webbing and frass inside the cob  
            • Reduces grain quality and market value""",
         """• Use pheromone traps to monitor infestations  
            • Apply biological control agents like *Bacillus thuringiensis*  
            • Rotate crops to break the pest cycle""",
         """• Caused by *Earias vittella* larvae  
            • More common in tropical maize-growing regions  
            • Prefers warm, humid environments"""),

         ("Leaf Footed Bugs (Insect)",[os.path.join("img2", "Leaf-Footed-Bugs.1.jpg"),os.path.join("img2", "Leaf-Footed-Bugs.2.jpg")],
         """• Pierces and sucks sap from maize kernels  
            • Leaves sunken, shriveled spots on grains  
            • Can transmit plant pathogens""",
         """• Use insecticidal soap or neem oil sprays  
            • Introduce natural predators like assassin bugs  
            • Remove weeds that provide shelter for pests""",
         """• Various species, including *Leptoglossus* spp.  
            • Feeds on multiple crops, including maize  
            • More active in warm, dry conditions"""),
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
        
render_corn_harvesting_diseases()