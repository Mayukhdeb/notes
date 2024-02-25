from papyrus.home import PapyrusHome, Post

posts = [
    Post(
        filename="content/post/2024-02-24-phase-spectrum.md",
        slug="2024-02-24-phase-spectrum",
        title="The Phase Spectrum",
    ),
    Post(
        filename="content/post/2024-02-23-magnitude-constrained-featurevis.md",
        slug="2024-02-23-magnitude-constrained-featurevis",
        title="MaCo - Feature Visualization for Deeper Networks",
    ),
    Post(
        filename="content/post/2024-02-10-optically-pumped-magnetometers.md",
        slug="2024-02-10-optically-pumped-magnetometers",
        title="Optically Pumped Magnetometers",
    ),
    Post(
        filename="content/post/2024-02-10-animatediff-svd-moonshot.md",
        slug="2024-02-10-animatediff-svd-moonshot",
        title="Video Generation Models",
    ),
    Post(
        filename="content/post/2024-01-16-dpo-diffusion.md",
        slug="2024-01-16-dpo-diffusion",
        title="Direct Preference Optimization for Diffusion Models",
    ),
    Post(
        filename="content/post/2023-07-02-svd.md",
        slug="2023-07-02-svd",
        title="Singular Value Decomposition",
    ),
    Post(
        filename="content/post/2023-07-02-matrices.md",
        slug="2023-07-02-matrices",
        title="Matrices",
    ),
    Post(
        filename="content/post/2023-06-27-dreamsim.md",
        slug="2023-06-27-dreamsim",
        title="DreamSim",
    ),
    Post(
        filename="content/post/2023-05-30-mindeye.md",
        slug="2023-05-30-mindeye",
        title="MindEye: fMRI-to-Image with Contrastive Learning ",
    ),
    Post(
        filename="content/post/2023-05-10-brain-inspired-model-training.md",
        slug="2023-05-10-brain-inspired-model-training",
        title="BIMT: Brain Inspired Modular Training",
    ),
    Post(
        filename="content/post/2023-04-20-audioclip.md",
        slug="2023-04-20-audioclip",
        title="AudioCLIP: Extending CLIP to Image, Text and Audio",
    ),
    Post(
        filename="content/post/2023-04-04-things-meg-dataset.md",
        slug="2023-04-04-things-meg-dataset",
        title="THINGS: a multimodal dataset for investigating object representations in thehuman brain",
    ),
    Post(
        filename="content/post/2023-01-25-open-vocab-eeg-text-decoding.md",
        slug="2023-01-25-open-vocab-eeg-text-decoding",
        title="Open Vocabulary EEG-To-Text Decoding",
    ),
    Post(
        filename="content/post/2023-01-25-brain2image-gan.md",
        slug="2023-01-25-brain2image-gan",
        title="Brain2Image: Converting Brain Signals into Images",
    ),
    Post(
        filename="content/post/2023-01-01-neural-taskonomy.md",
        slug="2023-01-01-neural-taskonomy",
        title="Neural Taskonomy - using encodings from vision models to understand the human brain",
    ),
    Post(
        filename="content/post/2022-19-07-locating-and-editing-factual-associations-in-gpt.md",
        slug="2022-19-07-locating-and-editing-factual-associations-in-gpt",
        title="Locating and Editing Factual Knowledge in GPTs",
    ),
    Post(
        filename="content/post/2022-14-07-lms-mostly-know-what-they-know.md",
        slug="2022-14-07-lms-mostly-know-what-they-know",
        title="Language Models (mostly) Know What they know",
    ),
    Post(
        filename="content/post/2022-12-25-diffusion.md",
        slug="2022-12-25-diffusion",
        title="Order From Chaos (Part 1): Diffusion for image synthesis explained in simple words",
    ),
    Post(
        filename="content/post/2022-12-25-diffusion-code.md",
        slug="2022-12-25-diffusion-code",
        title="Order From Chaos (Part 2): Diffusion for image synthesis explained in code and a little bit of math",
    ),
    Post(
        filename="content/post/2022-12-24-clip-fields.md",
        slug="2022-12-24-clip-fields",
        title="CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory",
    ),
    Post(
        filename="content/post/2022-12-18-clippo-image-and-language-understanding-from-text-only.md",
        slug="2022-12-18-clippo-image-and-language-understanding-from-text-only",
        title="CLIPPO: Image and Language understanding from pixels only",
    ),
    Post(
        filename="content/post/2022-11-20-clip-fields.md",
        slug="2022-11-20-clip-fields",
        title="VPT: Video Pre-Training on Minecraft",
    ),
    Post(
        filename="content/post/2022-11-19-brain-to-text-communication-via-handwriting.md",
        slug="2022-11-19-brain-to-text-communication-via-handwriting",
        title="Brain to Text Communication via handwriting",
    ),
    Post(
        filename="content/post/2022-10-31-craftassist.md",
        slug="2022-10-31-craftassist",
        title="CraftAssist - LLMs on minecraft (?)",
    ),
    Post(
        filename="content/post/2022-09-27-ai-through-lens-of-cogsci.md",
        slug="2022-09-27-ai-through-lens-of-cogsci",
        title="Watching artificial intelligence through the lens of CogSci",
    ),
    Post(
        filename="content/post/2022-09-03-new-science-of-common-sense.md",
        slug="2022-09-03-new-science-of-common-sense",
        title="Towards a New Science of Common Sense",
    ),
    Post(
        filename="content/post/2022-08-07-parti-image-generation.md",
        slug="2022-08-07-parti-image-generation",
        title="Parti - Scaling LLMs for Text to Image tasks",
    ),
    Post(
        filename="content/post/2022-08-01-the-third-wave.md",
        slug="2022-08-01-the-third-wave",
        title="The Third Wave (?)",
    ),
    Post(
        filename="content/post/2022-04-16-transformer_interpretability_beyond_attention.md",
        slug="2022-04-16-transformer_interpretability_beyond_attention",
        title="Transformer intrepretability beyond attention",
    ),
    Post(
        filename="content/post/2022-04-16-self-consistency-imrpoves-chain-of-thought.md",
        slug="2022-04-16-self-consistency-imrpoves-chain-of-thought",
        title="Self-Consistency Improves Chain of Thought Reasoning in LMs",
    ),
    Post(
        filename="content/post/2022-04-16-lost-unsupervised-object-detection.md",
        slug="2022-04-16-lost-unsupervised-object-detection",
        title="LOST - Localizing objects with self supervised transformers",
    ),
    Post(
        filename="content/post/2022-04-16-knowledge_neurons.md",
        slug="2022-04-16-knowledge_neurons",
        title="Knowledge Neurons",
    ),
    Post(
        filename="content/post/2022-04-16-interpreting-language-models-with-contrastive-explanations.md",
        slug="2022-04-16-interpreting-language-models-with-contrastive-explanations",
        title="Interpreting LMs with contrastive explanations",
    ),
    Post(
        filename="content/post/2022-04-16-generic_attention_model_explainability.md",
        slug="2022-04-16-generic_attention_model_explainability",
        title="Generic Attention-model Explainability",
    ),
    Post(
        filename="content/post/2022-04-16-attention_flow.md",
        slug="2022-04-16-attention_flow",
        title="Attention Rollout",
    ),
]

home = PapyrusHome(
    title="Notes", body_markdown_filename="home.md", posts_folder="posts", posts=posts
)

home.compile(output_html_filename="index.html")
