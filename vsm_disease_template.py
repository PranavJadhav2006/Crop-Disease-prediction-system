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

def render_corn_vegetation_diseases():
    IMAGE_FOLDER = "img2"
   
      # Vegetative Stage Diseases (Corn)
    st.markdown("## 🌽 Vegetative Stage (Corn)")

    disease_data =  [
         ("Powdery Mildew (Fungus)", [os.path.join("img2", "Powdery-Mildew.1.jpg"),os.path.join("img2", "Powdery-Mildew.2.jpg")],
         """• White powdery patches on leaves  
            • Leaf curling and yellowing  
            • Reduced photosynthesis, affecting growth""",
         """• Use resistant maize varieties  
            • Apply fungicides like sulfur or triazoles  
            • Ensure proper spacing to improve air circulation""",
         """• Caused by *Erysiphe spp.*  
            • Thrives in humid and warm conditions  
            • Spread by wind-blown spores"""),

         ("Northern Leaf Blight (Fungus)", [os.path.join("img2", "northern-leaf-blight-of-maize-maize-1.jpg"),os.path.join("img2", "northern-leaf-blight-of-maize-maize-2.jpg"),os.path.join("img2", "northern-leaf-blight-of-maize-maize-3.jpg")],
         """• Large, cigar-shaped gray-green lesions on leaves  
            • Premature leaf death, reducing yield  
            • Fungal spores visible on lesion surfaces""",
         """• Use resistant hybrids  
            • Apply fungicides during early infection  
            • Crop rotation with non-host crops""",
         """• Caused by *Exserohilum turcicum*  
            • Spread through wind and infected plant debris  
            • Favors cool, wet conditions"""),

         ("Common Rust of Maize (Fungus)", [os.path.join("img2", "common-rust-of-maize-maize-1.jpg")],
         """• Small, reddish-brown pustules on leaves  
            • Pustules burst and release powdery spores  
            • Severe infection leads to reduced grain fill""",
         """• Grow rust-resistant maize varieties  
            • Apply fungicides like azoxystrobin  
            • Remove infected plant debris""",
         """• Caused by *Puccinia sorghi*  
            • Spread by wind-blown spores  
            • Favors moderate temperature with high humidity"""),

         ("Tropical Rust (Fungus)",[os.path.join("img2", "tropical-rust-maize-1.jpg")],
         """• Small yellow spots on leaves  
            • Progresses to brown or rust-colored pustules  
            • Causes leaf drying and reduced yield""",
         """• Apply fungicides when early symptoms appear  
            • Plant resistant varieties  
            • Avoid planting maize near infected fields""",
         """• Caused by *Puccinia polysora*  
            • Spreads through wind-borne spores  
            • Thrives in warm, humid environments"""),

         ("Goss Wilt (Bacteria)", [os.path.join("img2", "goss's-wilt--maize-2.jpg"),os.path.join("img2", "goss's-wilt--maize-3.jpg"),os.path.join("img2", "goss's-wilt--maize-5.jpg")],
         """• Water-soaked streaks on leaves  
            • Black freckles within lesions  
            • Wilted and dying plants""",
         """• Plant resistant hybrids  
            • Rotate crops to reduce bacterial buildup  
            • Control insect vectors that spread the bacteria""",
         """• Caused by *Clavibacter michiganensis*  
            • Spread through wounds caused by insects or hail  
            • Survives in plant debris"""),

         ("Holcus Leaf Spot (Bacteria)",[os.path.join("img2", "holcus-leaf-spot-maize-1.jpg"),os.path.join("img2", "holcus-leaf-spot-maize-2.jpg"),os.path.join("img2", "holcus-leaf-spot-maize-3.jpg")],
         """• Round, water-soaked spots on leaves  
            • Spots turn tan with dark brown margins  
            • Severe cases lead to leaf drop""",
         """• Avoid overhead irrigation  
            • Use resistant varieties  
            • Remove infected plant residues""",
         """• Caused by *Pseudomonas syringae*  
            • Spread through rain splashes and contaminated tools  
            • Favors warm and humid conditions"""),

         ("Stunt of Maize (Bacteria)", [os.path.join("img2", "stunt-of-maize-1.jpg"),os.path.join("img2", "stunt-of-maize-2.jpg")],
         """• Stunted plant growth  
            • Shortened internodes and small ears  
            • Yellowing of leaves, especially near the base""",
         """• Control insect vectors like leafhoppers  
            • Plant tolerant hybrids  
            • Apply insecticides to reduce spread""",
         """• Caused by *Spiroplasma kunkelii*  
            • Transmitted by corn leafhoppers  
            • More severe in warm climates"""),

         ("Whiteflies (Insect)", [os.path.join("img2", "Whiteflies.1.jpg"),os.path.join("img2", "Whiteflies.2.jpg"),os.path.join("img2", "Whiteflies.3.jpg")],
         """• Yellowing and curling of leaves  
            • Honeydew secretion leading to sooty mold  
            • Weak plants with poor grain filling""",
         """• Use yellow sticky traps to monitor population  
            • Apply neem oil or insecticides  
            • Encourage natural predators like ladybugs""",
         """• *Bemisia tabaci* species attack maize  
            • Thrive in hot, dry conditions  
            • Spread viral diseases"""),

         ("Aphids (Insect)", [os.path.join("img2", "Aphids.1.jpg"),os.path.join("img2", "Aphids.2.jpg"),os.path.join("img2", "Aphids.3.jpg")],
         """• Sticky honeydew on leaves  
            • Curling and yellowing of leaves  
            • Reduced photosynthesis and plant vigor""",
         """• Spray insecticidal soap or neem oil  
            • Introduce predatory insects like ladybugs  
            • Avoid excessive nitrogen fertilizer""",
         """• Caused by *Rhopalosiphum maidis*  
            • Spread viruses like Maize Dwarf Mosaic Virus  
            • Thrive in warm, dry conditions"""),

         ("Thrips (Insect)", [os.path.join("img2", "Thrips.1.jpg"),os.path.join("img2", "Thrips.2.jpg"),os.path.join("img2", "Thrips.3.jpg")],
         """• Silvery streaks on leaves  
            • Leaf curling and distortion  
            • Poor ear development""",
         """• Spray neem oil or insecticidal soap  
            • Maintain weed-free fields  
            • Use reflective mulch to repel thrips""",
         """• *Frankliniella* species attack maize  
            • Spread maize chlorotic mottle virus  
            • Thrive in dry weather"""),
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
        
render_corn_vegetation_diseases()