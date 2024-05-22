from PIL import Image
import torch
import torchvision.transforms as transforms

class Resize:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s): # 设置要输入的参数
        return {
            "required": {
                "original_image":("IMAGE",),
                "new_image":("IMAGE",),
            },
        }
 
    CATEGORY = "resize_"
 
    RETURN_TYPES = ("IMAGE", )
    FUNCTION = "resize"
 
    def resize(self, original_image, new_image):
        original_width = original_image.shape[1]
        original_height = original_image.shape[2]

        divisible_by_eight = original_width % 8 == 0 and original_height % 8 == 0
        
        if divisible_by_eight:
            cropped_image = new_image
        else:
            new_width = original_width - (original_width % 8)
            new_height = original_height - (original_height % 8)
            
            cropped_image = new_image[:, :original_width, :original_height, :]
        return (cropped_image, )  

NODE_CLASS_MAPPINGS = {
    "function2": Resize,
}
 
NODE_DISPLAY_NAME_MAPPINGS = {
    "function2": "Resize to the origin",
}