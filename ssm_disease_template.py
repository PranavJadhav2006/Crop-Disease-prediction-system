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

def render_corn_seedling_diseases():
    IMAGE_FOLDER = "img2"
   
      # Seedling Stage Diseases (Corn)
    st.markdown("## 🌽 Seedling Stage (Corn)")

    disease_data = [
         ("Bottom Rot (Fungus)", [os.path.join("img2", "bottom-rot-lettuce-1.jpg"),os.path.join("img2", "bottom-rot-lettuce-2.jpg")],
         """• Causes seedling collapse at soil level  
            • Affected roots turn brown and decay  
            • Stunted growth and wilting of young plants""",
         """• Ensure proper field drainage  
            • Avoid excessive irrigation  
            • Use resistant seed varieties""",
         """• Caused by *Rhizoctonia solani*  
            • Thrives in warm and wet soil  
            • Spreads through infected plant debris"""),

         ("Root and Foot Rot (Fungus)",[os.path.join("img2", "root-and-foot-rot-1.jpg"),os.path.join("img2", "root-and-foot-rot-2.jpg"),os.path.join("img2", "root-and-foot-rot-3.jpg")],
         """• Yellowing and wilting of leaves  
            • Rotted roots with dark brown lesions  
            • Poor nutrient and water uptake""",
         """• Rotate crops regularly  
            • Use fungicide-treated seeds  
            • Avoid overwatering and compacted soil""",
         """• Caused by *Fusarium spp.* and *Pythium spp.*  
            • Spread through contaminated soil and water  
            • Thrives in poorly drained soils"""),

         ("Damping-off of Seedlings (Fungus)",[os.path.join("img2", "Damping-off-of-Seedlings.1.jpg"),os.path.join("img2", "Damping-off-of-Seedlings.2.jpg")],
         """• Seedlings fail to emerge or collapse after sprouting  
            • Soft, water-soaked lesions near the base of the stem  
            • Rapid decay of young plants""",
         """• Use well-drained soil with good aeration  
            • Apply fungicides to seeds before planting  
            • Avoid excessive moisture in seedbeds""",
         """• Caused by *Pythium*, *Rhizoctonia*, and *Phytophthora spp.*  
            • Favors damp, cool conditions  
            • Spreads through soil and infected seeds"""),

         ("Wireworms (Insect)",[os.path.join("img2", "wireworms-1.jpg")],
         """• Holes in emerging seedlings  
            • Wilting and poor seedling development  
            • Roots chewed off at the base""",
         """• Use insecticide-treated seeds  
            • Rotate crops with non-host plants  
            • Encourage natural predators like birds and ground beetles""",
         """• Larvae of click beetles (*Elateridae family*)  
            • Live in soil and attack roots  
            • More common in poorly tilled fields"""),

         ("Termites (Insect)",[os.path.join("img2", "termites-1.jpg")],
         """• Hollowed-out stems and roots  
            • Wilting and death of seedlings  
            • Soil mounds near plant bases""",
         """• Apply termiticides in soil  
            • Destroy old plant debris and stumps  
            • Improve soil drainage""",
         """• Caused by *Odontotermes* and *Microtermes* spp.  
            • Thrive in warm, dry soil  
            • Spread through underground tunnels"""),
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

render_corn_seedling_diseases()
