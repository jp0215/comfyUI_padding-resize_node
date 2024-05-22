# comfyUI_padding-resize_node

## Application Scenario

Stable diffusion adapts images with side lengths that are integer multiples of 8 when performing graph generation. If the input image is not an integer multiple of 8, the resulting image will be smaller. When using stable diffusion for local redrawing, it is necessary to ensure that the size of the input and output graphs are the same. To address this issue, a node is developed that padding the image that is not an integer multiple of 8 and resizing it after generation.

## Functional Description

 Padding image to 8x: input image and mask, if the side length is not an integer multiple of 8, expand the side length to the smallest multiple of 8 greater than the original side length. Output padding image and mask.
 Resize to the origin: input the generated image and the original image, crop the generated image to the size of the original image, output the cropped image.

 ## Usage
 Put the two python files into . /ComfyUI/custom_nodes
