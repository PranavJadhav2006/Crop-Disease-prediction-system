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
    # Add prefix for rice flowering stage
    prefix = "fsr"  # flowering stage rice
    
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

def render_rice_flowering_diseases():
    IMAGE_FOLDER = "img1/"

      # Flowering Stage Diseases (Rice)
    st.markdown("## 🌾 Flowering Stage (Rice)")

    disease_data = [
         ("Rice Sheath Blight (Fungus)", [os.path.join("img1", "rice-sheath-blight-rice-1.jpg"),os.path.join("img1", "rice-sheath-blight-rice-2.jpg"),os.path.join("img1", "rice-sheath-blight-rice-3.jpg"),os.path.join("img1", "rice-sheath-blight-rice-4.jpg")],
         """• Oval or irregular water-soaked lesions on leaf sheaths  
            • White fungal mycelia spread across affected areas  
            • Severe infection leads to lodging and poor grain filling""",
         """• Use resistant rice varieties  
            • Improve air circulation by spacing plants properly  
            • Apply fungicides like propiconazole at early infection stages""",
         """• Caused by *Rhizoctonia solani*, a soil-borne fungus  
            • Favors high humidity and wet conditions  
            • Spreads through infected plant debris and irrigation water"""),

         ("Sheath Rot of Rice (Fungus)", [os.path.join("img1", "sheath-rot-of-rice-rice-1.jpg"),os.path.join("img1", "sheath-rot-of-rice-rice-2.jpg"),os.path.join("img1", "sheath-rot-of-rice-rice-3.jpg")],
         """• Brownish or reddish lesions on leaf sheaths  
            • Grain discoloration and poor seed setting  
            • White or pinkish fungal growth on affected tissues""",
         """• Use clean, high-quality seeds  
            • Improve drainage to prevent excessive moisture  
            • Apply fungicides like carbendazim""",
         """• Caused by *Sarocladium oryzae*, a fungal pathogen  
            • Thrives in humid conditions  
            • Spread through infected plant debris and air"""),

         ("Udbatta Disease of Rice (Fungus)", [os.path.join("img1", "udbatta-disease-of-rice-1.jpg"),os.path.join("img1", "udbatta-disease-of-rice-2.jpg")],
         """• Leaves turn pale and roll upward  
            • Panicles remain enclosed within leaf sheaths  
            • White fungal structures visible on infected parts""",
         """• Use disease-free seeds for planting  
            • Burn infected plant residues to stop spread  
            • Apply fungicides like benomyl""",
         """• Caused by *Ephelis oryzae*  
            • Favors moist and humid conditions  
            • Spreads through contaminated seeds"""),

         ("Phoma Sorghina in Rice (Fungus)", [os.path.join("img1", "phoma-sorghina-in-rice-1.jpg")],
         """• Dark brown lesions on leaves and stems  
            • Weak plant structure leading to breakage  
            • Black fungal spots on grains""",
         """• Use seed treatment before planting  
            • Improve field drainage to reduce moisture  
            • Apply fungicides like mancozeb""",
         """• Caused by *Phoma sorghina*, a fungal pathogen  
            • Spread through infected seeds and plant residues  
            • Thrives in warm, wet conditions"""),

         ("Stackburn of Rice (Fungus)", [os.path.join("img1", "stackburn-of-rice-rice-.jpg"),os.path.join("img1", "stackburn-of-rice-rice-1.jpg"),os.path.join("img1", "stackburn-of-rice-rice-2.jpg"),os.path.join("img1", "stackburn-of-rice-rice-3.jpg")],
         """• Brown spots with concentric rings on leaves  
            • Affects panicles, leading to unfilled grains  
            • Leaves dry out and fall off prematurely""",
         """• Apply potassium and phosphorus fertilizers  
            • Use disease-resistant rice varieties  
            • Apply fungicides like tricyclazole""",
         """• Caused by *Alternaria padwickii*  
            • Favors warm and humid environments  
            • Spread through infected seeds and air"""),

         ("Fall Armyworm (Insect)", [os.path.join("img1", "fall-armyworm-rice-1.jpg"),os.path.join("img1", "fall-armyworm-rice-2.jpg")],
         """• Irregular holes in leaves and panicles  
            • Larvae feed on young grains  
            • Heavy infestations lead to significant yield loss""",
         """• Use biological control methods like Trichogramma wasps  
            • Apply neem-based insecticides  
            • Use pheromone traps to monitor population""",
         """• Caused by *Spodoptera frugiperda*  
            • Spread through adult moths laying eggs on plants  
            • Favors warm, dry conditions"""),

         ("Rice Bug (Insect)", [os.path.join("img1", "rice-bug-rice-1.jpg"),os.path.join("img1", "rice-bug-rice-2.jpg"),os.path.join("img1", "rice-bug-rice-3.jpg")],
         """• Grains turn black and shriveled  
            • Feeding scars on grains reduce quality  
            • Foul odor in heavily infested fields""",
         """• Encourage natural predators like birds and spiders  
            • Use light traps to capture adult bugs  
            • Spray insecticides during early infestation""",
         """• Caused by *Leptocorisa oratorius*  
            • Adult bugs feed on developing grains  
            • Favors warm and humid conditions"""),

         ("Rice Hispa (Insect)", [os.path.join("img1", "rice-hispa-rice-1.jpg"),os.path.join("img1", "rice-hispa-rice-2.jpg"),os.path.join("img1", "rice-hispa-rice-3.jpg")],
         """• Parallel white streaks on leaves  
            • Leaves become ragged and dry  
            • Heavy infestations cause defoliation""",
         """• Introduce natural predators like ladybugs  
            • Remove affected leaves early  
            • Apply botanical insecticides""",
         """• Caused by *Dicladispa armigera*  
            • Spread through adult beetles laying eggs on leaves  
            • Favors dense crop growth"""),

         ("Rice Leafroller (Insect)", [os.path.join("img1", "rice-leafroller-1.jpg"),os.path.join("img1", "rice-leafroller-2.jpg"),os.path.join("img1", "rice-leafroller-3.jpg"),os.path.join("img1", "rice-leafroller-4.jpg"),os.path.join("img1", "rice-leafroller-5.jpg")],
         """• Leaves roll up and appear dry  
            • Caterpillars feed on leaf tissue  
            • Reduced photosynthesis and plant growth""",
         """• Use neem oil or Bacillus thuringiensis sprays  
            • Introduce biological control agents  
            • Avoid excessive nitrogen fertilizers""",
         """• Caused by *Cnaphalocrocis medinalis*  
            • Spreads through adult moths laying eggs on leaves  
            • Favors humid conditions"""),

         ("Asian Rice Gall (Insect)", [os.path.join("img1", "asian-rice-gall-midge-1.jpg"),os.path.join("img1", "asian-rice-gall-midge-2.jpg")],
         """• Small, swollen galls on stems and leaves  
            • Weak plants with poor tillering  
            • Reduced grain development""",
         """• Remove infested plants to prevent spread  
            • Encourage natural enemies like parasitic wasps  
            • Use insecticides if infestation is severe""",
         """• Caused by *Orseolia oryzae*  
            • Spread through infected plants and insect movement  
            • Favors warm, wet climates"""),
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
        
render_rice_flowering_diseases()