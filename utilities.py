import discord

def format_history(commands):
    if not commands:
        return "Aucune commande n'a été trouvée dans votre historique."
    formatted_history = "\n".join([f"{idx + 1}. {cmd}" for idx, cmd in enumerate(commands)])
    return formatted_history

def validate_user_input(input_str, expected_type):
    try:
        return expected_type(input_str)
    except ValueError:
        return None

def random_fact(facts):
    import random
    return random.choice(facts)

def embed_message(title, description, color=0x00ff00):
    embed = discord.Embed(title=title, description=description, color=color)
    return embed

