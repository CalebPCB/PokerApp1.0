import tkinter as tk
from tkinter import messagebox

class PokerCardPickerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Poker Card Picker")

        self.selected_cards = set()
        self.max_selected_cards = 2
        self.saved_hands = []

        self.suits = {0: "♥", 1: "♦", 2: "♣", 3: "♠"}
        self.card_buttons = self.generate_card_buttons()

        self.create_save_button()
        self.create_show_saved_button()
        self.create_saved_hands_listbox()
        self.create_selected_cards_label()

    def generate_card_buttons(self):
        card_buttons = {}

        for suit in self.suits:
            cards = [f"{value}{suit}" for value in [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]]
            #cards.sort(reverse=True)
            
            for i, card in enumerate(cards):
                button = tk.Button(self.root, text=f"{str(card[0])}{self.suits[suit]}", width=3, height=2, command=lambda c=card: self.toggle_card(c))
                button.grid(row=i, column=suit, padx=5, pady=5)
                card_buttons[card] = button

        return card_buttons

    def create_save_button(self):
        save_button = tk.Button(self.root, text="Save", command=self.save_cards, font=("Helvetica", 12, "bold"))
        save_button.grid(row=len(self.card_buttons), column=0, columnspan=len(self.suits), pady=10)

    def create_show_saved_button(self):
        show_saved_button = tk.Button(self.root, text="Show Saved Hands", command=self.show_saved_hands, font=("Helvetica", 12, "bold"))
        show_saved_button.grid(row=len(self.card_buttons) + 1, column=0, columnspan=len(self.suits), pady=10)

    def create_saved_hands_listbox(self):
        self.saved_hands_listbox = tk.Listbox(self.root, height=15, width=20, font=("Helvetica", 12), selectbackground="#a6a6a6", selectmode=tk.SINGLE)
        self.saved_hands_listbox.grid(row=0, column=len(self.suits), rowspan=len(self.card_buttons), pady=10)

    def create_selected_cards_label(self):
        self.selected_cards_label = tk.Label(self.root, text="Selected Cards:", font=("Helvetica", 12, "bold"))
        self.selected_cards_label.grid(row=0, column=len(self.suits) + 1, pady=10)

    def toggle_card(self, card):
        if card in self.selected_cards:
            self.selected_cards.remove(card)
            self.card_buttons[card].config(bg="SystemButtonFace")
        elif len(self.selected_cards) < self.max_selected_cards:
            self.selected_cards.add(card)
            self.card_buttons[card].config(bg="#a6a6a6")
        else:
            messagebox.showinfo("Error", "You can only select up to 2 cards.")
        self.update_selected_cards_label()

    def update_selected_cards_label(self):
        self.selected_cards_label.config(text=f"Selected Cards: {', '.join(self.selected_cards)}")

    def save_cards(self):
        if len(self.selected_cards) == 2:
            self.saved_hands.append(set(self.selected_cards))
            messagebox.showinfo("Saved", f"Selected cards: {', '.join(self.selected_cards)} saved to your hand.")
            self.clear_selection()
            self.update_saved_hands_listbox()
        else:
            messagebox.showinfo("Error", "Please select 2 cards to save.")

    def clear_selection(self):
        for card in self.selected_cards:
            self.card_buttons[card].config(bg="SystemButtonFace")
        self.selected_cards.clear()
        self.update_selected_cards_label()

    def update_saved_hands_listbox(self):
        self.saved_hands_listbox.delete(0, tk.END)
        for i, hand in enumerate(self.saved_hands):
            formatted_hand = [f"{card[0]}{self.suits[int(card[1])]}" for card in hand]
            self.saved_hands_listbox.insert(tk.END, f"Hand {i + 1}: {', '.join(formatted_hand)}")

    def show_saved_hands(self):
        if not self.saved_hands:
            messagebox.showinfo("Saved Hands", "No hands saved yet.")
        else:
            self.update_saved_hands_listbox()
            messagebox.showinfo("Saved Hands", "Saved hands:\n\nSelect a hand from the list to view the cards.")

if __name__ == "__main__":
    root = tk.Tk()
    poker_picker_gui = PokerCardPickerGUI(root)
    root.mainloop()
