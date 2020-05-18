import insightface.face_model as face_model
import argparse
import cv2


class InsightfaceEmbedder:
    def __init__(self, model_path, epoch_num='0000', image_size=(112, 112),
                 ):
        self.model_path = ','.join([model_path, epoch_num])
        args = argparse.Namespace()
        args.model = self.model_path
        args.det = 0
        args.flip = 0
        args.threshold = 1.24
        args.ga_model = ''
        args.image_size = ",".join([str(i) for i in image_size])
        self.model = face_model.FaceModel(args)

    def embed_image(self, image):
        preprocessed = self.model.get_input(image)

        if preprocessed is None:   
            return []
            # if self.no_face_raise:
            #     raise Exception("No face detected!")
            # else:
            #     return None

        embedding = self.model.get_feature(preprocessed)
        return embedding
