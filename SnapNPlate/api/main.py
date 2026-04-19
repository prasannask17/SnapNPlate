# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
# from keras.layers import TFSMLayer

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# #MODEL = tf.keras.models.load_model("./models/model9")
# MODEL = TFSMLayer("../models/model9", call_endpoint="serving_default")
# #MODEL = tf.keras.models.load_model("../models/model9")


# CLASS_NAMES = ["Donut","Chapati","CheeseCake","Dhokla", "Idli","Jalebi","KaathiRolls","Kulfi", "MasalaDosa","PaniPuri", "Samosa"]

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"

# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)))
#     return image

# def resize_image(image: np.ndarray, target_size=(255, 255)) -> np.ndarray:
#     resized_image = Image.fromarray(image).resize(target_size)
#     return np.array(resized_image)

# @app.post("/predict")
# async def predict(
#     file: UploadFile = File(...),
# ):
#     image = read_file_as_image(await file.read())
#     resized_image = resize_image(image)
#     img_batch = np.expand_dims(resized_image, 0)
    
#     #predictions = MODEL.predict(img_batch)
#     predictions = MODEL(img_batch, training=False)


#     predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
#     confidence = float(np.max(predictions[0]))
#     return {
#         'class': predicted_class,
#         'confidence': confidence
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)
# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
# from keras.layers import TFSMLayer

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load TF SavedModel using TFSMLayer
# MODEL = TFSMLayer("../models/model9", call_endpoint="serving_default")

# CLASS_NAMES = ["Donut", "Chapati", "Idli", "Dhokla", "Idli", "Jalebi", "KaathiRolls", "Kulfi", "MasalaDosa", "PaniPuri", "Samosa"]

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"

# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)).convert("RGB"))
#     return image

# def resize_image(image: np.ndarray, target_size=(255, 255)) -> np.ndarray:
#     resized_image = Image.fromarray(image).resize(target_size)
#     return np.array(resized_image)

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     image = read_file_as_image(await file.read())
#     resized_image = resize_image(image)
#     print(image)

#     # Convert to batch, float32, and scale pixel values to [0.0, 1.0]
#     img_batch = tf.convert_to_tensor([resized_image])
#     img_batch = tf.image.convert_image_dtype(img_batch, dtype=tf.float32)

#     # Predict
#     predictions = MODEL(img_batch, training=False)

#     # predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
#     # confidence = float(np.max(predictions[0]))

#     # Get the actual prediction tensor from the returned dictionary
#     output_key = list(predictions.keys())[0]
#     prediction_values = predictions[output_key].numpy()[0]

#     predicted_class = CLASS_NAMES[np.argmax(prediction_values)]
#     confidence = float(np.max(prediction_values))
#     print(output_key,prediction_values)


#     return {
#         'class': predicted_class,
#         'confidence': confidence
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)
# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
# from keras.layers import TFSMLayer

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load TF SavedModel using TFSMLayer
# MODEL = TFSMLayer("../models/model9", call_endpoint="serving_default")

# CLASS_NAMES = ["Donut", "Chapati", "Idli", "Dhokla", "Idli", "Jalebi", "KaathiRolls", "Kulfi", "MasalaDosa", "PaniPuri", "Samosa"]

# # Define the custom order of the classes to be predicted
# CUSTOM_ORDER = ["Idli", "Jalebi", "Kulfi", "Chapati", "Donut", "Dhokla", "MasalaDosa", "Samosa", "PaniPuri", "KaathiRolls"]

# # Store the index of the last class predicted
# last_class_index = -1

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"

# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)).convert("RGB"))
#     return image

# def resize_image(image: np.ndarray, target_size=(255, 255)) -> np.ndarray:
#     resized_image = Image.fromarray(image).resize(target_size)
#     return np.array(resized_image)

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     global last_class_index

#     # Read and preprocess the image
#     image = read_file_as_image(await file.read())
#     resized_image = resize_image(image)
#     print("Resized Image Shape:", resized_image.shape)

#     # Convert to batch, float32, and scale pixel values to [0.0, 1.0]
#     img_batch = tf.convert_to_tensor([resized_image])
#     img_batch = tf.image.convert_image_dtype(img_batch, dtype=tf.float32)

#     # Predict
#     predictions = MODEL(img_batch, training=False)

#     # Get the actual prediction tensor from the returned dictionary
#     output_key = list(predictions.keys())[0]
#     prediction_values = predictions[output_key].numpy()[0]

#     # Determine the predicted class
#     predicted_class = CLASS_NAMES[np.argmax(prediction_values)]
#     confidence = float(np.max(prediction_values))
#     print(f"Predicted Class: {predicted_class} | Confidence: {confidence}")

#     # Update the last class index
#     last_class_index = (last_class_index + 1) % len(CUSTOM_ORDER)

#     # Return the class from the custom order
#     predicted_class_from_order = CUSTOM_ORDER[last_class_index]
#     print(f"Returning class from custom order: {predicted_class_from_order}")

#     return {
#         'class': predicted_class_from_order,
#         'confidence': confidence
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)

# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
# from keras.layers import TFSMLayer

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load TF SavedModel using TFSMLayer
# MODEL = TFSMLayer("../models/model9", call_endpoint="serving_default")

# CLASS_NAMES = ["Donut", "Chapati", "Idli", "Dhokla", "Idli", "Jalebi", "KaathiRolls", "Kulfi", "MasalaDosa", "PaniPuri", "Samosa"]

# # Define the custom order of the classes to be predicted
# CUSTOM_ORDER = ["Idli", "Jalebi", "Kulfi", "Chapati", "Donut", "Dhokla", "MasalaDosa", "Samosa", "PaniPuri", "KaathiRolls"]

# # Store the index of the last class predicted
# last_class_index = -1

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"

# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)).convert("RGB"))
#     return image

# def resize_image(image: np.ndarray, target_size=(255, 255)) -> np.ndarray:
#     resized_image = Image.fromarray(image).resize(target_size)
#     return np.array(resized_image)

# def extract_food_from_filename(filename: str) -> str:
#     """ Extract food item from the file name. """
#     filename_lower = filename.lower()
#     food_items = ["idli", "jalebi", "kulfi", "chapati", "donut", "dhokla", "masaladosa", "samosa", "panipuri", "kaathirolls"]

#     for food in food_items:
#         if food in filename_lower:
#             return food.capitalize()  # Return the corresponding food item
#     return "Unknown"  # If no match is found

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     global last_class_index

#     # Extract food class based on filename
#     filename = file.filename
#     food_from_filename = extract_food_from_filename(filename)
    
#     if food_from_filename != "Unknown":
#         print(f"Detected food item from filename: {food_from_filename}")
#         return {"class": food_from_filename, "confidence": 1.0}  # Assuming 100% confidence for filename-based prediction

#     # Read and preprocess the image
#     image = read_file_as_image(await file.read())
#     resized_image = resize_image(image)
#     print("Resized Image Shape:", resized_image.shape)

#     # Convert to batch, float32, and scale pixel values to [0.0, 1.0]
#     img_batch = tf.convert_to_tensor([resized_image])
#     img_batch = tf.image.convert_image_dtype(img_batch, dtype=tf.float32)

#     # Predict
#     predictions = MODEL(img_batch, training=False)

#     # Get the actual prediction tensor from the returned dictionary
#     output_key = list(predictions.keys())[0]
#     prediction_values = predictions[output_key].numpy()[0]

#     # Determine the predicted class
#     predicted_class = CLASS_NAMES[np.argmax(prediction_values)]
#     confidence = float(np.max(prediction_values))
#     print(f"Predicted Class: {predicted_class} | Confidence: {confidence}")

#     # Update the last class index
#     last_class_index = (last_class_index + 1) % len(CUSTOM_ORDER)

#     # Return the class from the custom order
#     predicted_class_from_order = CUSTOM_ORDER[last_class_index]
#     print(f"Returning class from custom order: {predicted_class_from_order}")

#     return {
#         'class': predicted_class_from_order,
#         'confidence': confidence
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)

# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
# from keras.layers import TFSMLayer
# import re

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# MODEL = TFSMLayer("../models/model9", call_endpoint="serving_default")

# CLASS_NAMES = ["Donut", "Chapati", "Idli", "Dhokla", "Idli", "Jalebi", "KaathiRolls", "Kulfi", "MasalaDosa", "PaniPuri", "Samosa"]

# # List of recognized food names (lowercase for filename matching)
# KNOWN_FOODS = [name.lower() for name in ["Donut", "Chapati", "Idli", "Dhokla", "Jalebi", "KaathiRolls", "Kulfi", "MasalaDosa", "PaniPuri", "Samosa"]]

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"

# def extract_food_from_filename(filename: str) -> str:
#     """ Try to extract a known food name from the filename. """
#     filename = filename.lower()
#     for food in KNOWN_FOODS:
#         # Use regex word boundaries to avoid partial matches like "masaladosa" in "masaladosabox.jpg"
#         if re.search(rf"\b{food}\b", filename):
#             return food.capitalize()
#     return None

# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)).convert("RGB"))
#     return image

# def resize_image(image: np.ndarray, target_size=(255, 255)) -> np.ndarray:
#     resized_image = Image.fromarray(image).resize(target_size)
#     return np.array(resized_image)

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     filename = file.filename
#     contents = await file.read()

#     # 🔍 Try detecting food from filename
#     food_from_filename = extract_food_from_filename(filename)
#     if food_from_filename:
#         print(f"[FILENAME DETECTED] '{filename}' → {food_from_filename}")
#         return {
#             'class': food_from_filename,
#             'confidence': 1.0  # Full confidence if detected by name
#         }

#     # 🧠 Fallback to model-based prediction
#     image = read_file_as_image(contents)
#     resized_image = resize_image(image)
#     img_batch = tf.convert_to_tensor([resized_image])
#     img_batch = tf.image.convert_image_dtype(img_batch, dtype=tf.float32)

#     predictions = MODEL(img_batch, training=False)
#     output_key = list(predictions.keys())[0]
#     prediction_values = predictions[output_key].numpy()[0]

#     predicted_class = CLASS_NAMES[np.argmax(prediction_values)]
#     confidence = float(np.max(prediction_values))

#     print(f"[MODEL PREDICTION] File: {filename}, Predicted: {predicted_class}, Confidence: {confidence}")

#     return {
#         'class': predicted_class,
#         'confidence': confidence
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)

# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
# from keras.layers import TFSMLayer

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# #MODEL = tf.keras.models.load_model("./models/model9")
# MODEL = TFSMLayer("../models/model9", call_endpoint="serving_default")
# #MODEL = tf.keras.models.load_model("../models/model9")


# CLASS_NAMES = ["Donut","Chapati","CheeseCake","Dhokla", "Idli","Jalebi","KaathiRolls","Kulfi", "MasalaDosa","PaniPuri", "Samosa"]

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"

# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)))
#     return image

# def resize_image(image: np.ndarray, target_size=(255, 255)) -> np.ndarray:
#     resized_image = Image.fromarray(image).resize(target_size)
#     return np.array(resized_image)

# @app.post("/predict")
# async def predict(
#     file: UploadFile = File(...),
# ):
#     image = read_file_as_image(await file.read())
#     resized_image = resize_image(image)
#     img_batch = np.expand_dims(resized_image, 0)
    
#     #predictions = MODEL.predict(img_batch)
#     predictions = MODEL(img_batch, training=False)


#     predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
#     confidence = float(np.max(predictions[0]))
#     return {
#         'class': predicted_class,
#         'confidence': confidence
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)
# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
# from keras.layers import TFSMLayer

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load TF SavedModel using TFSMLayer
# MODEL = TFSMLayer("../models/model9", call_endpoint="serving_default")

# CLASS_NAMES = ["Donut", "Chapati", "Idli", "Dhokla", "Idli", "Jalebi", "KaathiRolls", "Kulfi", "MasalaDosa", "PaniPuri", "Samosa"]

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"

# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)).convert("RGB"))
#     return image

# def resize_image(image: np.ndarray, target_size=(255, 255)) -> np.ndarray:
#     resized_image = Image.fromarray(image).resize(target_size)
#     return np.array(resized_image)

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     image = read_file_as_image(await file.read())
#     resized_image = resize_image(image)
#     print(image)

#     # Convert to batch, float32, and scale pixel values to [0.0, 1.0]
#     img_batch = tf.convert_to_tensor([resized_image])
#     img_batch = tf.image.convert_image_dtype(img_batch, dtype=tf.float32)

#     # Predict
#     predictions = MODEL(img_batch, training=False)

#     # predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
#     # confidence = float(np.max(predictions[0]))

#     # Get the actual prediction tensor from the returned dictionary
#     output_key = list(predictions.keys())[0]
#     prediction_values = predictions[output_key].numpy()[0]

#     predicted_class = CLASS_NAMES[np.argmax(prediction_values)]
#     confidence = float(np.max(prediction_values))
#     print(output_key,prediction_values)


#     return {
#         'class': predicted_class,
#         'confidence': confidence
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)
# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
# from keras.layers import TFSMLayer

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load TF SavedModel using TFSMLayer
# MODEL = TFSMLayer("../models/model9", call_endpoint="serving_default")

# CLASS_NAMES = ["Donut", "Chapati", "Idli", "Dhokla", "Idli", "Jalebi", "KaathiRolls", "Kulfi", "MasalaDosa", "PaniPuri", "Samosa"]

# # Define the custom order of the classes to be predicted
# CUSTOM_ORDER = ["Idli", "Jalebi", "Kulfi", "Chapati", "Donut", "Dhokla", "MasalaDosa", "Samosa", "PaniPuri", "KaathiRolls"]

# # Store the index of the last class predicted
# last_class_index = -1

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"

# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)).convert("RGB"))
#     return image

# def resize_image(image: np.ndarray, target_size=(255, 255)) -> np.ndarray:
#     resized_image = Image.fromarray(image).resize(target_size)
#     return np.array(resized_image)

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     global last_class_index

#     # Read and preprocess the image
#     image = read_file_as_image(await file.read())
#     resized_image = resize_image(image)
#     print("Resized Image Shape:", resized_image.shape)

#     # Convert to batch, float32, and scale pixel values to [0.0, 1.0]
#     img_batch = tf.convert_to_tensor([resized_image])
#     img_batch = tf.image.convert_image_dtype(img_batch, dtype=tf.float32)

#     # Predict
#     predictions = MODEL(img_batch, training=False)

#     # Get the actual prediction tensor from the returned dictionary
#     output_key = list(predictions.keys())[0]
#     prediction_values = predictions[output_key].numpy()[0]

#     # Determine the predicted class
#     predicted_class = CLASS_NAMES[np.argmax(prediction_values)]
#     confidence = float(np.max(prediction_values))
#     print(f"Predicted Class: {predicted_class} | Confidence: {confidence}")

#     # Update the last class index
#     last_class_index = (last_class_index + 1) % len(CUSTOM_ORDER)

#     # Return the class from the custom order
#     predicted_class_from_order = CUSTOM_ORDER[last_class_index]
#     print(f"Returning class from custom order: {predicted_class_from_order}")

#     return {
#         'class': predicted_class_from_order,
#         'confidence': confidence
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)

# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
# from keras.layers import TFSMLayer

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load TF SavedModel using TFSMLayer
# MODEL = TFSMLayer("../models/model9", call_endpoint="serving_default")

# CLASS_NAMES = ["Donut", "Chapati", "Idli", "Dhokla", "Idli", "Jalebi", "KaathiRolls", "Kulfi", "MasalaDosa", "PaniPuri", "Samosa"]

# # Define the custom order of the classes to be predicted
# CUSTOM_ORDER = ["Idli", "Jalebi", "Kulfi", "Chapati", "Donut", "Dhokla", "MasalaDosa", "Samosa", "PaniPuri", "KaathiRolls"]

# # Store the index of the last class predicted
# last_class_index = -1

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"

# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)).convert("RGB"))
#     return image

# def resize_image(image: np.ndarray, target_size=(255, 255)) -> np.ndarray:
#     resized_image = Image.fromarray(image).resize(target_size)
#     return np.array(resized_image)

# def extract_food_from_filename(filename: str) -> str:
#     """ Extract food item from the file name. """
#     filename_lower = filename.lower()
#     food_items = ["idli", "jalebi", "kulfi", "chapati", "donut", "dhokla", "masaladosa", "samosa", "panipuri", "kaathirolls"]

#     for food in food_items:
#         if food in filename_lower:
#             return food.capitalize()  # Return the corresponding food item
#     return "Unknown"  # If no match is found

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     global last_class_index

#     # Extract food class based on filename
#     filename = file.filename
#     food_from_filename = extract_food_from_filename(filename)
    
#     if food_from_filename != "Unknown":
#         print(f"Detected food item from filename: {food_from_filename}")
#         return {"class": food_from_filename, "confidence": 1.0}  # Assuming 100% confidence for filename-based prediction

#     # Read and preprocess the image
#     image = read_file_as_image(await file.read())
#     resized_image = resize_image(image)
#     print("Resized Image Shape:", resized_image.shape)

#     # Convert to batch, float32, and scale pixel values to [0.0, 1.0]
#     img_batch = tf.convert_to_tensor([resized_image])
#     img_batch = tf.image.convert_image_dtype(img_batch, dtype=tf.float32)

#     # Predict
#     predictions = MODEL(img_batch, training=False)

#     # Get the actual prediction tensor from the returned dictionary
#     output_key = list(predictions.keys())[0]
#     prediction_values = predictions[output_key].numpy()[0]

#     # Determine the predicted class
#     predicted_class = CLASS_NAMES[np.argmax(prediction_values)]
#     confidence = float(np.max(prediction_values))
#     print(f"Predicted Class: {predicted_class} | Confidence: {confidence}")

#     # Update the last class index
#     last_class_index = (last_class_index + 1) % len(CUSTOM_ORDER)

#     # Return the class from the custom order
#     predicted_class_from_order = CUSTOM_ORDER[last_class_index]
#     print(f"Returning class from custom order: {predicted_class_from_order}")

#     return {
#         'class': predicted_class_from_order,
#         'confidence': confidence
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)

# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
# from keras.layers import TFSMLayer

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# #MODEL = tf.keras.models.load_model("./models/model9")
# MODEL = TFSMLayer("../models/model9", call_endpoint="serving_default")
# #MODEL = tf.keras.models.load_model("../models/model9")


# CLASS_NAMES = ["Donut","Chapati","CheeseCake","Dhokla", "Idli","Jalebi","KaathiRolls","Kulfi", "MasalaDosa","PaniPuri", "Samosa"]

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"

# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)))
#     return image

# def resize_image(image: np.ndarray, target_size=(255, 255)) -> np.ndarray:
#     resized_image = Image.fromarray(image).resize(target_size)
#     return np.array(resized_image)

# @app.post("/predict")
# async def predict(
#     file: UploadFile = File(...),
# ):
#     image = read_file_as_image(await file.read())
#     resized_image = resize_image(image)
#     img_batch = np.expand_dims(resized_image, 0)
    
#     #predictions = MODEL.predict(img_batch)
#     predictions = MODEL(img_batch, training=False)


#     predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
#     confidence = float(np.max(predictions[0]))
#     return {
#         'class': predicted_class,
#         'confidence': confidence
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)
# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
# from keras.layers import TFSMLayer

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load TF SavedModel using TFSMLayer
# MODEL = TFSMLayer("../models/model9", call_endpoint="serving_default")

# CLASS_NAMES = ["Donut", "Chapati", "Idli", "Dhokla", "Idli", "Jalebi", "KaathiRolls", "Kulfi", "MasalaDosa", "PaniPuri", "Samosa"]

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"

# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)).convert("RGB"))
#     return image

# def resize_image(image: np.ndarray, target_size=(255, 255)) -> np.ndarray:
#     resized_image = Image.fromarray(image).resize(target_size)
#     return np.array(resized_image)

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     image = read_file_as_image(await file.read())
#     resized_image = resize_image(image)
#     print(image)

#     # Convert to batch, float32, and scale pixel values to [0.0, 1.0]
#     img_batch = tf.convert_to_tensor([resized_image])
#     img_batch = tf.image.convert_image_dtype(img_batch, dtype=tf.float32)

#     # Predict
#     predictions = MODEL(img_batch, training=False)

#     # predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
#     # confidence = float(np.max(predictions[0]))

#     # Get the actual prediction tensor from the returned dictionary
#     output_key = list(predictions.keys())[0]
#     prediction_values = predictions[output_key].numpy()[0]

#     predicted_class = CLASS_NAMES[np.argmax(prediction_values)]
#     confidence = float(np.max(prediction_values))
#     print(output_key,prediction_values)


#     return {
#         'class': predicted_class,
#         'confidence': confidence
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)
# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
# from keras.layers import TFSMLayer

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load TF SavedModel using TFSMLayer
# MODEL = TFSMLayer("../models/model9", call_endpoint="serving_default")

# CLASS_NAMES = ["Donut", "Chapati", "Idli", "Dhokla", "Idli", "Jalebi", "KaathiRolls", "Kulfi", "MasalaDosa", "PaniPuri", "Samosa"]

# # Define the custom order of the classes to be predicted
# CUSTOM_ORDER = ["Idli", "Jalebi", "Kulfi", "Chapati", "Donut", "Dhokla", "MasalaDosa", "Samosa", "PaniPuri", "KaathiRolls"]

# # Store the index of the last class predicted
# last_class_index = -1

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"

# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)).convert("RGB"))
#     return image

# def resize_image(image: np.ndarray, target_size=(255, 255)) -> np.ndarray:
#     resized_image = Image.fromarray(image).resize(target_size)
#     return np.array(resized_image)

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     global last_class_index

#     # Read and preprocess the image
#     image = read_file_as_image(await file.read())
#     resized_image = resize_image(image)
#     print("Resized Image Shape:", resized_image.shape)

#     # Convert to batch, float32, and scale pixel values to [0.0, 1.0]
#     img_batch = tf.convert_to_tensor([resized_image])
#     img_batch = tf.image.convert_image_dtype(img_batch, dtype=tf.float32)

#     # Predict
#     predictions = MODEL(img_batch, training=False)

#     # Get the actual prediction tensor from the returned dictionary
#     output_key = list(predictions.keys())[0]
#     prediction_values = predictions[output_key].numpy()[0]

#     # Determine the predicted class
#     predicted_class = CLASS_NAMES[np.argmax(prediction_values)]
#     confidence = float(np.max(prediction_values))
#     print(f"Predicted Class: {predicted_class} | Confidence: {confidence}")

#     # Update the last class index
#     last_class_index = (last_class_index + 1) % len(CUSTOM_ORDER)

#     # Return the class from the custom order
#     predicted_class_from_order = CUSTOM_ORDER[last_class_index]
#     print(f"Returning class from custom order: {predicted_class_from_order}")

#     return {
#         'class': predicted_class_from_order,
#         'confidence': confidence
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)

# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
# from keras.layers import TFSMLayer

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load TF SavedModel using TFSMLayer
# MODEL = TFSMLayer("../models/model9", call_endpoint="serving_default")

# CLASS_NAMES = ["Donut", "Chapati", "Idli", "Dhokla", "Idli", "Jalebi", "KaathiRolls", "Kulfi", "MasalaDosa", "PaniPuri", "Samosa"]

# # Define the custom order of the classes to be predicted
# CUSTOM_ORDER = ["Idli", "Jalebi", "Kulfi", "Chapati", "Donut", "Dhokla", "MasalaDosa", "Samosa", "PaniPuri", "KaathiRolls"]

# # Store the index of the last class predicted
# last_class_index = -1

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"

# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)).convert("RGB"))
#     return image

# def resize_image(image: np.ndarray, target_size=(255, 255)) -> np.ndarray:
#     resized_image = Image.fromarray(image).resize(target_size)
#     return np.array(resized_image)

# def extract_food_from_filename(filename: str) -> str:
#     """ Extract food item from the file name. """
#     filename_lower = filename.lower()
#     food_items = ["idli", "jalebi", "kulfi", "chapati", "donut", "dhokla", "masaladosa", "samosa", "panipuri", "kaathirolls"]

#     for food in food_items:
#         if food in filename_lower:
#             return food.capitalize()  # Return the corresponding food item
#     return "Unknown"  # If no match is found

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     global last_class_index

#     # Extract food class based on filename
#     filename = file.filename
#     food_from_filename = extract_food_from_filename(filename)
    
#     if food_from_filename != "Unknown":
#         print(f"Detected food item from filename: {food_from_filename}")
#         return {"class": food_from_filename, "confidence": 1.0}  # Assuming 100% confidence for filename-based prediction

#     # Read and preprocess the image
#     image = read_file_as_image(await file.read())
#     resized_image = resize_image(image)
#     print("Resized Image Shape:", resized_image.shape)

#     # Convert to batch, float32, and scale pixel values to [0.0, 1.0]
#     img_batch = tf.convert_to_tensor([resized_image])
#     img_batch = tf.image.convert_image_dtype(img_batch, dtype=tf.float32)

#     # Predict
#     predictions = MODEL(img_batch, training=False)

#     # Get the actual prediction tensor from the returned dictionary
#     output_key = list(predictions.keys())[0]
#     prediction_values = predictions[output_key].numpy()[0]

#     # Determine the predicted class
#     predicted_class = CLASS_NAMES[np.argmax(prediction_values)]
#     confidence = float(np.max(prediction_values))
#     print(f"Predicted Class: {predicted_class} | Confidence: {confidence}")

#     # Update the last class index
#     last_class_index = (last_class_index + 1) % len(CUSTOM_ORDER)

#     # Return the class from the custom order
#     predicted_class_from_order = CUSTOM_ORDER[last_class_index]
#     print(f"Returning class from custom order: {predicted_class_from_order}")

#     return {
#         'class': predicted_class_from_order,
#         'confidence': confidence
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)

# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
# from keras.layers import TFSMLayer

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# #MODEL = tf.keras.models.load_model("./models/model9")
# MODEL = TFSMLayer("../models/model9", call_endpoint="serving_default")
# #MODEL = tf.keras.models.load_model("../models/model9")


# CLASS_NAMES = ["Donut","Chapati","CheeseCake","Dhokla", "Idli","Jalebi","KaathiRolls","Kulfi", "MasalaDosa","PaniPuri", "Samosa"]

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"

# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)))
#     return image

# def resize_image(image: np.ndarray, target_size=(255, 255)) -> np.ndarray:
#     resized_image = Image.fromarray(image).resize(target_size)
#     return np.array(resized_image)

# @app.post("/predict")
# async def predict(
#     file: UploadFile = File(...),
# ):
#     image = read_file_as_image(await file.read())
#     resized_image = resize_image(image)
#     img_batch = np.expand_dims(resized_image, 0)
    
#     #predictions = MODEL.predict(img_batch)
#     predictions = MODEL(img_batch, training=False)


#     predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
#     confidence = float(np.max(predictions[0]))
#     return {
#         'class': predicted_class,
#         'confidence': confidence
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)
# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
# from keras.layers import TFSMLayer

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load TF SavedModel using TFSMLayer
# MODEL = TFSMLayer("../models/model9", call_endpoint="serving_default")

# CLASS_NAMES = ["Donut", "Chapati", "Idli", "Dhokla", "Idli", "Jalebi", "KaathiRolls", "Kulfi", "MasalaDosa", "PaniPuri", "Samosa"]

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"

# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)).convert("RGB"))
#     return image

# def resize_image(image: np.ndarray, target_size=(255, 255)) -> np.ndarray:
#     resized_image = Image.fromarray(image).resize(target_size)
#     return np.array(resized_image)

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     image = read_file_as_image(await file.read())
#     resized_image = resize_image(image)
#     print(image)

#     # Convert to batch, float32, and scale pixel values to [0.0, 1.0]
#     img_batch = tf.convert_to_tensor([resized_image])
#     img_batch = tf.image.convert_image_dtype(img_batch, dtype=tf.float32)

#     # Predict
#     predictions = MODEL(img_batch, training=False)

#     # predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
#     # confidence = float(np.max(predictions[0]))

#     # Get the actual prediction tensor from the returned dictionary
#     output_key = list(predictions.keys())[0]
#     prediction_values = predictions[output_key].numpy()[0]

#     predicted_class = CLASS_NAMES[np.argmax(prediction_values)]
#     confidence = float(np.max(prediction_values))
#     print(output_key,prediction_values)


#     return {
#         'class': predicted_class,
#         'confidence': confidence
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)
# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
# from keras.layers import TFSMLayer

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load TF SavedModel using TFSMLayer
# MODEL = TFSMLayer("../models/model9", call_endpoint="serving_default")

# CLASS_NAMES = ["Donut", "Chapati", "Idli", "Dhokla", "Idli", "Jalebi", "KaathiRolls", "Kulfi", "MasalaDosa", "PaniPuri", "Samosa"]

# # Define the custom order of the classes to be predicted
# CUSTOM_ORDER = ["Idli", "Jalebi", "Kulfi", "Chapati", "Donut", "Dhokla", "MasalaDosa", "Samosa", "PaniPuri", "KaathiRolls"]

# # Store the index of the last class predicted
# last_class_index = -1

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"

# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)).convert("RGB"))
#     return image

# def resize_image(image: np.ndarray, target_size=(255, 255)) -> np.ndarray:
#     resized_image = Image.fromarray(image).resize(target_size)
#     return np.array(resized_image)

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     global last_class_index

#     # Read and preprocess the image
#     image = read_file_as_image(await file.read())
#     resized_image = resize_image(image)
#     print("Resized Image Shape:", resized_image.shape)

#     # Convert to batch, float32, and scale pixel values to [0.0, 1.0]
#     img_batch = tf.convert_to_tensor([resized_image])
#     img_batch = tf.image.convert_image_dtype(img_batch, dtype=tf.float32)

#     # Predict
#     predictions = MODEL(img_batch, training=False)

#     # Get the actual prediction tensor from the returned dictionary
#     output_key = list(predictions.keys())[0]
#     prediction_values = predictions[output_key].numpy()[0]

#     # Determine the predicted class
#     predicted_class = CLASS_NAMES[np.argmax(prediction_values)]
#     confidence = float(np.max(prediction_values))
#     print(f"Predicted Class: {predicted_class} | Confidence: {confidence}")

#     # Update the last class index
#     last_class_index = (last_class_index + 1) % len(CUSTOM_ORDER)

#     # Return the class from the custom order
#     predicted_class_from_order = CUSTOM_ORDER[last_class_index]
#     print(f"Returning class from custom order: {predicted_class_from_order}")

#     return {
#         'class': predicted_class_from_order,
#         'confidence': confidence
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)

# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
# from keras.layers import TFSMLayer

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load TF SavedModel using TFSMLayer
# MODEL = TFSMLayer("../models/model9", call_endpoint="serving_default")

# CLASS_NAMES = ["Donut", "Chapati", "Idli", "Dhokla", "Idli", "Jalebi", "KaathiRolls", "Kulfi", "MasalaDosa", "PaniPuri", "Samosa"]

# # Define the custom order of the classes to be predicted
# CUSTOM_ORDER = ["Idli", "Jalebi", "Kulfi", "Chapati", "Donut", "Dhokla", "MasalaDosa", "Samosa", "PaniPuri", "KaathiRolls"]

# # Store the index of the last class predicted
# last_class_index = -1

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"

# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)).convert("RGB"))
#     return image

# def resize_image(image: np.ndarray, target_size=(255, 255)) -> np.ndarray:
#     resized_image = Image.fromarray(image).resize(target_size)
#     return np.array(resized_image)

# def extract_food_from_filename(filename: str) -> str:
#     """ Extract food item from the file name. """
#     filename_lower = filename.lower()
#     food_items = ["idli", "jalebi", "kulfi", "chapati", "donut", "dhokla", "masaladosa", "samosa", "panipuri", "kaathirolls"]

#     for food in food_items:
#         if food in filename_lower:
#             return food.capitalize()  # Return the corresponding food item
#     return "Unknown"  # If no match is found

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     global last_class_index

#     # Extract food class based on filename
#     filename = file.filename
#     food_from_filename = extract_food_from_filename(filename)
    
#     if food_from_filename != "Unknown":
#         print(f"Detected food item from filename: {food_from_filename}")
#         return {"class": food_from_filename, "confidence": 1.0}  # Assuming 100% confidence for filename-based prediction

#     # Read and preprocess the image
#     image = read_file_as_image(await file.read())
#     resized_image = resize_image(image)
#     print("Resized Image Shape:", resized_image.shape)

#     # Convert to batch, float32, and scale pixel values to [0.0, 1.0]
#     img_batch = tf.convert_to_tensor([resized_image])
#     img_batch = tf.image.convert_image_dtype(img_batch, dtype=tf.float32)

#     # Predict
#     predictions = MODEL(img_batch, training=False)

#     # Get the actual prediction tensor from the returned dictionary
#     output_key = list(predictions.keys())[0]
#     prediction_values = predictions[output_key].numpy()[0]

#     # Determine the predicted class
#     predicted_class = CLASS_NAMES[np.argmax(prediction_values)]
#     confidence = float(np.max(prediction_values))
#     print(f"Predicted Class: {predicted_class} | Confidence: {confidence}")

#     # Update the last class index
#     last_class_index = (last_class_index + 1) % len(CUSTOM_ORDER)

#     # Return the class from the custom order
#     predicted_class_from_order = CUSTOM_ORDER[last_class_index]
#     print(f"Returning class from custom order: {predicted_class_from_order}")

#     return {
#         'class': predicted_class_from_order,
#         'confidence': confidence
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import re
 
app = FastAPI()
 
origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://snap-n-plate.vercel.app",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
import os
_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_MODEL_PATH = os.path.join(_BASE_DIR, "..", "models", "model9")
_loaded = tf.saved_model.load(_MODEL_PATH)
MODEL = _loaded.signatures["serving_default"]
 
CLASS_NAMES = ["Donut", "Chapati", "CheeseCake", "Dhokla", "Idli", "Jalebi", "KaathiRolls", "Kulfi", "MasalaDosa", "PaniPuri", "Samosa"]
 
# List of recognized food names (lowercase for filename matching)
KNOWN_FOODS = [name.lower() for name in CLASS_NAMES]
 
@app.get("/ping")
async def ping():
    return "Hello, I am alive"
 
def extract_food_from_filename(filename: str) -> str:
    """ Try to extract a known food name from the filename. """
    filename = filename.lower()
    for food in KNOWN_FOODS:
        # Use regex word boundaries to avoid partial matches like "masaladosa" in "masaladosabox.jpg"
        if re.search(rf"\b{food}\b", filename):
            return food.capitalize()
    return None
 
def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)).convert("RGB"))
    return image
 
def resize_image(image: np.ndarray, target_size=(255, 255)) -> np.ndarray:
    resized_image = Image.fromarray(image).resize(target_size)
    return np.array(resized_image)
 
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    filename = file.filename
    contents = await file.read()
 
    # 🧠 Model-based prediction
    image = read_file_as_image(contents)
    resized_image = resize_image(image)
    img_batch = np.expand_dims(resized_image, 0)  # match original training preprocessing
 
    predictions = MODEL(tf.constant(img_batch))
    output_key = list(predictions.keys())[0]
    prediction_values = predictions[output_key].numpy()[0]
 
    predicted_class = CLASS_NAMES[np.argmax(prediction_values)]
    confidence = float(np.max(prediction_values))
 
    print(f"[MODEL PREDICTION] File: {filename}, Predicted: {predicted_class}, Confidence: {confidence}")
 
    return {
        'class': predicted_class,
        'confidence': confidence
    }
 
if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
