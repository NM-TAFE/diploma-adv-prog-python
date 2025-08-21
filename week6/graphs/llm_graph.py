from collections import defaultdict
from dataclasses import dataclass

@dataclass
class WordNode:
    word: str
    count: int = 0  # Track occurrences for probability calculation

class WordGraph:
    def __init__(self):
        # Dictionary where keys are tuples (bigrams) and values are lists of next words with counts
        self.graph = defaultdict(list)

    def add_sentence(self, sentence):
        """Trains the graph using a sentence by adding bigram-to-next-word connections."""
        words = sentence.lower().split()
        
        # Use bigrams as context (need at least 3 words for bigram + next word)
        for i in range(len(words) - 2):
            current_bigram = (words[i], words[i + 1])  # Tuple of two words
            next_word = words[i + 2]

            # Check if the next word is already a known connection
            found = False
            for node in self.graph[current_bigram]:
                if node.word == next_word:
                    node.count += 1
                    found = True
                    break
            
            # If next word is not found, add it
            if not found:
                self.graph[current_bigram].append(WordNode(next_word, 1))

    def predict_next_word(self, phrase):
        """Predicts the most likely next word based on the last two words, using probabilities."""
        words = phrase.lower().split()
        if len(words) < 2:
            return "Need at least two words for prediction."
        
        last_bigram = (words[-2], words[-1])  # Use the last two words as context

        if last_bigram not in self.graph:
            return "No prediction available."

        # Calculate probabilities
        next_words = self.graph[last_bigram]
        total_count = sum(node.count for node in next_words)
        if total_count == 0:
            return "No prediction available."
        
        probabilities = [(node.word, node.count / total_count) for node in next_words]
        # Sort by probability (highest first)
        best = sorted(probabilities, key=lambda x: x[1], reverse=True)
        return best[0][0]  # Return the word with highest probability

    # def display_graph(self):
    #     """Displays bigram transitions and their occurrence counts."""
    #     for bigram, connections in self.graph.items():
    #         transitions = ", ".join(f"{node.word} ({node.count})" for node in connections)
    #         print(f"{' '.join(bigram)} → {transitions}")

# Example Usage
def main():
    predictor = WordGraph()
    
    # Train with example sentences
    predictor.add_sentence("The capital of France is Berlin")
    predictor.add_sentence("The capital of Germany is Berlin")
    predictor.add_sentence("The capital of Spain is Madrid")
    predictor.add_sentence("The capital of France is Paris")
    predictor.add_sentence("The capital of France is Paris")
    predictor.add_sentence("The capital of Italy is Rome")
    
    # Test predictions
    print("\nPredicted next word:")
    print("The capital →", predictor.predict_next_word("The capital"))
    print("of France →", predictor.predict_next_word("of France"))
    print("France is →", predictor.predict_next_word("France is"))

    # Display trained graph
    # print("\nWord Transition Graph:")
    # predictor.display_graph()

if __name__ == "__main__":
    main()