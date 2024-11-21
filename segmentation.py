import cv2
import numpy as np
from sklearn.cluster import KMeans

def segment(image_path):
    # Charger l'image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convertir BGR en RGB
    h, w, c = image.shape

    # Reshape pour obtenir un tableau de pixels
    pixels = image.reshape(-1, 3)  # Dimension (H*W, 3)

    # Nombre de clusters
    K = 2

    # Application de K-means clustering
    kmeans = KMeans(n_clusters=K, random_state=0, n_init='auto')
    kmeans.fit(pixels)

    # Remplacer chaque pixel par le centre du cluster auquel il appartient
    segmented_pixels = kmeans.cluster_centers_[kmeans.labels_]
    segmented_image = segmented_pixels.reshape(h, w, 3).astype(np.uint8)

    # Convertir l'image segmentée en niveaux de gris
    gray_image = cv2.cvtColor(segmented_image, cv2.COLOR_RGB2GRAY)

    gray_image=cv2.resize(gray_image,(500,500),interpolation=cv2.INTER_AREA)


    # Sauvegarder l'image en noir et blanc
    cv2.imwrite('image_segmented.jpg', gray_image)
segment("feuille.jpg")