from tkinter import Tk, Label, Button, StringVar, Entry, OptionMenu, Listbox, Scrollbar, Toplevel

class AllergyDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Allergy Detector App")

        # Screen 1
        self.screen1()

    def screen1(self):
        # Widgets for entering personal information
        self.name_label = Label(self.root, text="Name:")
        self.name_entry = Entry(self.root)
        self.age_label = Label(self.root, text="Age:")
        self.age_var = StringVar()
        self.age_entry = OptionMenu(self.root, self.age_var, *list(range(1, 101)))
        self.gender_label = Label(self.root, text="Gender:")
        self.gender_var = StringVar()
        self.gender_var.set("Male")
        self.gender_menu = OptionMenu(self.root, self.gender_var, "Male", "Female")

        # Grid placement for widgets
        self.name_label.grid(row=2, column=2, sticky="e")
        self.name_entry.grid(row=2, column=3)
        self.age_label.grid(row=3, column=2, sticky="e")
        self.age_entry.grid(row=3, column=3)
        self.gender_label.grid(row=4, column=2, sticky="e")
        self.gender_menu.grid(row=4, column=3)

        # Button to move to the next screen
        next_button = Button(self.root, text="Next", command=self.screen2)
        next_button.grid(row=5, columnspan=4)

    def screen2(self):
        # Retrieve personal information from screen 1
        self.name = self.name_entry.get()
        self.age = self.age_var.get()
        self.gender = self.gender_var.get()

        # Destroy widgets from screen 1
        self.name_label.destroy()
        self.name_entry.destroy()
        self.age_label.destroy()
        self.age_entry.destroy()
        self.gender_label.destroy()
        self.gender_menu.destroy()

        # Screen 2: Select symptoms
        self.symptoms_label = Label(self.root, text="Select Symptoms:")
        self.symptoms_listbox = Listbox(self.root, selectmode="multiple", exportselection=0)
        scrollbar = Scrollbar(self.root, command=self.symptoms_listbox.yview)
        self.symptoms_listbox.config(yscrollcommand=scrollbar.set)

        # List of symptoms
        self.symptoms = ["sneezing", "runny nose", "itchy or watery eyes", "fatigue", "difficulty breathing", "vomiting",
                          "swelling of lips, tongue or face", "hives", "abdominal pain", "nausea",
                          "redness and swelling at the site of sting", "itching", "chest tightness", "skin rash"]

        # Insert symptoms into the listbox
        for symptom in self.symptoms:
            self.symptoms_listbox.insert("end", symptom)

        # Grid placement for widgets
        self.symptoms_label.grid(row=0, column=0, columnspan=2)
        self.symptoms_listbox.grid(row=1, column=0, columnspan=2)
        scrollbar.grid(row=1, column=2, sticky="ns")

        # Button to proceed to the next screen
        detect_button = Button(self.root, text="Detect Allergy", command=self.screen3)
        detect_button.grid(row=2, columnspan=2)

        # Initialize the list to store selected symptoms
        self.selected_symptoms = []

    def screen3(self):
        # Retrieve selected symptoms from screen 2
        selected_indices = self.symptoms_listbox.curselection()
        self.selected_symptoms = [self.symptoms[i] for i in selected_indices]

        # Create a new window for displaying results
        result_window = Toplevel(self.root)
        result_window.title("Allergy Detection Results")

        # Display personal information
        Label(result_window, text="Name: {}".format(self.name)).grid(row=0, column=0, sticky="w")
        Label(result_window, text="Age: {}".format(self.age)).grid(row=1, column=0, sticky="w")
        Label(result_window, text="Gender: {}".format(self.gender)).grid(row=2, column=0, sticky="w")
        Label(result_window, text="Selected Symptoms: {}".format(", ".join(self.selected_symptoms))).grid(row=3, column=0, sticky="w")

        # Perform allergy detection
        detected_allergies = self.detect_allergies()

        # Display detected allergies
        Label(result_window, text="Detected Allergies: {}".format(", ".join(detected_allergies))).grid(row=4, column=0, sticky="w")

    def detect_allergies(self):
        # Mapping of allergies to their symptoms
        allergy_mapping = {
            'Pollen Allergy': ['sneezing', 'runny nose', 'itchy or watery eyes', 'fatigue'],
            'Peanut Allergy': ['swelling of lips, tongue or face', 'hives', 'abdominal pain', 'vomiting', 'nausea', 'difficulty breathing'],
            'Bee Sting Allergy': ['redness and swelling at the site of sting', 'hives', 'itching', 'difficulty breathing', 'chest tightness'],
            'Latex Allergy': ['skin rash', 'hives', 'itching', 'sneezing', 'runny nose', 'difficulty breathing']
        }

        # List to store detected allergies
        possible_allergies = []

        # Check for allergies based on selected symptoms
        for allergy, allergy_symptoms in allergy_mapping.items():
            if any(symptom in self.selected_symptoms for symptom in allergy_symptoms):
                possible_allergies.append(allergy)

        # If no allergies are detected, add a message
        if not possible_allergies:
            possible_allergies.append("No allergies detected")

        return possible_allergies


if __name__ == "__main__":
    # Initialize and run the Tkinter application
    root = Tk()
    app = AllergyDetectorApp(root)
    root.mainloop()
