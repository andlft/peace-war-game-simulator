import customtkinter as ctk
from typing import List
from helpers.base_strategy import BaseStrategy
from collections import defaultdict
from helpers.game import Game
from itertools import combinations
from helpers.plot_results import plot_results

def run_GUI(strats: List[BaseStrategy], rounds: int) -> List[BaseStrategy]:
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    root = ctk.CTk()
    root.geometry("500x800")

    def return_strategies():
        selected_strategies = []
        for i, s_var in enumerate(strat_vars):
            if s_var.get() == 1:
                selected_strategies.append(strats[i])
        
        game_strats = combinations(selected_strategies, 2)

        results = defaultdict(lambda : 0)

        for strat_group in game_strats:
            game = Game(*strat_group)
            game_result = game.run_game(rounds)

            for key, value in game_result.items():
                results[key] += value

        plot_results(results=results)

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=30, fill="both", expand=True)

    label = ctk.CTkLabel(master=frame, text="Choose strategies:")
    label.pack(pady=5, padx=10)

    strat_vars = [ctk.IntVar() for _ in range(len(strats))]

    for i, strat in enumerate(strats): 
        checkbox = ctk.CTkCheckBox(
            master=frame,
            text=f"{strat.__name__}",
            variable=strat_vars[i]
        )
        checkbox.pack(pady=10, padx=10, anchor="w")

    button = ctk.CTkButton(
        master=frame,
        text="Run simulation",
        command=return_strategies
    )
    button.pack(pady=12, padx=10)

    root.mainloop()