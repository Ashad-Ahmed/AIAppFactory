import customtkinter as ctk

class InterestCalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.title("Simple Interest Calculator")
        self.geometry("900x600")

        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.principal_label = ctk.CTkLabel(self.main_frame, text="Principal Amount:")
        self.principal_label.grid(row=0, column=0, padx=10, pady=10)

        self.principal_entry = ctk.CTkEntry(self.main_frame, width=200)
        self.principal_entry.grid(row=0, column=1, padx=10, pady=10)

        self.rate_label = ctk.CTkLabel(self.main_frame, text="Annual Interest Rate (%):")
        self.rate_label.grid(row=1, column=0, padx=10, pady=10)

        self.rate_entry = ctk.CTkEntry(self.main_frame, width=200)
        self.rate_entry.grid(row=1, column=1, padx=10, pady=10)

        self.time_label = ctk.CTkLabel(self.main_frame, text="Time (Years):")
        self.time_label.grid(row=2, column=0, padx=10, pady=10)

        self.time_entry = ctk.CTkEntry(self.main_frame, width=200)
        self.time_entry.grid(row=2, column=1, padx=10, pady=10)

        self.calculate_button = ctk.CTkButton(self.main_frame, text="Calculate Simple Interest", command=self.calculate_interest)
        self.calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.result_label = ctk.CTkLabel(self.main_frame, text="Result:")
        self.result_label.grid(row=4, column=0, padx=10, pady=10)

        self.result_value = ctk.CTkLabel(self.main_frame, text="")
        self.result_value.grid(row=4, column=1, padx=10, pady=10)

    def calculate_interest(self):
        try:
            principal = float(self.principal_entry.get())
            rate = float(self.rate_entry.get())
            time = float(self.time_entry.get())

            interest = (principal * rate * time) / 100
            total_amount = principal + interest

            self.result_value.configure(text=f"Simple Interest: ${interest:.2f}\nTotal Amount: ${total_amount:.2f}")
        except ValueError:
            self.result_value.configure(text="Invalid input")

if __name__ == "__main__":
    app = InterestCalculatorApp()
    app.mainloop()