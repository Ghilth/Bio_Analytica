import gradio as gr
import numpy as np
from PIL import Image, ImageOps
from skimage.transform import resize
import tensorflow as tf

# Fonction de segmentation améliorée (exemple, modèle réel pourrait être intégré)
def segmenter_image(image):
    image_gray = ImageOps.grayscale(image)
    return image_gray

# Fonction fictive pour détecter la maladie (à remplacer par un modèle réel)
def detecter_maladie(image):
    # Ici, nous simulons une détection de maladie
    return "Maladie détectée : Oïdium (champignon) - Un revêtement poudreux blanc sur les feuilles."

# Fonction pour générer des recommandations
def recommandations(image):
    return "Recommandations : Traitez avec un fongicide adapté et augmentez l’aération autour de la plante."

# Fonction principale de l'application : segmentation, détection de maladie et recommandations
def bio_analytica(image):
    image_segmentee = segmenter_image(image)
    maladie_detectee = detecter_maladie(image)
    reco_text = recommandations(image)
    
    return image_segmentee, maladie_detectee, reco_text


    

# Personnalisation de l'interface avec un design plus soigné
interface = gr.Interface(
    fn=bio_analytica,  # Fonction principale
    inputs=gr.Image(type="pil"),  # Entrée : Image de la plante
    outputs=[gr.Image(type="pil"), "text", "text"],  # Sorties : Image segmentée, maladie, recommandations
    title="🌿 Bio Analytica - Analyse Avancée des Plantes",
    description="""
    <div style="text-align: center;">
        <h2 style="color: #2E8B57;">Téléchargez une image de votre plante malade 🌱</h2>
        <p style="font-size: 16px; color: #555;">
            Nous allons analyser l'image pour détecter la maladie présente et vous fournir des recommandations adaptées.<br>
            Obtenez une segmentation précise de la plante 🌿 et découvrez comment soigner vos végétaux.
        </p>
    </div>""",
    examples=[["exemple_image_plante1.jpg"], ["exemple_image_plante2.jpg"]],  # Exemples pour tester
    css="""
    body { background-color: #f0f8ff; }  /* Couleur de fond douce */
    .output_image { border-radius: 10px; border: 2px solid #2E8B57; } /* Bordure stylisée pour les images segmentées */
    h2 { font-family: 'Arial', sans-serif; color: #2E8B57; } /* Couleur principale pour les titres */
    p { font-family: 'Verdana', sans-serif; color: #4F4F4F; } /* Polices élégantes pour les descriptions */
    button { background-color: #2E8B57; color: white; border-radius: 5px; } /* Style pour les boutons */
    .gradio-container { font-family: 'Arial', sans-serif; } /* Application de police générale */
    """,
    layout="vertical",  # Organisation verticale avec image en haut, puis texte
    theme="default",  # Utiliser un thème par défaut amélioré
    allow_flagging="never"
)

# Lancement de l'application
interface.launch()
