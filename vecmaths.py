# Toutes les fonctions avec les bvails de matrices, vecteurs, calculs d'intersection...
import numpy as np
def plane_line_intersection(plane, AB):
    """
        Return le point (np.array) d'intersection entre un plan plane et une droite AB

            plane (numpy.array): défini par un point O et deux vecteurs non colinéaires de ce plan
            AB (np.array(2, 2)) : la droite

            Return None si pas d'intersection
    """

    return