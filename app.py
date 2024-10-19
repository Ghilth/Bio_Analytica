import gradio as gr
import numpy as np
from PIL import Image, ImageOps
from skimage.transform import resize
import tensorflow as tf


# Fonction de segmentation de la plante (exemple)
def segmenter_image(image):
    # Ici, on peut appliquer un modèle de segmentation réel
    # Pour l'exemple, nous allons simplement convertir l'image en niveaux de gris (mock segmentation)
    image_gray = ImageOps.grayscale(image)
    
    # Simuler une segmentation (ici, on ne fait que retourner l'image en niveaux de gris)
    return image_gray

# Fonction pour générer des recommandations (fictif pour l'exemple)
def recommandations(image):
    # En fonction des caractéristiques de l'image segmentée, on pourrait donner des recommandations
    # Ici on retourne un texte générique
    return "Recommandations : Arrosez la plante régulièrement et assurez-vous qu'elle reçoit suffisamment de lumière."

# Interface Gradio
def bio_analytica(image):
    # Segmentation de l'image
    image_segmentee = segmenter_image(image)
    
    # Recommandations basées sur l'image (ici, texte fictif)
    reco_text = recommandations(image)
    
    return image_segmentee, reco_text

# Création de l'interface
interface = gr.Interface(
    fn=bio_analytica,                     # Fonction principale
    inputs=gr.Image(type="pil"),          # Entrée : Image de plante
    outputs=[gr.Image(type="pil"), "text"], # Sorties : Image segmentée + Recommandations
    title="Bio Analytica - Analyse des Plantes",
    description="Téléchargez une image de plante pour analyser l'image et obtenir des recommandations.",
    examples=[["exemple_image_plante.jpg"]] # Optionnel : exemples pour tester
)

# Lancement de l'application
interface.launch()
