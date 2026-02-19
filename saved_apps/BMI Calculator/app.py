import customtkinter as ctk

class BMICalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("BMI Calculator")
        self.geometry("900x600")
        self.resizable(False, False)
        self.configure(bg="#2f2f2f", appearance_mode="dark")

        self.main_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#3f3f3f")
        self.main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.title_label = ctk.CTkLabel(self.main_frame, text="BMI Calculator", font=("Arial", 24), text_color="#ffffff")
        self.title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        self.weight_label = ctk.CTkLabel(self.main_frame, text="Weight (kg):", font=("Arial", 16), text_color="#cccccc")
        self.weight_label.grid(row=1, column=0, padx=10, pady=10)

        self.weight_entry = ctk.CTkEntry(self.main_frame, width=200, height=30, corner_radius=10, font=("Arial", 16), placeholder_text="Enter weight")
        self.weight_entry.grid(row=1, column=1, padx=10, pady=10)

        self.height_label = ctk.CTkLabel(self.main_frame, text="Height (m):", font=("Arial", 16), text_color="#cccccc")
        self.height_label.grid(row=2, column=0, padx=10, pady=10)

        self.height_entry = ctk.CTkEntry(self.main_frame, width=200, height=30, corner_radius=10, font=("Arial", 16), placeholder_text="Enter height")
        self.height_entry.grid(row=2, column=1, padx=10, pady=10)

        self.calculate_button = ctk.CTkButton(self.main_frame, text="Calculate BMI", command=self.calculate_bmi, width=200, height=40, corner_radius=10, font=("Arial", 16))
        self.calculate_button.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

        self.bmi_label = ctk.CTkLabel(self.main_frame, text="", font=("Arial", 16), text_color="#cccccc")
        self.bmi_label.grid(row=4, column=0, columnspan=2, padx=20, pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            bmi = weight / (height ** 2)
            self.bmi_label.configure(text=f"BMI: {bmi:.2f}")
            if bmi < 18.5:
                self.bmi_label.configure(text=f"BMI: {bmi:.2f} (Underweight)")
            elif bmi < 25:
                self.bmi_label.configure(text=f"BMI: {bmi:.2f} (Normal weight)")
            elif bmi < 30:
                self.bmi_label.configure(text=f"BMI: {bmi:.2f} (Overweight)")
            else:
                self.bmi_label.configure(text=f"BMI: {bmi:.2f} (Obese)")
        except ValueError:
            self.bmi_label.configure(text="Invalid input")

if __name__ == "__main__":
    app = BMICalculatorApp()
    app.mainloop()