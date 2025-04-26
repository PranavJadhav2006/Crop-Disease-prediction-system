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
                st.image(current_image,width=600, caption=disease_name)
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

def render_corn_fruiting_diseases():
    IMAGE_FOLDER = "img2"
   
      # Fruiting Stage Diseases (Corn)
    st.markdown("## 🌽 Fruiting Stage (Corn)")

    disease_data = [

         ("Maize Smut (Fungus)", [os.path.join("img2", "maize-smut-maize-1.jpg"),os.path.join("img2", "maize-smut-maize-2.jpg"),os.path.join("img2", "maize-smut-maize-3.jpg"),os.path.join("img2", "maize-smut-maize-4.jpg")],
         """• Large, grayish-white galls on kernels and tassels  
            • Kernels swell and burst, releasing black spores  
            • Reduced grain yield""",
         """• Plant smut-resistant maize varieties  
            • Remove infected plants to prevent spore spread  
            • Rotate crops to break the disease cycle""",
         """• Caused by *Ustilago maydis*  
            • Spreads through wind-borne spores  
            • Favored by warm, humid conditions"""),

         ("Head Smut (Fungus)", [os.path.join("img2", "head-smut-maize-1.jpg"),os.path.join("img2", "head-smut-maize-2.jpg"),os.path.join("img2", "head-smut-maize-3.jpg"),os.path.join("img2", "head-smut-maize-4.jpg")],
         """• White fungal masses replace maize tassels  
            • Affected ears are malformed and sterile  
            • Black powdery spores develop later""",
         """• Use smut-resistant maize hybrids  
            • Apply fungicide-treated seeds  
            • Destroy infected plants to limit spore spread""",
         """• Caused by *Sporisorium reilianum*  
            • Soil-borne fungus, infects young plants  
            • Survives in soil for multiple seasons"""),

         ("Penicillium Ear Rot (Fungus)", [os.path.join("img2", "penicillium-ear-rot-1.jpg")],
         """• Green or blue-green mold on maize ears  
            • Soft, discolored kernels  
            • Reduces grain quality and can produce mycotoxins""",
         """• Harvest maize at correct moisture levels  
            • Store grain in dry, cool conditions  
            • Avoid mechanical damage to ears""",
         """• Caused by *Penicillium* species  
            • Fungal spores spread via wind and insects  
            • More common in damp storage conditions"""),

         ("False Smut (Fungus)", [os.path.join("img2", "False-Smut.1.jpg"),os.path.join("img2", "False-Smut.2.jpg"),os.path.join("img2", "False-Smut.3.jpg")],
         """• Small, bright orange or yellow spore balls on kernels  
            • Affected kernels shrink and harden  
            • Lowers grain quality and market value""",
         """• Use resistant maize varieties  
            • Apply foliar fungicides at flowering stage  
            • Maintain good field hygiene""",
         """• Caused by *Ustilaginoidea virens*  
            • Spreads through wind and water splashes  
            • Thrives in high humidity conditions"""),

         ("Fall Armyworm (Insect)", [os.path.join("img2", "fall-armyworm-maize-1.jpg"),os.path.join("img2", "fall-armyworm-maize-2.jpg"),os.path.join("img2", "fall-armyworm-maize-3.jpg")],
         """• Holes in maize leaves, resembling a 'shotgun' pattern  
            • Caterpillars burrow into maize cobs  
            • Can destroy entire maize fields if uncontrolled""",
         """• Apply biological insecticides like *Bacillus thuringiensis*  
            • Introduce natural enemies like parasitoid wasps  
            • Use pheromone traps for monitoring""",
         """• Caused by *Spodoptera frugiperda* larvae  
            • Highly migratory pest, spreads rapidly  
            • Prefers warm tropical climates"""),

         ("Stink Bugs on Maize, Millet, and Sorghum (Insect)", [os.path.join("img2", "stink-bugs-on-maize.1.jpg"),os.path.join("img2", "stink-bugs-on-maize.2.jpg"),os.path.join("img2", "stink-bugs-on-maize.3.jpg")],
         """• Sunken, dark spots on maize kernels  
            • Deformed ears with shriveled grains  
            • Stink bugs release foul odor when disturbed""",
         """• Use neem-based sprays or insecticides  
            • Encourage natural predators like assassin bugs  
            • Remove weeds that harbor stink bugs""",
         """• Various species, including *Nezara viridula*  
            • Suck sap from maize kernels, causing damage  
            • More active in warm, dry conditions"""),

         ("European Maize Borer (Insect)", [os.path.join("img2", "european-maize-borer-maize-1.jpg"),os.path.join("img2", "european-maize-borer-maize-2.jpg"),os.path.join("img2", "european-maize-borer-maize-3.jpg")],
         """• Small holes in maize stalks and ears  
            • Tunneling inside stems weakens plants  
            • Reduces maize ear size and grain quality""",
         """• Apply insecticides at early larval stages  
            • Introduce parasitoid wasps for biological control  
            • Rotate crops to reduce overwintering larvae""",
         """• Caused by *Ostrinia nubilalis* larvae  
            • Overwinters in maize stalk residues  
            • More common in temperate maize-growing regions"""),

         ("Helicoverpa Caterpillar (Insect)", [os.path.join("img2", "helicoverpa-caterpillar-maize-1.jpg"),os.path.join("img2", "helicoverpa-caterpillar-maize-2.jpg"),os.path.join("img2", "helicoverpa-caterpillar-maize-3.jpg")],
         """• Larvae feed on maize ears, damaging kernels  
            • Leaves silken webbing and frass inside ears  
            • Leads to secondary fungal infections""",
         """• Use genetically modified Bt maize  
            • Apply insecticides during early infestations  
            • Encourage natural predators like ladybugs""",
         """• Caused by *Helicoverpa armigera*  
            • Nocturnal moth lays eggs on maize silks  
            • Spreads rapidly in warm regions"""),
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
        
render_corn_fruiting_diseases()