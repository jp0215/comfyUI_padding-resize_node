from PIL import Image
import torch
import torchvision.transforms as transforms

class Padding:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s): # 设置要输入的参数
        return {
            "required": {
                "image": ("IMAGE",),
                "mask":("MASK",),
            },
        }
 
    CATEGORY = "padding"
 
    RETURN_TYPES = ("IMAGE", "MASK")
    FUNCTION = "padding"
 
    def padding(self, image, mask):
        height, width = image.shape[1], image.shape[2]
        
        # Calculate the target dimensions that are multiples of 8
        target_height = height if height % 8 == 0 else height + (8 - height % 8)
        target_width = width if width % 8 == 0 else width + (8 - width % 8)
        
        # If the dimensions are already multiples of 8, return the original tensors
        if target_height == height and target_width == width:
            return (image, mask)
        
        # Create a new tensor for the padded image
        padded_image = torch.zeros((image.shape[0], target_height, target_width, image.shape[3]), dtype=image.dtype)
        # image = image.permute(0, 3, 2, 1)
        # comfyUI中，image的格式为：[batch_size, height, width, channels]
        padded_image[:, :height, :width, :] = image
        
        # Create a new tensor for the padded mask
        padded_mask = torch.zeros((target_height, target_width), dtype=mask.dtype)
        padded_mask[:height, :width] = mask
    
        return (padded_image, padded_mask)  

NODE_CLASS_MAPPINGS = {
    "function": Padding,
}
 
NODE_DISPLAY_NAME_MAPPINGS = {
    "function": "Padding image to 8x",
}