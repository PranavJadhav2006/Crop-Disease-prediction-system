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
    # Add prefix for rice vegetation stage
    prefix = "vsr"  # vegetation stage rice
    
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

def render_rice_vegetation_diseases():
    IMAGE_FOLDER = "img1/"

# Vegetative Stage Diseases (Rice)
    st.markdown("## 🌾 Vegetative Stage (Rice)")

    disease_data = [
         ("Blast of Rice (Fungus)", [os.path.join("img1","blast-of-rice-rice-1.jpg"),os.path.join("img1","blast-of-rice-rice-2.jpg"),os.path.join("img1","blast-of-rice-rice-3.jpg")],
         """• Spindle-shaped lesions with gray centers  
            • Severe cases lead to broken or dead leaf tips  
            • Affects stems and panicles, causing yield loss""",
         """• Use resistant rice varieties  
            • Apply balanced fertilizers to improve plant strength  
            • Use fungicides like tricyclazole during early symptoms""",
         """• Caused by *Magnaporthe oryzae*, a fungal pathogen  
            • Favors humid, rainy, and cool conditions  
            • Spread through wind, infected seeds, and plant debris"""),

         ("Brown Spot of Rice (Fungus)", [os.path.join("img1","brown-spot-of-rice-rice-1.jpg"),os.path.join("img1","brown-spot-of-rice-rice-2.jpg"),os.path.join("img1","brown-spot-of-rice-rice-3.jpg")],
         """• Brown oval spots on leaves with yellow halos  
            • Infected plants show poor growth and leaf drying  
            • Severe cases lead to unfilled grains""",
         """• Apply potassium and phosphorus fertilizers  
            • Use clean, high-quality seeds  
            • Improve drainage and avoid excessive moisture""",
         """• Caused by *Bipolaris oryzae*, a fungal disease  
            • Spread through infected seeds and soil  
            • Thrives in poorly nourished crops"""),

         ("Foot and Collar Rot (Fungus)", [os.path.join("img1","foot-and-collar-rot-1.jpg"),os.path.join("img1","foot-and-collar-rot-chickpea-1.jpg")],
         """• Dark, water-soaked lesions at the base of seedlings  
            • Leaves turn yellow and wilt  
            • Weak stem base leads to lodging""",
         """• Use seed treatment with fungicides before planting  
            • Improve field drainage to reduce standing water  
            • Avoid excessive nitrogen fertilizers""",
         """• Caused by *Fusarium spp.* and *Rhizoctonia solani*  
            • Spreads through infected soil and plant debris  
            • Favored by high humidity and poor aeration"""),

         ("Stem Rot of Rice (Fungus)", [os.path.join("img1","stem-rot-of-rice-rice-1.jpg"),os.path.join("img1","stem-rot-of-rice-rice-2.jpg"),os.path.join("img1","stem-rot-of-rice-rice-3.jpg"),os.path.join("img1","stem-rot-of-rice-rice-4.jpg")],
         """• Black fungal growth inside lower stems  
            • Weakening of plants leads to lodging  
            • White fungal masses may appear on dead tissues""",
         """• Remove infected plant debris from fields  
            • Apply potassium fertilizers to strengthen plants  
            • Use fungicides during early infection""",
         """• Caused by *Sclerotium oryzae*, a soil-borne fungus  
            • Survives in plant debris and moist soil  
            • Spread through water and infected residues"""),

         ("Leaf Scald of Rice (Fungus)", [os.path.join("img1","leaf-scald-of-rice-1.jpg"),os.path.join("img1","leaf-scald-of-rice-2.jpg"),os.path.join("img1","leaf-scald-of-rice-3.jpg")],
         """• Long reddish-brown streaks on leaf tips  
            • Affected leaves dry out and die  
            • Reduced photosynthesis and plant growth""",
         """• Plant resistant rice varieties  
            • Maintain balanced nitrogen levels in soil  
            • Improve air circulation in dense fields""",
         """• Caused by *Microdochium oryzae*, a fungal pathogen  
            • Favors wet, warm climates  
            • Spreads through infected plant debris and water droplets"""),

         ("Rice Grassy Stunt Virus (Virus)", [os.path.join("img1","rice-grassy-stunt-virus-rice-1.jpg"),os.path.join("img1","rice-grassy-stunt-virus-rice-2.jpg")],
         """• Plants grow excessively tall with narrow leaves  
            • Reduced tillering and poor grain formation  
            • Leaves remain green but plants are weak""",
         """• Use insect-resistant varieties to reduce virus transmission  
            • Control planthopper populations with biological methods  
            • Remove infected plants from the field""",
         """• Caused by *Rice Grassy Stunt Virus* (RGSV)  
            • Transmitted by brown planthoppers  
            • Spread occurs when infected insects feed on healthy plants"""),

         ("Tungro (Virus)", [os.path.join("img1","tungro-rice-1.jpg"),os.path.join("img1","tungro-rice-2.jpg"),os.path.join("img1","tungro-rice-3.jpg")],
         """• Yellow-orange discoloration of leaves  
            • Stunted plant growth with reduced tillers  
            • Poor grain filling and reduced yield""",
         """• Use virus-resistant rice varieties  
            • Control leafhoppers that spread the virus  
            • Remove infected plants early to prevent further spread""",
         """• Caused by *Rice Tungro Bacilliform Virus*  
            • Spread by green leafhoppers  
            • Infection occurs through insect feeding"""),

         ("Bacterial Blight of Rice (Bacteria)", [os.path.join("img1","bacterial-blight-of-rice-rice-1.jpg"),os.path.join("img1","bacterial-blight-of-rice-rice-2.jpg"),os.path.join("img1","bacterial-blight-of-rice-rice-3.jpg"),os.path.join("img1","bacterial-blight-of-rice-rice-4.jpg")],
         """• Water-soaked streaks on leaves turning yellow-brown  
            • Leaves dry out and roll up  
            • Poor panicle development""",
         """• Use resistant rice varieties  
            • Apply copper-based bactericides  
            • Avoid overhead irrigation to reduce bacterial spread""",
         """• Caused by *Xanthomonas oryzae pv. oryzae*  
            • Spread through infected plant debris and rain splash  
            • Enters through leaf wounds and stomata"""),

         ("Bacterial Leaf Streak (Bacteria)", [os.path.join("img1","bacterial-leaf-streak-rice-1.jpg"), os.path.join("img1","bacterial-leaf-streak-rice-2.jpg"),os.path.join("img1","bacterial-leaf-streak-rice-3.jpg")],
         """• Narrow brown streaks along leaf veins  
            • Leaves become brittle and break easily  
            • Yield loss due to reduced photosynthesis""",
         """• Use clean seeds and remove infected plants  
            • Avoid excessive nitrogen fertilizers  
            • Apply copper-based sprays in early infections""",
         """• Caused by *Xanthomonas oryzae pv. oryzicola*  
            • Spread through irrigation water and plant debris  
            • Enters leaves through natural openings"""),

         ("Aphids (Insect)", [os.path.join("img1", "aphids-rice-1.jpg"),os.path.join("img1", "aphids-rice-2.jpg")],
          "Same as Seedling Stage", "Same as Seedling Stage", "Same as Seedling Stage"),
         ("Thrips (Insect)",[os.path.join("img1", "thrips-rice-1.jpg"),os.path.join("img1", "thrips-rice-2.jpg")], "Similar to aphids", "Use neem oil and insecticidal soap", "Spread by wind and infested plants"),
         ("Mealybug (Insect)",[os.path.join("img1", "mealybug-rice-1.jpg"),os.path.join("img1", "mealybug-rice-2.jpg")], "Cottony white pests on stems", "Introduce natural predators", "Spread through infested plants"),

      ]

      # Seedling Stage Diseases (Rice)
    st.markdown("## 🌱 Seedling Stage (Rice)")

    for i, disease in enumerate(disease_data):
       
        disease_template(
            disease_name=disease[0],
            image_paths=disease[1],
            symptoms=disease[2],
            prevention=disease[3],
            causes=disease[4],
            disease_index=i 
           )
        
        
render_rice_vegetation_diseases()
