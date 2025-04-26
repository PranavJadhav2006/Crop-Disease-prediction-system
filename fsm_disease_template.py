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

def render_corn_flowering_diseases():
    IMAGE_FOLDER = "img2"
   
      # Flowering Stage Diseases (Corn)
    st.markdown("## 🌽 Flowering Stage (Corn)")

    disease_data = [
         ("Verticillium Wilt (Fungus)",[os.path.join("img2", "Verticillium-Wilt.1.jpg"),os.path.join("img2", "Verticillium-Wilt.2.jpg")],
         """• Wilting and yellowing of lower leaves  
            • Vascular discoloration in stems  
            • Poor ear development""",
         """• Use resistant maize varieties  
            • Avoid excessive nitrogen fertilizers  
            • Rotate crops with non-host plants""",
         """• Caused by *Verticillium dahliae*  
            • Soil-borne fungus, spreads through infected residues  
            • Prefers cool, moist conditions"""),

         ("Zonate Leaf Spot (Fungus)", [os.path.join("img2", "zonate-leaf-spot-1.jpg"),os.path.join("img2", "zonate-leaf-spot-2.jpg"),os.path.join("img2", "zonate-leaf-spot-3.jpg")],
         """• Circular, tan lesions with zonate rings on leaves  
            • Leaf browning and drying in severe cases  
            • Reduces photosynthesis, leading to lower yield""",
         """• Apply fungicides like mancozeb or chlorothalonil  
            • Remove infected plant debris  
            • Rotate crops to minimize fungal spores""",
         """• Caused by *Gloeocercospora sorghi*  
            • Spreads via wind-borne spores  
            • Favors warm, humid conditions"""),

         ("Southern Rust of Maize (Fungus)",[os.path.join("img2", "southern-rust-of-maize-maize-1.jpg"),os.path.join("img2", "southern-rust-of-maize-maize-2.jpg"),os.path.join("img2", "southern-rust-of-maize-maize-3.jpg")],
         """• Small, orange to reddish-brown pustules on leaves  
            • Pustules mainly on upper leaf surface  
            • Causes premature leaf death and yield loss""",
         """• Grow rust-resistant maize hybrids  
            • Apply fungicides like azoxystrobin or propiconazole  
            • Monitor weather conditions for high humidity""",
         """• Caused by *Puccinia polysora*  
            • Spread through wind-blown spores  
            • Prefers warm, moist environments"""),

         ("Gray Leaf Spot of Maize (Fungus)", [os.path.join("img2", "Gray-Leaf-Spot.1.jpg"),os.path.join("img2", "Gray-Leaf-Spot.2.jpg"),os.path.join("img2", "Gray-Leaf-Spot.3.jpg")],
         """• Long, rectangular gray lesions on leaves  
            • Premature leaf senescence  
            • Reduced grain filling and lower yield""",
         """• Plant resistant maize hybrids  
            • Use crop rotation to break disease cycle  
            • Apply foliar fungicides at early stages""",
         """• Caused by *Cercospora zeae-maydis*  
            • Survives in infected crop residues  
            • Spreads through wind and rain splashes"""),

         ("Flea Beetles (Insect)",[os.path.join("img2", "flea-beetles-maize-1.jpg"),os.path.join("img2", "flea-beetles-maize-2.jpg"),os.path.join("img2", "flea-beetles-maize-3.jpg")],
         """• Tiny, round holes in leaves (shot-hole appearance)  
            • Yellowing and wilting of seedlings  
            • Can transmit bacterial wilt""",
         """• Apply insecticides like pyrethroids  
            • Use row covers to protect young plants  
            • Remove weeds that harbor flea beetles""",
         """• *Chaetocnema pulicaria* species attack maize  
            • Overwinter in plant debris and emerge in spring  
            • Spread bacterial wilt and Stewart’s wilt disease"""),

         ("Spotted Stemborer (Insect)", [os.path.join("img2", "spotted-stemborer-maize-1.jpg"),os.path.join("img2", "spotted-stemborer-maize-2.jpg"),os.path.join("img2", "spotted-stemborer-maize-3.jpg"),os.path.join("img2", "spotted-stemborer-maize-.jpg")],
         """• Small holes in young maize stems  
            • Stunted plant growth  
            • Boring tunnels inside maize stalks""",
         """• Introduce natural predators like parasitoid wasps  
            • Use resistant maize varieties  
            • Apply biological insecticides like *Bacillus thuringiensis*""",
         """• Caused by *Chilo partellus* larvae  
            • Larvae bore into stems, disrupting nutrient flow  
            • More severe in warm tropical regions"""),

         ("Violet Stem Borer (Insect)", [os.path.join("img2", "violet-stem-borer-maize-1.jpg"),os.path.join("img2", "violet-stem-borer-maize-2.jpg"),os.path.join("img2", "violet-stem-borer-maize-3.jpg")],
         """• Stems turn purplish due to larvae feeding inside  
            • Weak stems that break easily  
            • Reduces ear development""",
         """• Apply neem-based insecticides  
            • Use pheromone traps to monitor adult moths  
            • Encourage natural predators like Trichogramma wasps""",
         """• Caused by *Sesamia inferens* larvae  
            • More active in warm and humid conditions  
            • Affects maize, rice, and sugarcane"""),

         ("Cereal Leaf Beetle (Insect)", [os.path.join("img2", "Cereal-Leaf.1.jpg"),os.path.join("img2", "Cereal-Leaf.2.jpg"),os.path.join("img2", "Cereal-Leaf.3.jpg")],
         """• Skeletonized leaves (only veins remain)  
            • Yellowish-brown larvae feeding on leaves  
            • Reduced grain fill due to leaf loss""",
         """• Apply insecticides when larvae appear  
            • Encourage natural predators like ladybugs  
            • Use crop rotation with non-cereal crops""",
         """• Caused by *Oulema melanopus* larvae  
            • Overwinters in soil and emerges in spring  
            • More common in temperate maize-growing regions"""),

         ("Maize Earworm (Insect)",[os.path.join("img2", "maize-earworm-maize-1.jpg")],
         """• Caterpillars feeding on maize ears  
            • Kernels appear damaged with excrement inside ears  
            • Reduces grain quality and yield""",
         """• Use genetically modified Bt maize  
            • Apply insecticides during early infestations  
            • Encourage natural predators like Trichogramma wasps""",
         """• Caused by *Helicoverpa zea* larvae  
            • Eggs laid on silks hatch into feeding larvae  
            • More active in warm summer months"""),
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

render_corn_flowering_diseases()