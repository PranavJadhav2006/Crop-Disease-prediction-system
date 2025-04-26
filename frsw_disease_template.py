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
    # Add prefix for wheat fruiting stage
    prefix = "frsw"  # fruiting stage wheat
    
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

def render_wheat_fruiting_diseases():
    IMAGE_FOLDER = "img/"

    disease_data = [
            ("Foot and Collar Rot (Fungus)", [os.path.join("img", "foot-and-collar-rot-1.jpg"), os.path.join("img", "foot-and-collar-rot-chickpea-1.jpg")],
             """• Reddish-brown rot at the base of the plant  
                • Wilting and yellowing of leaves  
                • Stem weakening, leading to plant collapse""",
             """• Improve soil drainage to prevent waterlogging  
                • Use fungicide applications in early growth stages  
                • Rotate crops to reduce fungal presence in soil""",
             """• Caused by *Fusarium spp.* and *Rhizoctonia spp.* fungi  
                • Spreads through infected plant debris  
                • Moist soil conditions promote infection"""),

            ("Take-All (Fungus)", [os.path.join("img", "Take-All-1.jpg"), os.path.join("img", "Take-All-2.jpg"),os.path.join("img", "Take-All-3.jpg")],
             """• Blackened roots and lower stem  
                • Stunted plant growth and reduced tillering  
                • Leaves turn yellow and die prematurely""",
             """• Maintain proper soil pH with balanced fertilization  
                • Use resistant wheat varieties  
                • Practice crop rotation with non-host crops""",
             """• Caused by *Gaeumannomyces graminis* fungus  
                • Thrives in alkaline soils with high nitrogen levels  
                • Spreads through infected root residues"""),

            ("Wheat Blast (Fungus)", [os.path.join("img", "wheat-blast--wheat-1.jpg"), os.path.join("img", "wheat-blast--wheat-2.jpg"),os.path.join("img", "Wheat-Blast-3.jpg"),os.path.join("img", "wheat-blast--wheat-4.jpg")],
             """• Grayish lesions on spikes, preventing grain formation  
                • Premature bleaching of wheat heads  
                • Sudden yield loss in heavily infected fields""",
             """• Apply fungicides at the flag leaf and head emergence stage  
                • Avoid excessive nitrogen fertilization  
                • Remove infected plant residues""",
             """• Caused by *Magnaporthe oryzae* fungus  
                • Spreads through airborne spores in humid conditions  
                • Can survive on alternative grass hosts"""),

            ("Root and Foot Rot (Fungus)", [os.path.join("img", "root-and-foot-rot-1.jpg"), os.path.join("img", "root-and-foot-rot-2.jpg"), os.path.join("img", "root-and-foot-rot-3.jpg")],
             """• Dark brown to black root and stem base  
                • Weak plants that easily fall over  
                • Poor grain development due to nutrient blockage""",
             """• Avoid excessive soil moisture  
                • Treat seeds with fungicides before planting  
                • Implement deep plowing to bury infected residues""",
             """• Caused by *Fusarium spp.* and *Bipolaris spp.*  
                • Survives in soil and infected plant debris  
                • Develops under high humidity and poor drainage"""),

            ("Fall Armyworm (Insect)", [os.path.join("img", "fall-armyworm-wheat-1.jpg")],
             """• Leaves have irregular holes due to larval feeding  
                • Infestation spreads rapidly across fields  
                • Severe damage can destroy entire plants""",
             """• Use pheromone traps to monitor and reduce populations  
                • Apply biological controls like *Bacillus thuringiensis*  
                • Spray insecticides in early infestation stages""",
             """• Caused by *Spodoptera frugiperda* larvae  
                • Moths lay eggs on wheat leaves  
                • Thrives in warm, dry conditions"""),

            ("Cucumber Beetle (Insect)",[os.path.join("img", "Cucumber-Beetle-1.jpg"), os.path.join("img", "Cucumber-Beetle-2.jpg")],
             """• Yellow and black striped beetles feeding on leaves  
                • Stunted growth and reduced photosynthesis  
                • Larvae damage roots, affecting water uptake""",
             """• Use row covers to prevent beetle access  
                • Apply neem-based insecticides  
                • Introduce natural predators like ladybugs""",
             """• Caused by *Diabrotica spp.* beetles  
                • Beetles emerge from soil in spring  
                • Spreads through infested crop debris""")
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
        
render_wheat_fruiting_diseases()
        
