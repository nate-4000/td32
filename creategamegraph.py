import graphviz
import gas

game_file = gas.get("game.json")

def create_graph(game_file):
    dot = graphviz.Digraph(format='svg')
    dot.attr(rankdir='LR')
    for index, item in enumerate(game_file):
        dialog = item['dialog']
        dot.node(str(index), dialog)
    for index, item in enumerate(game_file):
        options = item['options']
        for option in options:
            target_index, label = option
            dot.edge(str(index), str(target_index), label=label)

    dot.render('game_graph')

create_graph(game_file)
