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
    # Add prefix for wheat seedling stage
    prefix = "ssw"  # seedling stage wheat
    
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

def render_wheat_seedling_diseases():
    IMAGE_FOLDER = "img/"

    disease_data = [
        ("Bottom Rot (Fungus)", [os.path.join("img", "bottom-rot-lettuce-1.jpg"), os.path.join("img", "bottom-rot-lettuce-2.jpg")], 
   """• Yellowing and wilting of lower leaves  
            • Rotting of the seedling base  
            • Weak root system and plant collapse""",
         """• Use well-drained soil to prevent excessive moisture  
            • Avoid overwatering to reduce fungal growth  
            • Use fungicide-treated seeds to prevent infections""",
         """• Caused by *Rhizoctonia solani*, a soil-borne fungus  
            • Thrives in high moisture and poorly aerated soil  
            • Spreads through infected soil and plant debris"""),
        
        ("Yellow Stripe Rust (Fungus)", [os.path.join("img", "yellow-stripe-rust-wheat-1.jpg"), os.path.join("img", "yellow-stripe-rust-wheat-2.jpg")], 
      """• Long yellow stripes along the leaf veins  
         • Stunted growth, poor tillering, and reduced yield  
         • Leaves dry prematurely and turn brown""",
      """• Plant resistant wheat varieties to reduce susceptibility  
         • Apply fungicides early to prevent the spread  
         • Ensure proper nitrogen fertilization for plant health""",
      """• Caused by *Puccinia striiformis*, a windborne fungus  
         • Spreads rapidly in cool, humid conditions  
         • Overwinters on infected plant residues"""),

      ("Septoria Tritici Blotch (Fungus)", [os.path.join("img", "septoria-tritici-blotch-wheat-1.jpg"), os.path.join("img", "septoria-tritici-blotch-wheat-2.jpg"),  os.path.join("img", "septoria-tritici-blotch-wheat-3.jpg"), os.path.join("img", "septoria-tritici-blotch-wheat-4.jpg")], 
      """• Brown blotches with yellow halos on leaves  
         • Black fruiting bodies form within lesions  
         • Severe infections cause leaves to wither prematurely""",
      """• Rotate crops to break the fungal life cycle  
         • Avoid overhead irrigation to prevent moisture buildup  
         • Apply fungicides at early signs of infection""",
      """• Caused by *Zymoseptoria tritici*, a fungal pathogen  
         • Spreads through rain splash and wind  
         • Can survive on wheat stubble from previous crops"""),

      ("Snow Mold of Cereals (Fungus)", [os.path.join("img", "snow-mold-of-cereals-wheat-1.jpg"), os.path.join("img", "snow-mold-of-cereals-wheat-2.jpg")], 
      """• Pink or gray mold covering seedlings  
         • Weak, yellowed seedlings with poor growth  
         • Stunted root development leading to plant death""",
      """• Avoid planting in poorly drained, compacted soils  
         • Use resistant wheat varieties suited for cold regions  
         • Apply fungicides before snowfall to reduce fungal spread""",
      """• Caused by *Microdochium nivale* and *Typhula spp.*  
         • Develops under prolonged snow cover with excess moisture  
         • Can remain dormant in soil and plant debris"""),

      ("Powdery Mildew of Cereals (Fungus)", [os.path.join("img", "powdery-mildew-of-cereals-wheat-1.jpg"), os.path.join("img", "powdery-mildew-of-cereals-wheat-2.jpg"),os.path.join("img", "powdery-mildew-of-cereals-wheat-3.jpg"), os.path.join("img", "powdery-mildew-of-cereals-wheat-4.jpg")], 
      """• White, powdery fungal patches on leaves and stems  
         • Reduced photosynthesis leading to poor growth  
         • Leaves curl, dry out, and become brittle""",
      """• Grow resistant wheat varieties to minimize risk  
         • Increase air circulation between plants by proper spacing  
         • Apply sulfur-based fungicides to control infection""",
      """• Caused by *Blumeria graminis*, an airborne fungus  
         • Spreads through wind-carried spores  
         • Prefers warm, dry conditions for rapid growth"""),

      ("Aphids (Insect)", [os.path.join("img", "aphids-wheat-1.jpg"), os.path.join("img", "aphids-wheat-2.jpg")], 
      """• Leaves curl and turn yellow due to sap-sucking  
         • Sticky honeydew secretions attract ants  
         • Plants show stunted growth and reduced vigor""",
      """• Introduce natural predators like ladybugs and lacewings  
         • Use neem oil sprays to repel aphids naturally  
         • Apply systemic insecticides in severe infestations""",
      """• Small, soft-bodied insects that suck plant sap  
         • Reproduce rapidly under warm and dry conditions  
         • Can transmit viral diseases to plants"""),

      ("Cereal Leaf Beetle (Insect)", [os.path.join("img", "cereal-leaf-beetle-wheat-1.jpg"), os.path.join("img", "cereal-leaf-beetle-wheat-2.jpg"),os.path.join("img", "cereal-leaf-beetle-wheat-3.jpg")], 
      """• Skeletonized leaves due to larval feeding  
         • Black, sticky excrement left behind by larvae  
         • Weakened plants lead to reduced grain yield""",
      """• Introduce biological control agents (parasitic wasps)  
         • Hand-pick beetles and destroy larvae manually  
         • Apply insecticides during larval feeding stage""",
      """• *Oulema melanopus* beetles lay eggs on leaves  
         • Larvae feed on wheat and other cereals  
         • Populations increase in warm, moist conditions"""),

      ("Wireworms (Insect)", [os.path.join("img", "wireworms-1.jpg")], 
      """• Seedlings fail to emerge or appear wilted  
         • Roots and stems have small boreholes  
         • Plants turn yellow and show slow growth""",
      """• Rotate crops with non-host plants like legumes  
         • Use seed treatments with insecticides for control  
         • Improve soil drainage to reduce infestation""",
      """• Larvae of *Click Beetles* that feed on underground plant parts  
         • Prefer moist, compacted soils for development  
         • Can persist in soil for multiple years"""),

      ("Termites (Insect)", [ os.path.join("img", "termites-1.jpg")], 
      """• Hollowed-out plant stems and weakened roots  
         • Seedlings can be pulled from soil easily  
         • Presence of mud tubes in affected fields""",
      """• Apply termiticides to soil before planting  
         • Use neem cake or organic barriers for protection  
         • Reduce excessive crop residues that attract termites""",
      """• Colonies of termites feed on plant roots and stems  
         • Thrive in dry conditions and organic debris  
         • Cause major losses in poorly managed fields""")
       
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
        
render_wheat_seedling_diseases()
