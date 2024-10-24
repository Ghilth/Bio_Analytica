import numpy as np
from PIL import Image

def mask(img):
    # Étape 1 : Charger et redimensionner correctement l'image
    image = Image.open(img)
    image = image.resize((128, 128))  # Redimensionner avec Pillow

    # Convertir l'image en tableau NumPy
    im = np.array(image)

    # Normaliser l'image (entre 0 et 1) et ajouter une dimension pour le batch
    im = im / 255.0
    im = np.expand_dims(im, axis=0)  # (1, 128, 128, 3)

    # Étape 2 : Prédire le masque
    mask = model.predict(im)

    # Binariser le masque (seuillage)
    mask = (mask > 0.5).astype(np.uint8)  # Convertir en entier 0 ou 1

    # Étape 3 : Enlever les dimensions inutiles (squeeze)
    # Initialement, la forme du masque peut être (1, 128, 128, 1), donc on enlève les dimensions 1
    mask = np.squeeze(mask, axis=0)  # Enlever la première dimension (batch)
    mask = np.squeeze(mask, axis=-1)  # Enlever la dernière dimension (canal unique)

    # Étape 4 : Convertir le masque en image PIL (niveaux de gris)
    image_mask = Image.fromarray(mask * 255)  # Multiplier par 255 pour obtenir un masque binaire visible

    plt.imshow(image_mask)

    # Sauvegarder et afficher le masque
    #image_mask.save('mask.png')
    #plt.show(image_mask)

