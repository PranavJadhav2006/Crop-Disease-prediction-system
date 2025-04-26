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
    # Add prefix for rice fruiting stage
    prefix = "frsr"  # fruiting stage rice
    
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

def render_rice_fruiting_diseases():
    IMAGE_FOLDER = "img1/"

      # Fruiting Stage Diseases (Rice)
    st.markdown("## 🌾 Fruiting Stage (Rice)")

    disease_data = [
         ("False Smut (Fungus)", [os.path.join("img1", "false-smut-rice-1.jpg"),os.path.join("img1", "false-smut-rice-2.jpg"),os.path.join("img1", "false-smut-rice-3.jpg"),os.path.join("img1", "false-smut-rice-4.jpg")],
         """• Yellowish or greenish spore masses on grains  
            • Grains become covered with fungal balls  
            • Reduces seed quality and yield""",
         """• Use disease-resistant rice varieties  
            • Avoid excess nitrogen fertilization  
            • Apply fungicides like propiconazole""",
         """• Caused by *Ustilaginoidea virens*  
            • Thrives in humid conditions  
            • Spread through infected seeds and air"""),

         ("Kernel Smut of Rice (Fungus)", [os.path.join("img1", "kernel-smut-of-rice-rice-1.jpg"),os.path.join("img1", "kernel-smut-of-rice-rice-2.jpg")],
         """• Black powdery spores inside rice kernels  
            • Affected grains break easily during processing  
            • No visible symptoms on leaves""",
         """• Use certified disease-free seeds  
            • Maintain proper field sanitation  
            • Apply fungicides like azoxystrobin""",
         """• Caused by *Tilletia barclayana*  
            • Spread through wind-borne spores  
            • Favors warm and humid conditions"""),

         ("Spiny Bollworm (Insect)", [os.path.join("img1", "spiny-bollworm-cotton-1.jpg"),os.path.join("img1", "spiny-bollworm-cotton-2.jpg")],
         """• Caterpillars bore into developing grains  
            • Holes in rice panicles  
            • Grains become shriveled and lightweight""",
         """• Use pheromone traps to monitor infestation  
            • Apply neem-based insecticides  
            • Introduce natural predators like wasps""",
         """• Caused by *Earias vittella*  
            • Larvae feed inside grains and panicles  
            • Favors warm, dry conditions"""),

         ("Pod Bug (Insect)", [os.path.join("img1", "pod-bug-rice-1.jpg"),os.path.join("img1", "pod-bug-rice-2.jpg")],
         """• Discolored grains with feeding scars  
            • Grains develop an off-flavor  
            • Adults and nymphs suck plant sap""",
         """• Use light traps to reduce population  
            • Encourage natural predators like spiders  
            • Spray botanical insecticides if needed""",
         """• Caused by *Clavigralla gibbosa*  
            • Spread through infested plant debris  
            • Prefers warm and humid climates"""),

         ("Tussock Moths (Insect)", [os.path.join("img1", "tussock-moths-rice-1.jpg"),os.path.join("img1", "tussock-moths-rice-2.jpg")],
         """• Caterpillars feed on rice leaves  
            • Leaves appear skeletonized with missing tissue  
            • Heavy infestations lead to defoliation""",
         """• Remove affected leaves to prevent spread  
            • Introduce biological control agents  
            • Apply neem oil sprays""",
         """• Caused by *Orgyia spp.*  
            • Caterpillars hatch from eggs on rice plants  
            • Favors dense crop growth"""),

         ("Slender Rice Bug (Insect)",  [os.path.join("img1", "slender-rice-bug-rice-1.jpg"),os.path.join("img1", "slender-rice-bug-rice-2.jpg"),os.path.join("img1", "slender-rice-bug-rice-3.jpg")],
         """• Feeds on developing grains  
            • Grains become empty and discolored  
            • Reduced yield and poor grain quality""",
         """• Apply insecticides during early infestation  
            • Use biological controls like spiders  
            • Remove weeds that host bugs""",
         """• Caused by *Leptocorisa acuta*  
            • Adults and nymphs suck sap from grains  
            • Favors warm, wet conditions"""),
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
        
render_rice_fruiting_diseases()