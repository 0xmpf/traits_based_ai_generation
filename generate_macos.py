# Generate_macos.py

from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
import torch
from utils import get_trait,write_trait_to_json

path = 'fluently/Fluently-XL-v4'  # Path to the chosen model-type

# Insert negative prompt below. Default negative prompt for portrait shot.
negative_prompt = "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck"

# Number of generations
n=10

torch.set_grad_enabled(False)

device = 'cpu'  # Use 'cpu' instead of 'cuda' on MacOS

with torch.inference_mode():
    gen = torch.Generator(device).manual_seed(1674753452)
    pipe = DiffusionPipeline.from_pretrained(path, torch_dtype=torch.float32, safety_checker=None, requires_safety_checker=False)
    pipe.to(device)
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe.unet.to(device=device, dtype=torch.float32)  # Use torch.float32 instead of torch.float16
    for i in range(0,n):
        chosen_trait, prompt = get_trait()
        number=f'{i}'
        padded_number=number.zfill(5)
        name=f'image_{padded_number}'
        img = pipe(prompt=prompt, negative_prompt=negative_prompt, width=512, height=512, num_inference_steps=25, guidance_scale=7, num_images_per_prompt=1, generator=gen).images[0]
        img.save(f"{name}.png")
        write_trait_to_json(chosen_trait,f'{name}.json')