import mylib

CURRENT_PATH = "NoiseFree_Original"
DESTINATION_PATH = "Noisefree_64x64"
IMAGE_SIZE = (64, 64)


# mylib.copy_folders(CURRENT_PATH, DESTINATION_PATH)
# mylib.resize_images(CURRENT_PATH, DESTINATION_PATH, IMAGE_SIZE)
# mylib.split_to("Noisefree_128x128", "Noisefree_128x128_split", 0.9, 0.1, 0)
mylib.split_to("augmented_224x224___reflect",
               "augmented_224x224___reflect_split_train", 0.8, 0.2)
