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
    # Add prefix for wheat flowering stage
    prefix = "fsw"  # flowering stage wheat
    
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

def render_wheat_flowering_diseases():
    IMAGE_FOLDER = "img/"

    disease_data = [
            ("Net Blotch (Fungus)", [os.path.join("img", "net-blotch-1.jpg"), os.path.join("img", "net-blotch-2.jpg"),os.path.join("img", "net-blotch-3.jpg"),os.path.join("img", "net-blotch-barley-4.jpg")],
             """• Brown or dark net-like lesions on leaves  
                • Reduced photosynthesis leading to poor grain filling  
                • Lower leaves die prematurely""",
             """• Use resistant wheat varieties to minimize infection  
                • Apply fungicides early in the disease cycle  
                • Practice crop rotation to reduce fungal buildup""",
             """• Caused by *Pyrenophora teres*, a fungal pathogen  
                • Thrives in humid and wet conditions  
                • Spreads through infected seeds and crop debris"""),

            ("Eyespot of Cereals (Fungus)", [os.path.join("img","eyespot-of-cereals-1.jpg"), os.path.join("img", "eyespot-of-cereals-3.jpg"),os.path.join("img", "eyespot-of-cereals-4.jpg")],
             """• Oval-shaped brown lesions on lower stem  
                • Weak stems leading to lodging (falling over)  
                • Poor water and nutrient uptake""",
             """• Use fungicide-treated seeds to prevent early infection  
                • Avoid excessive nitrogen application  
                • Rotate crops to break fungal lifecycle""",
             """• Caused by *Tapesia spp.* fungus  
                • Fungal spores survive in soil and plant residues  
                • Moist conditions accelerate the spread"""),

            ("Foot and Collar Rot (Fungus)", [os.path.join("img", "foot-and-collar-rot-1.jpg"), os.path.join("img", "foot-and-collar-rot-chickpea-1.jpg")],
             """• Reddish-brown rot on stem base  
                • Wilting and yellowing of upper leaves  
                • Severe infections lead to plant death""",
             """• Improve soil drainage to prevent waterlogging  
                • Use fungicide applications in early growth stages  
                • Avoid planting in previously infected soil""",
             """• Caused by *Fusarium spp.* and *Rhizoctonia spp.* fungi  
                • Fungi survive in soil and crop residues  
                • Favorable conditions: high moisture and warm temperatures"""),

            ("Snow Mold of Cereal (Fungus)",[os.path.join("img", "snow-mold-of-cereals-wheat-1.jpg"), os.path.join("img", "snow-mold-of-cereals-wheat-2.jpg")],
             """• Grayish-white mold covering wheat plants  
                • Weak, stunted growth after snow melts  
                • Severe infections cause plant death""",
             """• Grow resistant wheat varieties for cold regions  
                • Avoid excessive snow accumulation in fields  
                • Apply protective fungicides before snowfall""",
             """• Caused by *Microdochium nivale* and *Typhula spp.* fungi  
                • Develops under prolonged snow cover  
                • Can survive in plant debris and soil"""),

            ("Rice Leafroller (Insect)", [os.path.join("img", "rice-leafroller-1.jpg"), os.path.join("img", "rice-leafroller-2.jpg"),os.path.join("img", "rice-leafroller-rice-3.jpg")],
             """• Leaves roll up, forming protective tubes for larvae  
                • Feeding damage reduces leaf photosynthesis  
                • Severe infestations lead to poor grain yield""",
             """• Introduce natural enemies like parasitic wasps  
                • Apply neem-based sprays to deter larvae  
                • Use insecticides when infestation is high""",
             """• Caused by *Cnaphalocrocis medinalis* larvae  
                • Larvae feed on leaves and create protective tunnels  
                • Prefers warm and humid conditions"""),

            ("Shoot Flies (Insect)",[os.path.join("img", "shoot-flies-1.jpg")],
             """• Seedlings wilt and die due to larval feeding  
                • Shoots appear cut or tunneled  
                • Reduced tillering and poor yield""",
             """• Use early sowing to escape peak infestation periods  
                • Apply insecticidal seed treatments  
                • Maintain proper field hygiene by removing infested shoots""",
             """• Caused by *Atherigona spp.* larvae  
                • Flies lay eggs near plant stems  
                • Larvae bore into shoots and stunt plant growth""")
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

render_wheat_flowering_diseases()