from roboflow import Roboflow

rf = Roboflow(api_key="XJtNNLYoyAQcoBpU2M67")
project = rf.workspace("objectobjects").project("objects-7fzco")
version = project.version(1)
dataset = version.download("yolov8")