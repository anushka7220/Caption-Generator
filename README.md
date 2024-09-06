# Social Media Caption Generator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-brightgreen)
![LangChain](https://img.shields.io/badge/LangChain-0.0.12-yellow)
![LLM](https://img.shields.io/badge/LLM-LLama_2-orange)

![caption](https://github.com/user-attachments/assets/e131f476-3b8b-4054-be23-7a242c3af886)


A Streamlit application that generates engaging social media captions tailored to specific platforms using a fine-tuned LLama 2 Large Language Model (LLM). The application allows users to select the platform, tone, and length of the caption, ensuring content is optimized for various social media environments.


## Features

- **Customizable Captions**: Generate captions with specific tone and length based on the chosen social media platform.
- **Emoji Integration**: Automatically includes relevant emojis in the captions to enhance engagement.
- **Real-Time Performance**: Optimized with model quantization and caching for fast and efficient caption generation.

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, LangChain
- **Model**: LLama 2 (via CTransformers)
- **Deployment**: Local Environment

## Installation

### Prerequisites

- Python 3.8+
- Pip (Python package installer)

### Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/social-media-caption-generator.git
   cd social-media-caption-generator
   ```

2. **Create a Virtual Environment (Optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download the Model:**

   - Place the LLama 2 model file (`llama-2-7b-chat.ggmlv3.q8_0.bin`) in the `models/` directory.
   - Ensure the model path in the code points to the correct location.

5. **Run the Application:**

   ```bash
   streamlit run app.py
   ```

   The application will open in your default web browser at `http://localhost:8501`.

## Usage

1. **Enter the Topic**: Provide the topic for your social media post.
2. **Select the Platform**: Choose the social media platform (Instagram, Twitter, LinkedIn, TikTok).
3. **Choose the Tone**: Select the tone of the caption (Friendly, Professional, Humorous, Inspirational).
4. **Set Maximum Length**: Adjust the slider to set the maximum length of the caption.
5. **Generate**: Click the "Generate Caption" button to create your customized caption.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

## Contact

If you have any questions or feedback, feel free to reach out:

- **Email**: anushkasharma3704@gmail.com
- **LinkedIn**:(https://linkedin.com/in/anushka37)
- **GitHub**:(https://github.com/anushka7220)



