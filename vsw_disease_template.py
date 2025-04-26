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
    # Add prefix for wheat vegetation stage
    prefix = "vsw"  # vegetation stage wheat
    
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

def render_wheat_vegetation_diseases():
    IMAGE_FOLDER = "img/"

    disease_data = [
         ("Leaf Rust (Fungus)",[os.path.join("img", "wheat-leaf-rust-wheat-1.jpg"), os.path.join("img", "wheat-leaf-rust-wheat-2.jpg"),os.path.join("img", "wheat-leaf-rust-wheat-3.jpg")], 
         """• Orange-red pustules on the leaves  
            • Yellowing and premature leaf drop  
            • Reduced photosynthesis leading to poor growth""",
         """• Grow resistant wheat varieties  
            • Apply fungicides at early infection stages  
            • Remove infected plant residues to reduce spread""",
         """• Caused by *Puccinia triticina* fungus  
            • Spreads through windborne spores  
            • Thrives in humid and warm conditions"""),

         ("Stem Rust (Fungus)",[os.path.join("img", "wheat-stem-rust-wheat-1.jpg"), os.path.join("img", "wheat-stem-rust-wheat-2.jpg"),os.path.join("img", "wheat-stem-rust-wheat-3.jpg")], 
         """• Brick-red pustules on stems and leaves  
            • Weakening of stems causing lodging  
            • Grain shriveling leading to yield loss""",
         """• Use rust-resistant wheat varieties  
            • Destroy alternate hosts like barberry  
            • Apply fungicides during early rust stages""",
         """• Caused by *Puccinia graminis* fungus  
            • Spreads through air and survives on infected residues  
            • Prefers warm, moist conditions"""),

         ("Septoria Leaf Blotch (Fungus)", [os.path.join("img", "septoria-leaf-spot-tomato-2.jpg"), os.path.join("img", "septoria-leaf-spot-1.jpg")], 
         """• Irregular brown spots with yellow halos on leaves  
            • Dark fruiting bodies visible in lesions  
            • Premature leaf drop affecting yield""",
         """• Avoid excessive nitrogen fertilizers  
            • Ensure proper air circulation between plants  
            • Apply fungicides to control spread""",
         """• Caused by *Zymoseptoria tritici*  
            • Spreads via rain splash and wind  
            • Can survive on infected plant debris"""),

         ("Wheat Streak Mosaic Virus (Virus)",[os.path.join("img", "wheat-leaf-streak-virus-maize-1.jpg"), os.path.join("img", "wheat-leaf-streak-virus-maize-2.jpg")], 
         """• Yellow streaks and mosaic patterns on leaves  
            • Stunted plant growth and reduced tillering  
            • Thin and poorly developed grain heads""",
         """• Use virus-resistant wheat varieties  
            • Control wheat curl mite population  
            • Avoid planting wheat near infected fields""",
         """• Transmitted by *wheat curl mite*  
            • Overwinters in volunteer wheat plants  
            • Spreads rapidly under warm conditions"""),

         ("Fusarium Head Blight (Fungus)", [os.path.join("img", "fusarium-head-blight-1.jpg"), os.path.join("img", "fusarium-head-blight-wheat-2.jpg"),os.path.join("img", "fusarium-head-blight-wheat-3.jpg")], 
         """• Bleached spikelets with pink mold growth  
            • Shrivelled, light-weight grains  
            • Production of harmful mycotoxins""",
         """• Rotate crops to reduce fungal survival  
            • Avoid excessive nitrogen application  
            • Use fungicides at wheat flowering stage""",
         """• Caused by *Fusarium graminearum*  
            • Thrives in warm, wet conditions  
            • Spreads through rain splash and wind"""),

         ("Armyworm (Insect)", [os.path.join("img", "fall-armyworm-wheat-1.jpg")], 
         """• Skeletonized leaves with large feeding holes  
            • Visible green or brown caterpillars on leaves  
            • Sudden loss of leaf cover leading to weak plants""",
         """• Introduce natural predators like birds and parasitoids  
            • Use pheromone traps to monitor infestation  
            • Apply biological insecticides such as Bacillus thuringiensis (Bt)""",
         """• Caused by *Mythimna separata* larvae  
            • Migratory insect, active during night  
            • Feeds heavily on wheat leaves"""),

         ("Hessian Fly (Insect)",[os.path.join("img", "shoot-flies-1.jpg")], 
         """• Stunted plant growth and weak stems  
            • Darkened leaf bases due to maggot feeding  
            • Lodging of wheat plants before maturity""",
         """• Delay planting to avoid peak fly emergence  
            • Use resistant wheat cultivars  
            • Plow fields after harvest to destroy overwintering larvae""",
         """• Caused by *Mayetiola destructor* fly larvae  
            • Overwinters in wheat stubble  
            • Spreads rapidly in warm, moist conditions"""),

         ("Russian Wheat Aphid (Insect)", [os.path.join("img", "Russian_Wheat_Aphid-1.jpg"), os.path.join("img", "Russian_Wheat_Aphid-2.jpg")], 
         """• Curled and rolled leaves with yellow streaks  
            • Stunted growth and reduced yield  
            • Presence of tiny green aphids under leaves""",
         """• Introduce natural predators like ladybugs  
            • Apply neem-based insecticides  
            • Avoid excessive nitrogen application""",
         """• Caused by *Diuraphis noxia* aphids  
            • Sucks plant sap leading to weak plants  
            • Spreads plant viruses affecting growth"""),

         ("Barley Yellow Dwarf Virus (Virus)", [os.path.join("img", "wheat-dwarf-virus-wheat-1.jpg"), os.path.join("img", "wheat-dwarf-virus-wheat-2.jpg"),os.path.join("img", "wheat-dwarf-virus-wheat-3.jpg")], 
         """• Yellowing and reddening of leaf tips  
            • Stunted plant growth with thin stems  
            • Poor grain filling leading to reduced yield""",
         """• Plant early to escape aphid transmission  
            • Use resistant wheat varieties  
            • Control aphid populations with insecticides""",
         """• Transmitted by *aphids* feeding on wheat  
            • Overwinters in grass hosts  
            • Spreads rapidly in warm, dry conditions""")
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
        
render_wheat_vegetation_diseases()
