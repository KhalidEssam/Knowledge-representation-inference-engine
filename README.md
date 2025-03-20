# Knowledge Representation Inference Engine

## Overview
The **Knowledge Representation Inference Engine** is a rule-based AI system that helps users determine which car to buy or rent based on a structured dialogue. By leveraging knowledge representation techniques, the engine analyzes user responses to contextual questions and applies logical inference to recommend suitable car options.

This engine is built using:
- **KQB** and **KRB** files for knowledge representation
- **PyKE (Python Knowledge Engine)** for inference and rule processing

## Features
- **Context-Aware Decision Making:** Uses structured questions and answers to refine car recommendations.
- **Rule-Based Inference:** Implements a knowledge-based approach to infer suitable car options.
- **Customizable Knowledge Base:** Users can modify and expand the knowledge base using KQB and KRB files.
- **Flexible Integration:** Can be incorporated into larger AI-driven recommendation systems.

## Installation
### Prerequisites
Ensure you have the following dependencies installed:
- Python (>=3.7)
- PyKE (`pip install pyke3`)

### Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/knowledge-representation-inference-engine.git
   cd knowledge-representation-inference-engine
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the engine:
   ```sh
   python main.py
   ```

## Usage
1. Start the engine.
2. Answer a series of questions about car preferences (e.g., budget, fuel type, usage needs).
3. The system will analyze responses and suggest the most suitable car.

## Configuration
- **KQB Files:** Define the knowledge base (facts and rules).
- **KRB Files:** Specify inference rules and logical reasoning patterns.

You can modify these files to enhance or customize the inference process.

## Example Interaction
```
User: I need a fuel-efficient car for city driving.
System: Do you prefer electric, hybrid, or gasoline?
User: Hybrid.
System: Based on your preferences, we recommend the Toyota Prius or Honda Insight.
```

## Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch-name`).
3. Commit your changes and push to your fork.
4. Submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries or support, reach out at **khaledesam384@gmail.com** or open an issue in the repository.

---
Happy coding! 🚀

