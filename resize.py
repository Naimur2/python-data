import mylib

CURRENT_PATH = "NoiseFree_Original__augmented"
DESTINATION_PATH = "NoiseFree_Original__augmented_New_SPLIT"
IMAGE_SIZE = (224, 224)


# mylib.copy_folders(CURRENT_PATH, DESTINATION_PATH)
# mylib.resize_images(CURRENT_PATH, DESTINATION_PATH, IMAGE_SIZE)
# mylib.split_to("Noisefree_128x128", "Noisefree_128x128_split", 0.9, 0.1, 0)
mylib.split_to(CURRENT_PATH,
               DESTINATION_PATH, 0.15, 0.8, 0.05)


# mylib.get_folders(CURRENT_PATH)
