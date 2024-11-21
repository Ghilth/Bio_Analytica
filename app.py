import gradio as gr
from PIL import Image
import numpy as np
from segmentation import segment  

# Fonction principale de l'application
def bio_analytica(image):
    """
    Analyse une image de feuille de plante, segmente les anomalies et retourne l'image segmentée.
    
    Args:
        image (PIL.Image): Image téléchargée par l'utilisateur.
        
    Returns:
        PIL.Image: Image segmentée avec anomalies mises en évidence.
    """
    # Sauvegarder temporairement l'image téléchargée
    image_path = "temp_uploaded_image.jpg"
    image.save(image_path)
    
    # Appeler la fonction segment pour traiter l'image
    segment(image_path)  
    
    # Charger l'image segmentée pour la renvoyer dans l'interface
    segmented_image = Image.open("image_segmented.jpg")
    
    return segmented_image

# Interface utilisateur Gradio
interface = gr.Interface(
    fn=bio_analytica,  # Fonction de traitement
    inputs=gr.Image(type="pil"),  # Entrée : Image téléchargée
    outputs=gr.Image(type="pil"),  # Sortie : Image segmentée

    title="🌿 Analyse des Feuilles de Plantes - Détection d'Anomalies",

    description="""
    <div style="text-align: center;">
        <h2 style="color: green;">Bio Analytica 🌱</h2>
        <p style="font-size: 16px; color: white;">
            Téléchargez une image de feuille de plante.<br>
            Notre outil segmente l'image et fait ressortir les anomalies présentes sur la feuille.<br>
            Obtenez des informations visuelles claires sur l'état de vos plantes 🌿.
        </p>
    </div>
    """,
    examples=[["feuille.jpg"], ["feuille_segment.jpg"]],  # Exemples d'images pour test
    flagging_mode="never",  # Désactiver le signalement des résultats
    theme="dark"  # Thème simple
)

# Lancement de l'application
if __name__ == "__main__":
    interface.launch()
