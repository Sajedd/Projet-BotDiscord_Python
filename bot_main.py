import discord
from discord.ext import commands
import config
from command_history_manager import CommandHistoryManager
from utilities import format_history, validate_user_input
from football_motocross_quiz import build_football_motocross_tree
import random

bot = commands.Bot(command_prefix='!' , intents=discord.Intents.all())
history_manager = CommandHistoryManager()
quiz_tree = build_football_motocross_tree()
current_quiz_state = {}

@bot.event
async def on_ready():
    print(f'{bot.user.name} est parfaitement connecter à Discord!')

@bot.event
async def on_command_completion(ctx):
    command = ctx.command
    user_id = str(ctx.author.id)
    history_manager.add_command(user_id, command.name)

@bot.command(name='history')
async def history(ctx):
    user_id = str(ctx.author.id)
    user_history = history_manager.get_user_history(user_id)
    if user_history:
        formatted_history = format_history(user_history)
        await ctx.send(f"Votre historique de commandes :\n{formatted_history}")
    else:
        await ctx.send("Aucun historique de commandes disponible.")

@bot.command(name='last')
async def last(ctx):
    user_id = str(ctx.author.id)
    user_history = history_manager.get_user_history(user_id)
    if user_history:
        last_command = user_history[-1] 
        await ctx.send(f"Votre dernière commande était: {last_command}")
    else:
        await ctx.send("Aucune commande précédente trouvée.")


@bot.command(name='clear')
async def clear_history(ctx):
    user_id = str(ctx.author.id)
    history_manager.clear_history(user_id)
    await ctx.send("Votre historique de commandes a été effacé.")


@bot.command(name='reset')
async def reset_quiz(ctx):
    user_id = str(ctx.author.id)
    if user_id in current_quiz_state:
        del current_quiz_state[user_id]
    await ctx.send("Quiz réinitialisé.")

@bot.command(name='motocross_info')
async def motocross_info(ctx):
    motocross_brands = ["Yamaha", "KTM", "RMZ", "Honda"]
    info = f"Je peux parler de ces marques de motocross : {', '.join(motocross_brands)}. Quelle marque vous intéresse ?"
    await ctx.send(info)

@bot.command(name='football_facts')
async def football_facts(ctx):
    facts = "Le football est le sport le plus populaire au monde. Avez-vous une équipe préférée ?"
    await ctx.send(facts)

@bot.command(name='quiz')
async def start_quiz(ctx):
    user_id = str(ctx.author.id)
    current_quiz_state[user_id] = quiz_tree
    await ctx.send(quiz_tree.question)

@bot.command(name='answer')
async def answer_quiz(ctx, *, answer):
    user_id = str(ctx.author.id)
    if user_id not in current_quiz_state:
        await ctx.send("Veuillez d'abord commencer le quiz avec la commande !quiz.")
        return

    current_node = current_quiz_state[user_id]
    next_node = current_node.yes if answer.lower() in ['oui', 'yes'] else current_node.no

    if next_node is None:
        await ctx.send("Merci d'avoir participé au quiz!")
        del current_quiz_state[user_id]
    else:
        current_quiz_state[user_id] = next_node
        await ctx.send(next_node.question)
        

@bot.command(name=config.RANDOM_FACTS_COMMAND)
async def random_facts(ctx):
    facts_football = ["Fact 1 sur le football", "Fact 2 sur le football"]
    facts_motocross = ["Fact 1 sur le motocross", "Fact 2 sur le motocross"]
    selected_fact = random.choice(facts_football + facts_motocross)
    await ctx.send(selected_fact)

@bot.command(name=config.LEADERBOARD_COMMAND)
async def leaderboard(ctx):
    await ctx.send("Classement des meilleures équipes ou marques.")

@bot.command(name=config.UPCOMING_EVENTS_COMMAND)
async def upcoming_events(ctx):
    await ctx.send("Voici les événements à venir dans le monde du football et du motocross.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message):
        if message.mention_everyone is False:
            commands_guide = (
                "Voici quelques commandes que vous pouvez utiliser pour interagir avec moi:\n\n"
                "!history - Affiche votre historique de commandes.\n"
                "!last - Affiche la derniere commande realiser\n "
                "!reset - Réinitialise le quiz en cours.\n"
                "!motocross_info - Donne des informations sur le motocross.\n"
                "!football_facts - Partage des faits sur le football.\n"
                "!quiz - Commence un quiz interactif.\n"
                "!answer - Répond à une question du quiz.\n"
                "!random_facts - Peut afficher des faits aléatoires sur divers sujets.\n"
                "!leaderboard - Affiche probablement un tableau des scores ou un classement des utilisateurs.\n"
                "!upcoming_events - Peut montrer les événements à venir, peut-être liés au football ou au motocross.\n"
                "!clear - Permet de suprimer l'historique \n"
            )
            await message.channel.send(commands_guide)
        else:
            await message.channel.send("Bonjour ! Comment puis-je vous aider ?")

    await bot.process_commands(message)


bot.run(config.DISCORD_TOKEN)
