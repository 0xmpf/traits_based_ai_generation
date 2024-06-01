import json
import random

def load_traits(file_path):
    with open(file_path, 'r') as file:
        traits = json.load(file)
    return traits

def choose_trait(category):
    odds = [trait['odd'] for trait in category]
    chosen_trait = random.choices(category, weights=odds)[0]
    return chosen_trait['trait']

def generate_prompt(traits):
    # Modify depending on your traits.json
    origin = choose_trait(traits['origin'])
    hair_length = choose_trait(traits['hair']['length'])
    hair_color = choose_trait(traits['hair']['color'])
    hair_style = choose_trait(traits['hair']['style'])
    character = choose_trait(traits['character'])
    gender = choose_trait(traits['gender'])
    age = choose_trait(traits['age'])
    accessory = choose_trait(traits['accessories'])
    occupation = choose_trait(traits['occupation'])
    chosen_traits = {
        'origin': origin,
        'hair_length': hair_length,
        'hair_color': hair_color,
        'hair_style': hair_style,
        'character': character,
        'gender': gender,
        'age': age,
        'accessory': accessory,
        'occupation': occupation
    }

    # Custom prompt, depending on traits.json
    prompt = f"Faceshot Portrait of {character.lower()} {age.lower()} {origin} {gender.lower()}, {occupation.lower()}, with {hair_length.lower()} {hair_color.lower()} {hair_style.lower()} hair, wearing {accessory.lower()}, (masterpiece, extremely detailed skin, photorealistic, heavy shadow, dramatic and cinematic lighting, key light, fill light), sharp focus, BREAK epicrealism"

    return chosen_traits, prompt

def get_trait():
    traits_file = 'traits.json'
    traits = load_traits(traits_file)
    chosen_traits, prompt = generate_prompt(traits)
    return chosen_traits, prompt

def write_trait_to_json(chosen_traits, output_file):
    with open(output_file, 'w') as file:
        json.dump(chosen_traits, file, indent=2)
