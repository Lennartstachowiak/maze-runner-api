from db import models
from sqlalchemy_schemadisplay import create_uml_graph
from sqlalchemy.orm import class_mapper

# lets find all the mappers in our model
mappers = []
for attr_name in dir(models):
    if attr_name.startswith("_"):
        continue  # Skip private attributes and methods
    attr_class = getattr(models, attr_name)
    if hasattr(attr_class, "__mapper__"):
        mappers.append(class_mapper(attr_class))

# pass them to the function and set some formatting options
graph = create_uml_graph(mappers)
graph.write("db/schema.png", prog="dot", format="png")
