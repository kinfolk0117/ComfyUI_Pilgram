import sys
import os

import pilgram2
import torchvision.transforms as transforms

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "comfy"))

pilgram_filters = [
    "_1977",
    "aden",
    "amaro",
    "ashby",
    "brannan",
    "brooklyn",
    "charmes",
    "clarendon",
    "crema",
    "dogpatch",
    "earlybird",
    "gingham",
    "ginza",
    "hefe",
    "helena",
    "hudson",
    "inkwell",
    "juno",
    "kelvin",
    "lark",
    "lofi",
    "ludwig",
    "maven",
    "mayfair",
    "moon",
    "nashville",
    "perpetua",
    "poprocket",
    "reyes",
    "rise",
    "sierra",
    "skyline",
    "slumber",
    "stinson",
    "sutro",
    "toaster",
    "valencia",
    "walden",
    "willow",
    "xpro2",
]


class Pilgram:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"image": ("IMAGE",), "pilgram_filter": (pilgram_filters,)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "pilgram"
    CATEGORY = "utils"

    def pilgram(self, image, pilgram_filter):
        tensor = image
        tensor = tensor.squeeze(0).permute(2, 0, 1)
        print(tensor.shape)
        input_image = transforms.ToPILImage()(tensor)

        im = getattr(pilgram2, pilgram_filter)(input_image)

        im = transforms.ToTensor()(im)

        print(im.shape)
        im = im.unsqueeze(0).permute(0, 2, 3, 1)
        print(im.shape)

        return [im]


NODE_CLASS_MAPPINGS = {
    "Pilgram": Pilgram,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Pilgram": "Pilgram",
}
