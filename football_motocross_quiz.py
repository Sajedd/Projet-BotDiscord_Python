class TreeNode:
    def __init__(self, question, yes=None, no=None):
        self.question = question
        self.yes = yes
        self.no = no

def build_football_motocross_tree():
    root = TreeNode("Préférez-vous le football ou le motocross ?")

    # Branche pour les amateurs de football
    football_branch = TreeNode("Qui est le meilleur dribbleur selon vous ?")
    football_branch.yes = TreeNode("Messi, Neymar ou quelqu'un d'autre ?", yes=TreeNode("Intéressant ! Parlons de Messi et Neymar."), no=TreeNode("D'accord, et qui alors ?"))
    football_branch.no = TreeNode("Préférez-vous discuter des buteurs comme Ronaldo ?", yes=TreeNode("Ronaldo est un choix populaire !"), no=TreeNode("Qui est votre joueur préféré alors ?"))

    motocross_branch = TreeNode("Quelle est votre marque de motocross préférée ?")
    motocross_branch.yes = TreeNode("Yamaha, KTM, ou une autre marque ?", yes=TreeNode("Yamaha et KTM sont des marques emblématiques !"), no=TreeNode("Quelle est alors votre marque préférée ?"))
    motocross_branch.no = TreeNode("Vous intéressez-vous plus aux pilotes qu'aux marques ?", yes=TreeNode("Les pilotes sont le cœur du sport !"), no=TreeNode("Parlons alors des courses elles-mêmes."))

    root.yes = football_branch
    root.no = motocross_branch

    return root

