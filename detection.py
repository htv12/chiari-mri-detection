from roboflow import Roboflow
import json


rf = Roboflow(api_key="8fupKQTma679qZwA58JX")  # Roboflow API key
project = rf.workspace().project("chiari-mri-detection")  # Roboflow project name
model = project.version(2).model  # Roboflow version number

# infer on a local image
def infer(filePath):  # Run the defect detection model
    return json.dumps(model.predict(filePath, confidence=77).json())  # Returns the detection data from the image

def parse(inference):
    if 'chiari' in inference:  # Check if the inference contains chiari
        return 'Chiari'
    else:
        return 'Nothing Detected'