import requests


# This function will pass your text to the machine learning model
# and return the top result with the highest confidence

def classify(text):
    key = "f6b93840-a24c-11eb-b330-292323ef1ae2c17e6f14-960d-4e47-825b-4b1232dd2d34"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return label(topMatch)
    else:
        response.raise_for_status()

def label (match):
    
    label = match["class_name"]
    if label == 'PezP':
        return  "Los peces (del latín pisces) son animales vertebrados primariamente acuáticos, generalmente ectotérmicos (regulan su temperatura a partir del medio ambiente) y con respiración por branquias. Suelen estar recubiertos por escamas, y están dotados de aletas, que permiten su movimiento continuo en los medios acuáticos, y branquias, con las que captan el oxígeno disuelto en el agua."
    if label == "AveP":
        return "Las aves son animales vertebrados, de sangre caliente, que caminan, saltan o se mantienen solo sobre las extremidades posteriores,3 mientras que las extremidades anteriores han evolucionado hasta convertirse en alas que, al igual que muchas otras características anatómicas únicas, les permiten, en la mayoría de los casos, volar, si bien no todas vuelan."
    if label == "mamiferoP":
        return "Los mamíferos (Mammalia) son una clase de animales vertebrados amniotas homeotermos (de «sangre caliente») que poseen glándulas mamarias productoras de leche con las que alimentan a las crías. La mayoría son vivíparos (con la excepción de los monotremas: ornitorrinco y equidnas)."
    if label == "ReptilP":
        return " Los reptiles son generalmente carnívoros pero los hay también herbívoros y omnívoros. Todos son ovíparos, nacen de un huevo. La única especie que no tiene cuatro patas es la de las serpientes."

    return ""
    

# CHANGE THIS to something you want your machine learning model to classify
#demo = classify("ave")

#label = demo["class_name"]
#confidence = demo["confidence"]


# CHANGE THIS to do something different with the result
# print ("result: '%s' with %d%% confidence" % (label, confidence))

    






