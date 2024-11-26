import streamlit as st

class ChatbotOffre:
    def __init__(self):
        self.questions = [
            {
                "question": "La fiabilité et la disponibilité sont-elles vos priorités principales ?",
                "options": ["Oui", "Non"],
                "key": "fiabilite_prioritaire"
            },
            {
                "question": "Est-ce que vous avez une contrainte importante sur le coût initial ?",
                "options": ["Oui", "Non"],
                "key": "cout_contrainte"
            },
            {
                "question": "Quelle est votre priorité pour la productivité énergétique ?",
                "options": ["Maximiser la production", "Priorité secondaire"],
                "key": "priorite_energie"
            },
            {
                "question": "Souhaitez-vous privilégier une solution réduisant fortement l'impact environnemental ?",
                "options": ["Oui", "Non"],
                "key": "impact_environnement"
            },
            {
                "question": "Votre projet nécessite-t-il une solution adaptée aux contraintes offshore ?",
                "options": ["Oui", "Non"],
                "key": "offshore_contraintes"
            },
            {
                "question": "Accepteriez-vous une phase pilote pour tester la solution ?",
                "options": ["Oui", "Non"],
                "key": "phase_pilote"
            }
        ]
        
        self.table_verite = {
            "GS10 Xi": {
                "fiabilite_prioritaire": "Oui",
                "cout_contrainte": "Non",
                "priorite_energie": "Priorité secondaire",
                "impact_environnement": "Oui",
                "offshore_contraintes": "Oui",
                "phase_pilote": "Oui"
            },
            "GS6 AP": {
                "fiabilite_prioritaire": "Non",
                "cout_contrainte": "Oui",
                "priorite_energie": "Maximiser la production",
                "impact_environnement": "Non",
                "offshore_contraintes": "Non",
                "phase_pilote": "Non"
            },
            "GS10 AP": {
                "priorite_energie": "Maximiser la production",
                "phase_pilote": "Non"
            }
        }

    def determiner_offre(self, reponses):
        for offre, criteres in self.table_verite.items():
            match = all(reponses.get(key) == value for key, value in criteres.items() if key in reponses)
            if match:
                return offre
        return "Aucune offre correspondante trouvée."

    def run(self):
        st.title("Chatbot de sélection d'offres")
        st.write("Répondez aux questions pour trouver l'offre la plus adaptée à vos besoins.")

        reponses = {}
        for question in self.questions:
            reponses[question["key"]] = st.radio(
                question["question"],
                question["options"],
                key=question["key"]
            )

        if st.button("Voir l'offre recommandée"):
            offre = self.determiner_offre(reponses)
            st.subheader(f"L'offre recommandée est : {offre}")

if __name__ == "__main__":
    bot = ChatbotOffre()
    bot.run()
